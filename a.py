from http.server import HTTPServer,BaseHTTPRequestHandler
# from urllib.parse import urlparse,parse_qs
class mybackend(BaseHTTPRequestHandler):
    def do_GET(self):
        crpath=self.path
        # path_part=crpath.split('/')
        if crpath in ('/','/home'):
            self.send_response(200)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Hello. Welcome to Dugduy coin api!')
        elif crpath in ('/price','/prize','/cost'):
            self.send_response(200)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Cost page!')
s=HTTPServer(('',80),mybackend)
print('Started server!')
s.serve_forever()