from flask import Blueprint, jsonify
from app.models import ArtPiece

art_bp = Blueprint("art", __name__)

@art_bp.route("/", methods=["GET"])
def get_art_pieces():
    art_pieces = ArtPiece.query.all()
    return jsonify([{
        "id": art.id,
        "name": art.name,
        "artist": art.artist,
        "medium": art.medium
    } for art in art_pieces])

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
