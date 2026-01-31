from flask import Flask, send_from_directory
from flask_cors import CORS
import os
import sys

STATIC_DIR = sys.argv[1] if len(sys.argv) > 1 else '.'

app = Flask(__name__, static_folder=None)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve(path):
    return send_from_directory(STATIC_DIR, path)

if __name__ == '__main__':
    print(f"目录: {os.path.abspath(STATIC_DIR)}")
    app.run(host='127.0.0.1', port=53421, threaded=True)
