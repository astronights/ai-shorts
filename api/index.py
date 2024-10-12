from .services.instagram import instagram
from .config import CredentialConfig, URLConfig, ContentConfig

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
