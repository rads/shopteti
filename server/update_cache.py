import redis
import os
import requests

ETSY_API_KEY = os.environ.get('ETSY_API_KEY')
REDIS_URL = os.environ.get('REDIS_URL')
r = redis.from_url(REDIS_URL)

url = 'https://openapi.etsy.com/v2/shops/shopteti/listings/active'

response = requests.get(url + '?api_key='+ ETSY_API_KEY + '&includes=Images')
r.set(url, response.text)