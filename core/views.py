# Create your views here.
import json
import urllib2
import xml.utils.iso8601 as iso8601
import lxml.html
import itertools
from datetime import datetime, date, timedelta

from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Narrative, GuardianSearch, ReadTo

def home(request):
  narratives = Narrative.objects.all()

  for narrative in narratives:
    if not request.user.is_anonymous():
      try:
        read_to = ReadTo.objects.get(user=request.user,
                                     narrative=narrative)
      except ReadTo.DoesNotExist:
        read_to = None

      if read_to is not None:
        count = 0
        if narrative.last_updated > read_to.date: # Short circuit counting if the narrative hasn't any new stories since
          for article in narrative.results:
            if article['date'] > read_to.date:
              count += 1
            else:
              break
        narrative.new_count = count

  narratives = sorted(narratives, key=lambda narrative: narrative.last_updated, reverse=True)

  return render_to_response('home.html', {'narratives': narratives})

def narrative(request, id=None, slug=None, show_all=False):
  narrative = None
  if id is not None:
    narrative = Narrative.objects.get(pk=id)
  if slug is not None:
    narrative = Narrative.objects.get(slug=slug)

  if request.user.is_anonymous():
    read_to = None
  else:
    try:
      read_to = ReadTo.objects.get(user=request.user,
                                   narrative=narrative)
    except ReadTo.DoesNotExist:
      read_to = None
  
  results = list(narrative.results)

  for i, result in enumerate(results):
    result['int_id'] = i

  unread_i = 0
  if read_to is not None:
    for i in range(len(results)):
      if results[i]['date'] <= read_to.date:
        results[i]['read_to'] = True

        if i != 0:
          results[i-1]['last_unread'] = True

        unread_i = i

        break

    if unread_i == 0:
      show_all = True

    if not show_all:
      results = results[:unread_i]

  day_grouped = itertools.groupby(results, lambda article: article['date'].date()) 

  grouped_articles = []
  for date, articles in day_grouped:
    articles = list(articles)
    grouped_articles.append((date, articles))

  return render_to_response('narrative.html', {'narrative': narrative,
                                               'grouped_articles': grouped_articles,
                                               'read_to': read_to,
                                               'show_all': show_all,})

def create_narrative(request):
  return render_to_response('narrative_create.html', {})

def flush_narrative(request, slug=None):
  if slug is None:
    narratives = Narrative.objects.all()
  else:
    narratives = [Narrative.objects.get(slug=slug)]

  for narrative in narratives:
    for search in narrative.guardiansearch_set.all():
      search.cache = ""
      search.save()
    narrative.results

  if slug is not None:
    return HttpResponseRedirect(reverse('narrative_slug', kwargs={'slug': slug}))
  else:
    return HttpResponseRedirect(reverse('home'))

def set_read_to_narrative(request, slug):
  date = request.POST['date']
  date = datetime.fromtimestamp(iso8601.parse(date)) + timedelta(0,0,0,0,0,6)

  if request.user.is_anonymous():
    return HttpResponse('')

  narrative = Narrative.objects.get(slug=slug)
  
  try:
    read_to = ReadTo.objects.get(user=request.user, narrative=narrative)
  except ReadTo.DoesNotExist:
    read_to = None

  if read_to is not None:
    read_to.date = date
    read_to.save()
  else:
    read_to = ReadTo.objects.create(user=request.user,
                                    narrative=narrative,
                                    date=date)

  
  return HttpResponse('')
