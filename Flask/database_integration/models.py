from app import db  # Import database instance from app

# Define a User model with an ID and Name field
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing primary key
    name = db.Column(db.String(80), nullable=False)  # Name field (cannot be null)
