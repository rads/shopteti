import requests
import os
ETSY_API_KEY = os.environ["ETSY_API_KEY"]

def images():
	r = requests.get('https://openapi.etsy.com/v2/shops/shopteti/listings/active?api_key='+ ETSY_API_KEY + '&includes=Images')
	json = r.json()
	results = json["results"]
	image_tags = []
	for listing in results:
		image_url = listing["Images"][0]["url_170x135"]
		image_tags.append("<img src=" + image_url + '>')
	return "\n".join(image_tags)