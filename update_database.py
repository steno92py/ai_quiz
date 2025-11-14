"""Script to update the database schema by adding the record_date column.

Run this script once to add the new column to existing databases.
"""

from app import create_app
from app.extensions import db
from config import DevConfig


def update_database():
    """Add record_date column to users table if it doesn't exist."""

    app = create_app(DevConfig)

    with app.app_context():
        # Check if we need to add the column
        from sqlalchemy import inspect, text

        inspector = inspect(db.engine)
        columns = [col['name'] for col in inspector.get_columns('users')]

        if 'record_date' not in columns:
            print("Aggiunta colonna 'record_date' alla tabella users...")

            # Add the column using raw SQL
            with db.engine.connect() as conn:
                conn.execute(text('ALTER TABLE users ADD COLUMN record_date DATETIME'))
                conn.commit()

            print("Colonna aggiunta con successo!")
        else:
            print("La colonna 'record_date' esiste già nel database.")


if __name__ == '__main__':
    update_database()
