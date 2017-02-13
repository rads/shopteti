from html import *
import nav_bar

def html(content):
    return html5([
        head([
            title('ShopTeti'),
            stylesheets()
        ]),
        body('', [
            nav_bar.html(),
            content
        ])
    ])

def stylesheets():
    return link('rel="stylesheet" href="/static/style.css"')
