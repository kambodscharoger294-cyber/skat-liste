import http.server, os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


class H(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html", "/skat"):
            self.path = "/skat-liste.html"
        super().do_GET()

    def log_message(self, *a):
        pass


http.server.ThreadingHTTPServer(("0.0.0.0", 8787), H).serve_forever()
