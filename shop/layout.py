from html import *

def html(content):
    return html5([
        head([
            title('ShopTeti'),
            stylesheets()
        ]),
        body('', content)
    ])

def stylesheets():
    return link('rel="stylesheet" href="/static/style.css"')
