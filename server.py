
import falcon

class IndexPage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ('\nTwo things awe me most, the starry sky '
                     'above me and the moral law within me.\n'
                     '\n'
                     '    ~ Immanuel Kant\n\n')

class HelloPage(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'hello'

app = falcon.API()
app.add_route('/', IndexPage())
app.add_route('/hello', HelloPage())