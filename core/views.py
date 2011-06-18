# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from util import render_with_context

from models import Poll, Option

def home(request):
  return render_to_response('home.html')

def poll(request, id=None):
  poll = Poll.objects.get(id=id)

  return render_to_response('poll.html', {'poll': poll,})

def poll_vote(request, poll_id, option_id):
  poll = Poll.objects.get(id=poll_id)
  option = Option.objects.get(id=option_id)

  option.votes += 1

  option.save()

  return HttpResponseRedirect(reverse('poll', kwargs={'id': poll_id,}))

