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

1. Clone the repository.
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
│── authentication/
│── requirements.txt
│── README.md
```
Each folder contains a different Flask concept or project.

## Topics Covered
- Flask setup and environment
- Routing and URL parameters
- Template rendering (Jinja2)
- Forms and user input handling
- Database integration with SQLite and SQLAlchemy
- Authentication and authorization
- API development with Flask
- Deployment strategies

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
