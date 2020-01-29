import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.wsgi

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h1 style='color: bl'>Welcome to our home page</h1>")


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")


def make_app():
    "initializes the web server"
    return tornado.web.Application([
        (r"/", GetHandler),
        (r"/home", HomeHandler),
        (r"/websocket", EchoWebSocket)
    ])


if __name__ == "__main__":
    app = make_app()
    application = tornado.wsgi.WSGIContainer(app)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
