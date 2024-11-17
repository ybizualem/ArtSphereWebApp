from app import create_app  # Import the application factory function
from app.services.data_importer import import_csv_to_db
import os

# Path to your CSV file
csv_file = '/Users/yeabsirabizualem/Documents/f24(Jun1)/CSPS415_AI/ArtSphereBackendTrial/testArt(Sheet1).csv'

# Ensure the database exists before importing data
if not os.path.exists('instance/art.db'):  # Adjust to match your database path
    print("Database not found. Importing data...")
    import_csv_to_db(csv_file)  # Import CSV data into the database

# Create the Flask application instance
app = create_app()

# Run the application
if __name__ == "__main__":
    app.run(debug=True)  # Use debug=True for easier debugging during development
