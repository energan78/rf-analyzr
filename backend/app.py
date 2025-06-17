from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Import routes after app initialization
from routes import rf_routes, analysis_routes, file_routes

# Register blueprints
app.register_blueprint(rf_routes.bp)
app.register_blueprint(analysis_routes.bp)
app.register_blueprint(file_routes.bp)

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
