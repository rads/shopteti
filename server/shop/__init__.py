import os
import products_page as products
import index_page as index
import redis

ETSY_API_KEY = os.environ["ETSY_API_KEY"]
REDIS_URL = os.environ["REDIS_URL"]

def index_page():
	return index.html()
	
def products_page():
	redis_client = redis.from_url(REDIS_URL)
	response_text = redis_client.get('https://openapi.etsy.com/v2/shops/shopteti/listings/active')
	return products.html(response_text)

def debug(x):
	file = open("/tmp/shopteti", 'w')
	file.write(str(x))
	file.close()