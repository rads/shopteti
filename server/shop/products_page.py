import requests
import layout
import json

def html(response_text):
	response_json = json.loads(response_text)
	return layout.html([format_data(response_json)])

def format_data(json):
	results = json["results"]
	image_tags = []
	for listing in results:
		image_url = listing["Images"][0]["url_170x135"]
		image_tags.append("<img src=" + image_url + '>')
	return "\n".join(image_tags)
