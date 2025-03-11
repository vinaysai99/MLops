# Flask Notes

## **WSGI (Web Server Gateway Interface)**
WSGI (pronounced "Whiskey") is a specification that defines how web servers communicate with Python web applications. It allows Python applications to be served by web servers like Gunicorn, uWSGI, or Apache.

### **How WSGI Works:**
1. A client sends an HTTP request to the web server (e.g., Nginx, Apache).
2. The web server forwards the request to a WSGI-compatible application.
3. The application processes the request and generates a response.
4. The response is sent back to the web server and then to the client.

### **Example of a WSGI Application in Flask:**
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, WSGI!"

if __name__ == "__main__":
    app.run()
```
If deployed with Gunicorn:
```sh
gunicorn -w 4 app:app
```
This runs the application with four worker processes.

---

## **Jinja2 (Templating Engine for Flask)**
Jinja2 is a powerful templating engine used in Flask to dynamically generate HTML pages by embedding Python-like expressions.

### **Features of Jinja2:**
- **Variables:** Use `{{ variable }}` to insert values dynamically.
- **Control Structures:** Supports loops (`for`) and conditionals (`if`).
- **Filters:** Modify data output (`{{ name|upper }}` converts text to uppercase).
- **Template Inheritance:** Define a base template and extend it in other pages.

### **Example of Jinja2 in a Flask App:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="John Doe")

if __name__ == "__main__":
    app.run()
```

### **Example of Jinja2 Template (`templates/index.html`):**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Jinja2 Example</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    {% if name == "John Doe" %}
        <p>You are our guest user.</p>
    {% else %}
        <p>Hello, {{ name }}!</p>
    {% endif %}
</body>
</html>
```

---

## **HTTP Methods: GET, POST, PUT, DELETE**
HTTP methods define the type of request a client sends to a server.

### **1️⃣ GET (Retrieve Data)**
- Used to fetch data from a server.
- No request body, parameters are sent via URL.
- Safe and idempotent (does not change server state).
#### **Example:**
```python
@app.route('/user/<name>', methods=['GET'])
def get_user(name):
    return f"User: {name}"
```
#### **Request Example:**
```sh
GET /user/John
```

---

### **2️⃣ POST (Create Data)**
- Used to send data to the server to create a new resource.
- Data is sent in the request body.
- Not idempotent (can create duplicate entries if repeated).
#### **Example:**
```python
@app.route('/add-user', methods=['POST'])
def add_user():
    data = request.json  # Expecting JSON data
    return {"message": f"User {data['name']} added successfully!"}, 201
```
#### **Request Example (Using cURL):**
```sh
curl -X POST http://127.0.0.1:5000/add-user -H "Content-Type: application/json" -d '{"name": "Alice"}'
```

---

### **3️⃣ PUT (Update Data)**
- Used to update an existing resource.
- Sends data in the request body.
- Idempotent (multiple identical requests produce the same result).
#### **Example:**
```python
@app.route('/update-user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    return {"message": f"User {id} updated with name {data['name']}"}
```
#### **Request Example:**
```sh
curl -X PUT http://127.0.0.1:5000/update-user/1 -H "Content-Type: application/json" -d '{"name": "Bob"}'
```

---

### **4️⃣ DELETE (Remove Data)**
- Used to delete a resource.
- Idempotent (deleting the same resource multiple times gives the same response).
#### **Example:**
```python
@app.route('/delete-user/<int:id>', methods=['DELETE'])
def delete_user(id):
    return {"message": f"User {id} deleted!"}
```
#### **Request Example:**
```sh
curl -X DELETE http://127.0.0.1:5000/delete-user/1
```

---

## **Summary Table**
| Method  | Purpose          | Idempotent? | Example |
|---------|----------------|-------------|---------|
| **GET**    | Retrieve data  | ✅ Yes | `/user/John` |
| **POST**   | Create data    | ❌ No  | `POST /add-user` |
| **PUT**    | Update data    | ✅ Yes | `PUT /update-user/1` |
| **DELETE** | Remove data    | ✅ Yes | `DELETE /delete-user/1` |

---

## **Final Thoughts**
- **WSGI** allows Flask applications to interact with web servers.
- **Jinja2** enables dynamic HTML rendering with Python-like syntax.
- **HTTP Methods (GET, POST, PUT, DELETE)** define how clients interact with APIs.

