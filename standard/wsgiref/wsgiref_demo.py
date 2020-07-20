from wsgiref.simple_server import  make_server, demo_app

ws = make_server("127.0.0.1", 9999, demo_app)
ws.serve_forever()
