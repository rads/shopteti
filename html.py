## Rad's Simple HTML Framework

def div(attributes, content):
	return '<div ' + attributes + '>' + content + '</div>'

def a(attributes, content):
	return '<a ' + attributes + '>' + content + '</a>'

def li(content):
	return '<li>' + content + '</li>'

def ul(attributes, items):
	return '<ul ' + attributes + '>' + ''.join(items) + '</ul>'