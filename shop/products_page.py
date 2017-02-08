import requests

def html(api_key):
	json = get_data(api_key)
	return format_data(json)

def get_data(api_key):
	response = requests.get('https://openapi.etsy.com/v2/shops/shopteti/listings/active?api_key='+ api_key + '&includes=Images')
	json = response.json()
	return json

def format_data(json):
	results = json["results"]
	image_tags = []
	for listing in results:
		image_url = listing["Images"][0]["url_170x135"]
		image_tags.append("<img src=" + image_url + '>')
	return "\n".join(image_tags)