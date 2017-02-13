from html import *

def html():
    return div('class="NavBar"', [
        logo(),
        menu(),
        social_media_links()
    ])

def logo():
    return h1('class="Logo"', a('href="/"', 'Teti'))

def menu():
	return ul("class='Menu'", [
		li(a("href='/'", 'Home')),
		li(a("href='/products'", 'Products'))
	])

def social_media_links():
    return div('class="SocialMediaLinks"', 'social media links')

