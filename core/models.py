from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

import settings
from settings import bitly_username, bitly_key

import urllib
import urllib2
import json
from datetime import datetime

def bitly_shorten(url):
  url = urllib.quote(url)
  response = urllib2.urlopen("http://api.bitly.com/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=json" % (bitly_username, bitly_key, url))
  
  data = json.loads(response.read())
  print data 
  return data['data']['url']

class Poll(models.Model):
  question = models.TextField(default="placeholder question")
  type = models.TextField(choices=(('sms', 'SMS shortcode'),
                                   ('uri', 'Browser URL')))

  def get_absolute_url(self):
    pass
  
  def __unicode__(self):
    return self.question

class Option(models.Model):
  poll = models.ForeignKey(Poll)
  text = models.TextField(default="placeholder option")

  votes = models.IntegerField(default=0)

  def sms(self):
    if self.poll.type == 'sms':
      return "smsto:5480605:TESTPOLL %d/%d" % (self.poll.id, self.id)
    elif self.poll.type == 'uri':
      return "%s%s" % ("http://localhost:8000", reverse('poll_vote', kwargs={'poll_id': self.poll.id,
                                                   'option_id': self.id,}))
    else:
      return "bad type"

  def __unicode__(self):
    return "%s - %s (%d)" % (self.poll.question, self.text, self.votes)

class Campaign(models.Model):
  name = models.CharField(max_length=2048)
  description = models.TextField()
  donate_link = models.CharField(max_length=2048,null=True)
  short_link = models.CharField(max_length=2048,blank=True,null=True)

  shortcode_number = models.CharField(max_length=256,null=True)
  shortcode_content = models.CharField(max_length=256,null=True)

  def __unicode__(self):
    return self.name

  def get_short_url(self):
    print type(self.short_link)
    if self.short_link is None:
      self.short_link = bitly_shorten(self.get_absolute_url())
      self.save()

    return self.short_link

  def get_absolute_url(self):
    return "%s%s" % (settings.BASE_URL, reverse('campaign', kwargs={'campaign_id': self.id,}))

class CampaignLink(models.Model):
  url = models.CharField(max_length=2048)
  name = models.CharField(max_length=2048)
  campaign = models.ForeignKey(Campaign)

  def __unicode__(self):
    return "%s - %s" % (self.campaign.name, self.name)
