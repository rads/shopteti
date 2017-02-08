import os
import products_page as products
import index_page as index

ETSY_API_KEY = os.environ["ETSY_API_KEY"]

def index_page():
	return index.html(ETSY_API_KEY)
	
def products_page():
	return products.html()

def debug(x):
	file = open("/tmp/shopteti", 'w')
	file.write(str(x))
	file.close()