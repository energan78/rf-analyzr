from flask import Blueprint, jsonify, request, send_file, Response
import os
from datetime import datetime

bp = Blueprint('files', __name__, url_prefix='/api/files')

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@bp.route('/list', methods=['GET'])
def list_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, filename)):
            files.append({
                "name": filename,
                "created": datetime.fromtimestamp(os.path.getctime(os.path.join(UPLOAD_FOLDER, filename))).isoformat(),
                "size": os.path.getsize(os.path.join(UPLOAD_FOLDER, filename))
            })
    return jsonify({"files": files})

@bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if not file or not file.filename:
        return jsonify({"error": "No selected file"}), 400
    filename = file.filename
    if filename is None:
        return jsonify({"error": "Invalid filename"}), 400
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    return jsonify({
        "status": "success",
        "filename": filename
    })

@bp.route('/<filename>', methods=['GET'])
def download_file(filename):
    if not filename:
        return jsonify({"error": "Filename required"}), 400
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "File not found"}), 404
    return send_file(filepath, as_attachment=True)
