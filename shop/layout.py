from html import *
import nav_bar

def html(content):
    return html5([
        head([
            title('ShopTeti'),
            stylesheets()
        ]),
        body('', [
            logo(),
            nav_bar.html(),
            content
        ])
    ])

def logo():
    return h1('class="Logo"', 'Teti')

def stylesheets():
    return link('rel="stylesheet" href="/static/style.css"')
