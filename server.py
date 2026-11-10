import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Support clean URL routing
        clean_path = self.path.split('?')[0].rstrip('/')
        if clean_path == '' or clean_path == '/':
            self.path = '/index.html'
        elif clean_path == '/properties' or clean_path == '/buy' or clean_path == '/rent':
            self.path = '/properties.html'
        elif clean_path == '/property-details' or clean_path == '/details':
            self.path = '/property-details.html'
        elif clean_path == '/about' or clean_path == '/about-us':
            self.path = '/about.html'
        elif clean_path == '/contact' or clean_path == '/contact-us':
            self.path = '/contact.html'
        elif clean_path == '/login' or clean_path == '/portal' or clean_path == '/client-portal':
            self.path = '/login.html'
        elif not os.path.splitext(clean_path)[1] and os.path.exists(os.path.join(DIRECTORY, clean_path.lstrip('/') + '.html')):
            self.path = clean_path + '.html'
            
        return super().do_GET()

def run_server(port=PORT):
    for p in [port, 8000, 8080, 5000]:
        try:
            handler = CustomHTTPRequestHandler
            server = socketserver.TCPServer(("0.0.0.0", p), handler)
            server.allow_reuse_address = True
            print(f"Élora Estates Portal server running at http://localhost:{p}")
            print(f"Serving directory: {DIRECTORY}")
            sys.stdout.flush()
            server.serve_forever()
        except OSError as e:
            if "address already in use" in str(e).lower() or e.errno == 10048:
                print(f"Port {p} is in use, trying next port...")
                continue
            raise

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    run_server(port)
