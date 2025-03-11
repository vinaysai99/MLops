# Flask Learning Repository

Welcome to my Flask learning repository! This repository contains my notes, projects, and experiments as I learn Flask, a micro web framework for Python.

## Table of Contents
- [About](#about)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Topics Covered](#topics-covered)
- [Usage](#usage)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## About
This repository serves as a personal learning space where I explore Flask, covering topics such as routing, templates, database integration, authentication, and more.

## Installation
To run any of the Flask projects in this repository, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/flask-learning.git
   cd flask-learning
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Project Structure
```
flask-learning/
│── basic-app/
│── templates/
│── static/
│── database-integration/
│── requirements.txt
│── README.md
```
Each folder contains a different Flask concept or project.

## Topics Covered
### Flask Setup and Environment
- Install Flask using `pip install flask`
- Set up a virtual environment for better dependency management
- Use `FLASK_APP` and `FLASK_ENV` variables to configure the environment

### Routing and URL Parameters
- Define routes using `@app.route('/')`
- Use dynamic URL parameters like `@app.route('/user/<name>')`
- Handle HTTP methods (`GET`, `POST`, etc.)

### Template Rendering (Jinja2)
- Use Jinja2 templates to separate HTML from Python logic
- Pass variables from Flask to templates using `render_template()`
- Use template inheritance to reuse layout components

### Forms and User Input Handling
- Handle form data using `request.form`
- Validate input with Flask-WTF and CSRF protection
- Use `redirect()` and `url_for()` for better user flow

### Database Integration with SQLite and SQLAlchemy
- Use SQLite for lightweight applications
- Integrate SQLAlchemy ORM for database management
- Perform CRUD operations with Flask-SQLAlchemy

### API Development with Flask
- Create RESTful APIs using Flask-RESTful
- Return JSON responses with `jsonify()`
- Use `Flask-CORS` to handle cross-origin requests

### Deployment Strategies
- Deploy Flask apps to Heroku, AWS, or Docker
- Use Gunicorn for production servers
- Configure environment variables for security

## Usage
Navigate to a project folder and run:
```sh
flask run
```
Make sure you have set the required environment variables, such as:
```sh
export FLASK_APP=app.py
export FLASK_ENV=development
```

## Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Jinja Templating](https://jinja.palletsprojects.com/)

## Contributing
Feel free to fork the repository, open issues, or submit pull requests.

## License
This project is licensed under the MIT License.
