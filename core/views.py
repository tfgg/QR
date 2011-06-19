# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from util import render_with_context

import settings

from models import Poll, Option, Campaign, CampaignLink

def home(request):
  return render_to_response('home.html')

def poll(request, id=None):
  poll = Poll.objects.get(id=id)

  return render_to_response('poll.html', {'poll': poll, })

def poll_print(request, id=None):
  poll = Poll.objects.get(id=id)

  return render_to_response('poll_print.html', {'poll': poll,'rows': range(2), 'cols': range(3),})

def poll_vote(request, poll_id, option_id):
  poll = Poll.objects.get(id=poll_id)
  option = Option.objects.get(id=option_id)

  option.votes += 1

  option.save()

  return HttpResponseRedirect(reverse('poll', kwargs={'id': poll_id,}))

def campaign(request, campaign_id):
  campaign = Campaign.objects.get(id=campaign_id)

  return render_to_response('campaign.html', {'campaign': campaign,})

def campaign_poster(request, campaign_id):
  campaign = Campaign.objects.get(id=campaign_id)

  description_scale = 1.5 # / len(campaign.description)

  return render_to_response('campaign_poster.html', {'campaign': campaign, 'd_scale':description_scale,})

def campaign_stickers(request, campaign_id):
  campaign = Campaign.objects.get(id=campaign_id)

  return render_to_response('campaign_stickers.html', {'campaign': campaign,})

