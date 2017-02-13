import requests
import nav_bar
import layout
from html import *

def html():
	return layout.html([
        nav_bar.html(),
        lookbook()
    ])

def social_media_links():
    return div('', 'social media links')

def lookbook():
	return div("class='Lookbook'", 'Lookbook One')
