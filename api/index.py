from .services.instagram import instagram
from .services.serving import serving
from .services.cleanup import cleanup
from .config import CredentialConfig, URLConfig, ContentConfig

import time
import threading
from uuid import uuid4

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = str(uuid4())
    
    # Load configuration
    app.config.from_object(CredentialConfig)
    app.config.from_object(URLConfig)
    app.config.from_object(ContentConfig)

    # Register blueprints
    app.register_blueprint(instagram, url_prefix='/instagram')
    app.register_blueprint(serving, url_prefix='/serving')

    def task_wrapper():
        '''Run the delete_files task at the specified interval.'''
        while True:
            cleanup()
            time.sleep(600)

    thread = threading.Thread(target=task_wrapper, daemon=True)
    thread.start()

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    return app

app = create_app()

# Entry point for Vercel
def main(request):
    # Use request context for Flask
    with app.request_context(request):
        return app.full_dispatch_request()

# For local development
if __name__ == '__main__':
    app.run(debug=True)
