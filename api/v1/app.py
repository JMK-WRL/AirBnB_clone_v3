#!/usr/bin/python3
"""
Commands to start the server
"""

import os
from flask import Flask
from werkzeug.exceptions import HTTPException
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def teardown(exception):
    """
    Closes the storage on teardown
    """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
