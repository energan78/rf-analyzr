# Initialize routes package

from .rf_routes import rf_routes
from .analysis_routes import analysis_routes
from .file_routes import file_routes
from .signals_routes import signals_routes

def register_routes(app):
    """Register all blueprint routes"""
    app.register_blueprint(rf_routes)
    app.register_blueprint(analysis_routes)
    app.register_blueprint(file_routes)
    app.register_blueprint(signals_routes)
