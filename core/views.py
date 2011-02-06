# Create your views here.
import json
import urllib2
import xml.utils.iso8601 as iso8601
import lxml.html
import itertools
from datetime import datetime, date, timedelta

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Narrative, GuardianSearch

def home(request):
  narratives = Narrative.objects.all()

  narratives = sorted(narratives, key=lambda narrative: narrative.last_updated, reverse=True)

  return render_to_response('home.html', {'narratives': narratives})

def narrative(request, id=None, slug=None):
  narrative = None
  if id is not None:
    narrative = Narrative.objects.get(pk=id)
  if slug is not None:
    narrative = Narrative.objects.get(slug=slug)

  read_to = datetime.now() - timedelta(3) 
  results = list(narrative.results)
  day_grouped = itertools.groupby(results, lambda article: article['date'].date()) 

  grouped_articles = []
  done_read_to = False
  for date, articles in day_grouped:
    articles = list(articles)
    for article in articles:
      if not done_read_to and article['date'] < read_to:
        article['read_to'] = True
        done_read_to = True
      else:
        article['read_to'] = False
    grouped_articles.append((date, articles))

  return render_to_response('narrative.html', {'narrative': narrative,
                                               'grouped_articles': grouped_articles,
                                               'read_to': read_to,})

def create_narrative(request):
  return render_to_response('narrative_create.html', {})

def flush_narrative(request, slug):
  narrative = Narrative.objects.get(slug=slug)
  for search in narrative.guardiansearch_set.all():
    search.cache = ""
    search.save()
  return HttpResponseRedirect(reverse('narrative_slug', kwargs={'slug': slug}))
