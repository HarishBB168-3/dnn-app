from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

handler = partial(SimpleHTTPRequestHandler, directory='./public')
server_object = HTTPServer(('', 3000), handler)
server_object.serve_forever()
