from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy instance
db = SQLAlchemy(app)

# Import models to avoid circular import issues
from models import User

# Home route - Displays all users from the database
@app.route('/')
def index():
    users = User.query.all()  # Fetch all users from the database
    return render_template('index.html', users=users)

# Route to add a new user
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']  # Get name from form input
    new_user = User(name=name)   # Create a new User object
    db.session.add(new_user)     # Add new user to database
    db.session.commit()          # Commit changes
    return redirect(url_for('index'))  # Redirect to home page

# Run the Flask app
if __name__ == "__main__":
    db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)  # Run in debug mode for easy development
