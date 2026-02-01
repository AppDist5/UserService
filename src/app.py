from flask import Flask
from flask_cors import CORS
from src.routes.user_routes import user_bp
from src.middlewares.error_handler import error_handler

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(user_bp, url_prefix='/api/users')

    @app.route('/health', methods=['GET'])
    def health():
        return {'status': 'OK', 'service': 'user-service'}, 200

    app.register_error_handler(Exception, error_handler)

    return app
