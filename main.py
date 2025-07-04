from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

def main():
    print("Hello, world!")

def greet(name):
    print(f"Hello, {name}!")

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/health':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server = HTTPServer(('0.0.0.0', 8000), HealthHandler)
    server.serve_forever()

if __name__ == "__main__":
    Thread(target=run_server, daemon=True).start()
    main() 
