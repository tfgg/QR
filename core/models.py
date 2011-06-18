from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

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

