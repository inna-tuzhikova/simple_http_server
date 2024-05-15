from http.server import BaseHTTPRequestHandler, HTTPServer

def run_server(host, port):
    httpd = HTTPServer((host, port), HTTPGetHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HTTPGetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<html><head><meta charset="utf-8">'.encode())
        self.wfile.write('<title>Простой HTTP-сервер.</title></head>'.encode())
        self.wfile.write('<body>Got GET Request here</body></html>'.encode())


run_server('python_http_server', 8080)
