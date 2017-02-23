## Rad's Simple HTML Framework

def content_str(str_or_list):
    if isinstance(str_or_list, list):
        return ''.join(map(content_str, str_or_list))
    else:
        return str_or_list

def div(attributes, content):
	return '<div ' + attributes + '>' + content_str(content) + '</div>'

def a(attributes, content):
	return '<a ' + attributes + '>' + content_str(content) + '</a>'

def li(content):
	return '<li>' + content_str(content) + '</li>'

def ul(attributes, content):
	return '<ul ' + attributes + '>' + content_str(content) + '</ul>'

def style(attributes, content):
    return '<style ' + attributes + '>' + content_str(content) + '</style>'

def link(attributes):
    return '<link ' + attributes + '>'

def body(attributes, content):
	return '<body ' + attributes + '>' + content_str(content) + '</body>'

def head(content):
	return '<head>' + content_str(content) + '</head>'

def title(content):
	return '<title>' + content_str(content) + '</title>'

def h1(attributes, content):
	return '<h1 ' + attributes + '>' + content_str(content) + '</h1>'

def html5(content):
    return '<!DOCTYPE html><html lang="en">' + content_str(content) + '</html>'

def meta(attributes):
	return '<meta ' + attributes + '>'
