#!/usr/bin/python3
"""
Jsonifying code
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    return jsonify({"status": "OK"})

@app_views.route('api/v1/stats', methods=['GET'], strict_slashes=False)
def stats():
    classes = {
            'amenities': 'Amenity',
            'cities': 'City',
            'places': 'Place',
            'reviews': 'Review',
            'states': 'States',
            'users': 'User'
            }
    stats_dict = {}
    for key, value in classes.items():
        stats_dict[key] = storage.count(value)

    return jsonify(stats_dict)
