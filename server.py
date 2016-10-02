import falcon
import shop

class IndexPage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = shop.images()
        resp.content_type = "text/html"

app = falcon.API()
app.add_route('/', IndexPage())
