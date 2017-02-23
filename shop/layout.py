from html import *
import nav_bar

def html(content):
    return html5([
        head([
            title('ShopTeti'),
            stylesheets(),
            google_verification(),
        ]),
        body('', [
            nav_bar.html(),
            content,
            scripts(),
        ])
    ])

def stylesheets():
    return link('rel="stylesheet" href="/static/style.css"')

def google_verification():
    return meta("name='google-site-verification' content='KVc0sJG_de4fYViq10IYiDAlJsloP6ZcxUxpXVhRj3s'")

def scripts():
    # <script src="build.js"></script>
    return script('src="/static/build.js"', '')