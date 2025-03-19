from flask import Blueprint, jsonify, request
from Backend.app.services.data_handler import load_data, save_data

# Initialize the Blueprint for routing
art_bp = Blueprint("art", __name__)

# Load initial data
df = load_data()

# In-memory cart to store selected art pieces
cart = []

# Route to fetch all art pieces
@art_bp.route("/", methods=["GET"])
def get_art_pieces():
    """Fetch all art pieces."""
    return jsonify(df.to_dict(orient="records")), 200


# Route to fetch a single art piece by ID
@art_bp.route("/<int:art_id>", methods=["GET"])
def get_art_piece(art_id):
    """Fetch a single art piece by ID."""
    global df
    if art_id >= len(df) or art_id < 0:
        return jsonify({"error": "Art piece not found"}), 404
    piece = df.iloc[art_id]
    return jsonify(piece.to_dict()), 200


# Route to add a new art piece
@art_bp.route("/", methods=["POST"])
def add_art_piece():
    """Add a new art piece."""
    global df
    new_piece = request.get_json()

    # Validate the presence of required fields
    required_fields = ["Education_URL", "Title", "Time Period", "Image", "Author", "Location"]
    missing_fields = [field for field in required_fields if field not in new_piece]
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

    # Add new piece to DataFrame and save
    df = df.append(new_piece, ignore_index=True)
    save_data(df)
    return jsonify(new_piece), 201


# Route to update an existing art piece by ID
@art_bp.route("/<int:art_id>", methods=["PUT"])
def update_art_piece(art_id):
    """Update an existing art piece."""
    global df
    updated_data = request.get_json()

    if art_id >= len(df) or art_id < 0:
        return jsonify({"error": "Art piece not found"}), 404

    # Update fields in the DataFrame
    for key, value in updated_data.items():
        if key in df.columns:
            df.loc[art_id, key] = value

    save_data(df)
    return jsonify({"message": "Art piece updated", "updated": updated_data}), 200


# Route to delete an art piece by ID
@art_bp.route("/<int:art_id>", methods=["DELETE"])
def delete_art_piece(art_id):
    """Delete an art piece."""
    global df
    if art_id >= len(df) or art_id < 0:
        return jsonify({"error": "Art piece not found"}), 404

    # Delete the piece and reset the index
    df = df.drop(index=art_id).reset_index(drop=True)
    save_data(df)
    return jsonify({"message": "Art piece deleted"}), 200


# Route to fetch all items currently in the cart
@art_bp.route("/cart", methods=["GET"])
def get_cart():
    """Fetch all items in the cart."""
    return jsonify(cart), 200


# Route to add an art piece to the cart by its ID
@art_bp.route("/cart", methods=["POST"])
def add_to_cart():
    """Add an art piece to the cart by its ID."""
    global cart, df
    data = request.get_json()
    art_id = data.get("art_id")

    # Validate the art_id
    if art_id is None or art_id >= len(df) or art_id < 0:
        return jsonify({"error": "Invalid art ID"}), 400

    # Fetch the art piece
    item = df.iloc[art_id].to_dict()

    # Check if the item is already in the cart
    if item in cart:
        return jsonify({"message": "Item already in the cart"}), 400

    # Add the item to the cart
    cart.append(item)
    return jsonify({"message": "Item added to cart", "item": item}), 201


# Route to fetch the profile of a specific art piece
@art_bp.route("/profile/<int:art_id>", methods=["GET"])
def get_art_piece_profile(art_id):
    """Fetch the profile of a specific art piece."""
    global df

    # Check if the ID exists
    if art_id >= len(df) or art_id < 0:
        return jsonify({"error": "Art piece not found"}), 404

    # Fetch and return the profile details
    piece = df.iloc[art_id].to_dict()
    return jsonify({
        "Education_URL": piece.get("Education_URL"),
        "Title": piece.get("Title"),
        "Time Period": piece.get("Time Period"),
        "Image": piece.get("Image"),
        "Author": piece.get("Author"),
        "Location": piece.get("Location")
    }), 200


# Route to search for art pieces based on a query string
@art_bp.route("/search", methods=["GET"])
def search_art_pieces():
    """Search for art pieces based on a query."""
    global df
    query = request.args.get("query", "").lower()

    # Search the DataFrame for the query in any column
    results = df[df.apply(lambda row: query in row.to_string().lower(), axis=1)]

    if results.empty:
        return jsonify({"message": "No art pieces match your search"}), 404

    return jsonify(results.to_dict(orient="records")), 200


# Route to remove an item from the cart by its ID
@art_bp.route("/cart/<int:art_id>", methods=["DELETE"])
def delete_from_cart(art_id):
    """Delete an item from the cart by its ID."""
    global cart

    # Validate art_id
    if art_id < 0 or art_id >= len(cart):
        return jsonify({"error": "Item not found in cart"}), 404

    # Remove the item from the cart
    removed_item = cart.pop(art_id)
    return jsonify({"message": "Item removed from cart", "removed": removed_item}), 200


# Route to fetch all art pieces by a specific author
@art_bp.route("/author/<string:author_name>", methods=["GET"])
def get_pieces_by_author(author_name):
    """Fetch all art pieces by a specific author."""
    global df

    # Filter art pieces by the author's name (case-insensitive)
    results = df[df["Author"].str.contains(author_name, case=False, na=False)]

    if results.empty:
        return jsonify({"message": f"No art pieces found for author: {author_name}"}), 404

    return jsonify(results.to_dict(orient="records")), 200
