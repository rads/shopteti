import falcon
import shop

from static_middleware import StaticMiddleware

class IndexPage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = shop.index_page()
        resp.content_type = "text/html"

class ProductsPage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = shop.products_page()
        resp.content_type = "text/html"


app = falcon.API()
app.add_route('/', IndexPage())
app.add_route('/products', ProductsPage())

app = StaticMiddleware(app)
