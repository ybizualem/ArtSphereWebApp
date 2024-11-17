import pandas as pd
from app import db
from app.model.art_model import ArtPiece

def import_csv_to_db(csv_file):
    df = pd.read_csv(csv_file)
    for _, row in df.iterrows():
        art_piece = ArtPiece(
            name=row['name'],
            artist=row['artist'],
            medium=row['medium'],
        )
        db.session.add(art_piece)
    db.session.commit()
    print(f"Imported {len(df)} art pieces.")
