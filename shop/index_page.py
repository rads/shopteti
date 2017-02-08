import requests

def html():
	return nav_bar() + lookbook()

def lookbook():
	return div('Lookbook One', "class='Lookbook'")

def nav_bar():
	list_items = [
		li(a('Home', "href='/'")),
		li(a('Products', "href='/products'"))
	]
	return ul(list_items, "class='NavBar")

## Rad's Simple HTML Framework

def div(content, attributes):
	return '<div ' + attributes + '>' + content + '</div>'

def a(content, attributes):
	return '<a ' + attributes + '>' + content + '</a>'

def li(content):
	return '<li>' + content + '</li>'

def ul(items, attributes):
	return '<ul ' + attributes + '>' + ''.join(items) + '</ul>'