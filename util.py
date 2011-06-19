from django.template import RequestContext
from django.shortcuts import render_to_response

def render_with_context(request, *args, **kwargs):
  kwargs['context_instance'] = RequestContext(request)
  return render_to_response(*args, **kwargs)
