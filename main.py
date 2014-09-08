from tornado import websocket
import os.path
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/index.html")

class EchoWebSocket(websocket.WebSocketHandler):
    
    def check_origin(self, origin):
        return True

    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"

application = tornado.web.Application([ (r"/", MainHandler), (r"/websocket", EchoWebSocket),], debug=True, static_path=os.path.join(os.path.dirname(__file__), 'static'))


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
