import urllib2
import json
from datetime import datetime

endpoint = "http://content.guardianapis.com"
key = "uct3rztj38km5gcnwaeqmk3z"

bitly_username = "caramelcarrot"
bitly_key = "R_4b93f4028596afc8a62dd140188d3644"

def bitly_shorten(url):
  response = urllib2.urlopen("http://api.bitly.com/v3/shorten?login=%s&apiKey=%s&longUrl=%s&format=json" % (bitly_username, bitly_key, url))
  
  return json.loads(response.read())['data']['url']

print bitly_shorten("http://www.guardian.co.uk")

