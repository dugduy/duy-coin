from http.server import HTTPServer,BaseHTTPRequestHandler
from duycoin import duycoin
from json import dumps
# from urllib.parse import urlparse,parse_qs

dugduy=duycoin(1000,'DugDuy coin',5)

class mybackend(BaseHTTPRequestHandler):
    def do_GET(self):
        crpath=self.path
        path_part=crpath.split('/')[1:]
        print(path_part)
        if crpath in ('/','/home'):
            self.send_response(200)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Hello. Welcome to Dugduy coin api!')
        elif crpath in ('/price','/prize','/cost'):
            self.send_response(200)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(str(dugduy.price).encode())
        elif path_part[0] in ['buy','get','take']:
            self.send_response(200)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            if dugduy.buy(int(path_part[1])):
                self.wfile.write(dumps({'sucess':1,'msg':'You buyed %s coin(s).'%path_part[1]}).encode())
            else:
                self.wfile.write(dumps({'sucess':0,'msg':'%s coins is bigger than our release! Please try smaller number!'%path_part[1]}).encode())
        elif path_part[0] in ['cell','out','take']:
            self.send_response(200)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            dugduy.cell(int(path_part[1]))
            self.wfile.write(dumps({'sucess':1,'msg':'You celled %s coin(s).'%path_part[1]}).encode())
        else :
            self.send_response(404)
            self.send_header('content-type','text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b'Opps! Something went wrong!<br>Are you a hacker?')
s=HTTPServer(('',80),mybackend)
print('Started server!')
s.serve_forever()