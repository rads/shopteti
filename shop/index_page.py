import requests
import nav_bar
from html import *

def html():
	return nav_bar.html() + lookbook()

def lookbook():
	return div("class='Lookbook'", 'Lookbook One')