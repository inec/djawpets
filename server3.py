import json
import urllib.request, urllib.parse, urllib.error
from os import curdir, sep
from urllib.parse import parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer

SITE_VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'
SITE_SECRET = '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
RECAPTCHA_RESPONSE_PARAM = 'g-recaptcha-response'.encode()

class Handler(BaseHTTPRequestHandler):
  def set_headers(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()

  def do_GET(self):
    self.set_headers();
    self.wfile.write((open(curdir + sep + 'feedback.html').read() % '').encode())

  def do_POST(self):
    self.set_headers();
    post_body = parse_qs(self.rfile.read(int(self.headers['Content-Length'])),encoding="utf-8")
    success = False
    print(len(post_body))
    print(post_body.keys())
    
    if RECAPTCHA_RESPONSE_PARAM in post_body:
      token = post_body[RECAPTCHA_RESPONSE_PARAM][0]
      print(token)
      rr=	   urllib.parse.urlencode(              {'secret': SITE_SECRET, 'response': token})
      print(rr)
      #f = urllib.request.urlopen(          SITE_VERIFY_URL, urllib.parse.urlencode(              {'secret': SITE_SECRET, 'response': token}, True))
      f=urllib.request.urlopen(          SITE_VERIFY_URL,rr.encode())
      resp=f.read()
      print(resp)
      if json.loads(resp).get("success"):
        success = True
    if success:
      message = 'Thanks for the feedback!'
    else:
      print("t")
      message = 'There was an error.'
    self.wfile.write((open(curdir + sep + 'feedback.html').read() % message ).encode())

if __name__ == '__main__':
  httpd = HTTPServer(('', 8080), Handler)
  httpd.serve_forever()
