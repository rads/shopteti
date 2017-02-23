from html import *
import social_media_links

def html():
    return div('class="NavBar"', [
        logo(),
        menu(),
        social_media_links.html()
    ])

def logo():
    return h1('class="Logo"', a('href="/"', 'Teti'))

def menu():
	return ul("class='Menu'", [
		li(a("href='/'", 'Home')),
		li(a("href='/products'", 'Products'))
	])
