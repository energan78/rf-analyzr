from flask import Blueprint, jsonify, request, current_app
import os
from werkzeug.utils import secure_filename

file_routes = Blueprint('file', __name__, url_prefix='/api/files')

ALLOWED_EXTENSIONS = {'iq', 'raw', 'dat', 'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_routes.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.root_path, 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        file.save(os.path.join(upload_folder, filename))
        return jsonify({'filename': filename}), 200
    
    return jsonify({'error': 'File type not allowed'}), 400

@file_routes.route('/list', methods=['GET'])
def list_files():
    upload_folder = os.path.join(current_app.root_path, 'uploads')
    os.makedirs(upload_folder, exist_ok=True)
    files = []
    for filename in os.listdir(upload_folder):
        if allowed_file(filename):
            file_path = os.path.join(upload_folder, filename)
            files.append({
                'name': filename,
                'size': os.path.getsize(file_path),
                'modified': os.path.getmtime(file_path)
            })
    return jsonify({'files': files})
