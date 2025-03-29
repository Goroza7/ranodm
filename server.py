from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME', 'world')
    return Response(f"Hello, {name}!\n")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Default to 8080
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    
    server = make_server('0.0.0.0', port, app)
    print(f"Serving on port {port}...")
    server.serve_forever()
