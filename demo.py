#!/usr/bin/env python

import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line, define, options

define("host", default='localhost', help="主机地址", type=str)
define("port", default=8000, help="主机端口", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("哈哈哈哈哈哈哈")


class AifeiHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("不想敲代码")


class JiangPangpangHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("我想躺着就把钱赚了")


class TestGetHandler(tornado.web.RequestHandler):
    def get(self):
        # 接收 URL 中的参数
        name = self.get_argument('name')
        self.write("%s但求一醉" % name)


class TestPostHandler(tornado.web.RequestHandler):
    def get(self):
        html = '''
            <form action="/test/post" method="POST">
            姓名: <input type="text" name="name">
            <br>
            城市: <input type="text" name="city">
            <input type="submit">
            </form>
        '''
        self.write(html)

    def post(self):
        name = self.get_argument('name')
        city = self.get_argument('city')

        self.write('%s 生活在 %s' % (name, city))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/foo", AifeiHandler),
        (r"/bar", JiangPangpangHandler),
        (r"/test/get", TestGetHandler),
        (r"/test/post", TestPostHandler),
    ])


if __name__ == "__main__":
    parse_command_line()

    app = make_app()
    print('server running on %s:%s' % (options.host, options.port))
    app.listen(options.port, options.host)

    loop = tornado.ioloop.IOLoop.current()
    loop.start()
