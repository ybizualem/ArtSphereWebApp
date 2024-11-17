from flask import Blueprint, jsonify, request
from app.model.art_model import db, ArtPiece

art_bp = Blueprint("art", __name__)

# Fetch all art pieces
@art_bp.route("/", methods=["GET"])
def get_art_pieces():
    art_pieces = ArtPiece.query.all()
    return jsonify([{
        "id": art.id,
        "name": art.name,
        "artist": art.artist,
        "medium": art.medium
    } for art in art_pieces])

# Fetch a single art piece by ID
@art_bp.route("/<int:art_id>", methods=["GET"])
def get_art_piece(art_id):
    piece = ArtPiece.query.get(art_id)
    if piece:
        return jsonify({
            "id": piece.id,
            "name": piece.name,
            "artist": piece.artist,
            "medium": piece.medium
        })
    return jsonify({"error": "Art piece not found"}), 404

# Update an existing art piece
@art_bp.route("/<int:art_id>", methods=["PUT"])
def update_art_piece(art_id):
    piece = ArtPiece.query.get(art_id)
    if not piece:
        return jsonify({"error": "Art piece not found"}), 404

    # Get the data from the request
    data = request.get_json()

    # Update the fields with the data from the request
    piece.name = data.get("name", piece.name)
    piece.artist = data.get("artist", piece.artist)
    piece.medium = data.get("medium", piece.medium)

    # Commit the changes to the database
    db.session.commit()

    return jsonify({
        "id": piece.id,
        "name": piece.name,
        "artist": piece.artist,
        "medium": piece.medium
    })
