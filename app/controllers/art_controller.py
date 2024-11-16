from flask import Blueprint, jsonify

# Create a blueprint for the art-related routes
art_bp = Blueprint('art', __name__)

@art_bp.route('/artists', methods=['GET'])
def get_artists():
    # Dummy data for now; replace with database or service logic later
    artists = [
        {"name": "Van Gogh", "style": "Post-Impressionism"},
        {"name": "Pablo Picasso", "style": "Cubism"}
    ]
    return jsonify(artists)

@art_bp.route('/artists/<int:artist_id>', methods=['GET'])
def get_artist(artist_id):
    # Simulate retrieving a single artist by ID
    return jsonify({"name": "Van Gogh", "style": "Post-Impressionism", "id": artist_id})
