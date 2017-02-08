from html import *

def html():
	return ul("class='NavBar'", [
		home(),
		li(a("href='/products'", 'Products'))
	])

def home():
	return li(a("href='/'", 'Home'))