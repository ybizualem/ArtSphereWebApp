from app import create_app  # Import the application factory function

# Create the Flask application instance
app = create_app()

# Run the application
if __name__ == "__main__":
    app.run(debug=True)  # Use debug=True for easier debugging during development
