# Day 40 – Student Management REST API

## Project Introduction

This project demonstrates a Student Management REST API built with FastAPI. The application provides endpoints to perform CRUD operations (Create, Read, Update, Delete) on student records. The API includes automatic data validation using Pydantic, comprehensive error handling, and interactive API documentation using Swagger UI.

# Technologies Used

* Python
* FastAPI
* Uvicorn
* Pydantic
* Starlette
* Swagger/OpenAPI

# Folder Structure

```text
Day-40/

├── app/
│   ├── main.py
│   ├── routes/
│   │   └── students.py
│   └── schemas/
│       └── student.py
│
├── requirements.txt
├── README.md
└── Deployment Info.txt
```

# Features

The API provides the following functionality:

* **GET /** — Welcome message endpoint
* **GET /health** — Health check endpoint
* **GET /students** — Retrieve all students
* **POST /students** — Add a new student
* **GET /students/{id}** — Get a specific student by ID
* **PUT /students/{id}** — Update student information
* **DELETE /students/{id}** — Delete a student
* **Automatic Data Validation** — Using Pydantic models
* **Error Handling** — Proper HTTP status codes and error messages
* **Interactive Documentation** — Built-in Swagger UI at `/docs`

# What is a REST API?

A REST (Representational State Transfer) API is a way for different applications to communicate over the internet using standard HTTP methods. Each endpoint represents a resource, and HTTP methods define what action to perform on that resource.

REST APIs are commonly used for:
* Mobile app backends
* Web application servers
* Microservices
* Third-party integrations
* Real-time data services
* IoT applications
* Social media platforms

# Difference Between GET and POST

### GET Request

* Used to **retrieve data** from the server.
* No request body required.
* Data passed through URL parameters.
* Visible in browser history and URL bar.
* Safe and cacheable.
* Suitable for reading data only.

Example:

GET /students/1
→ Retrieves student with ID 1


### POST Request

* Used to **send data** to the server to create new resources.
* Requires a request body with JSON data.
* Data is not visible in the URL.
* Not cached by default.
* Used for creating new records.
* Suitable for sending sensitive data.

Example:
POST /students
Body: {
"name": "Ahmed",
"age": 20,
"program": "BSCS"
}
→ Creates a new student record

# What is Pydantic?

Pydantic is a Python library that validates data automatically before it reaches your application logic.

**Benefits:**
* Automatic type checking
* Data validation (minimum/maximum values, string length, etc.)
* Clear error messages for invalid data
* Converts incoming JSON to Python objects
* Documents expected data format
* Prevents invalid data from being stored

**Example Validation in This Project:**
```python
class Student(BaseModel):
    name: str = Field(min_length=2)      # Name must be at least 2 characters
    age: int = Field(gt=0, lt=100)       # Age must be between 0 and 100
    program: str = Field(min_length=2)   # Program must be at least 2 characters
```

If someone tries to add a student with invalid data (age=150), Pydantic automatically rejects it with a clear error message.

# API Architecture

This project follows a clean, modular architecture:

**app/main.py**
* Initializes FastAPI application
* Includes routers from other modules
* Defines root and health check endpoints

**app/routes/students.py**
* Contains all student-related endpoints
* Implements CRUD operations
* Handles error cases with proper HTTP status codes

**app/schemas/student.py**
* Defines Pydantic model for student data
* Specifies validation rules
* Documents expected data format

# Coding Practice

Separate files were created to follow best practices and maintain clean code structure.

### app/main.py

* Initialize FastAPI application with metadata
* Define root endpoint (`GET /`)
* Define health check endpoint (`GET /health`)
* Include student routes using APIRouter

### app/routes/students.py

* `GET /students` — Retrieve all student records
* `POST /students` — Add a new student with automatic validation
* `GET /students/{student_id}` — Get specific student by ID
* `PUT /students/{student_id}` — Update existing student
* `DELETE /students/{student_id}` — Remove student from system

### app/schemas/student.py

* Define Student Pydantic model
* Specify validation rules for each field
* Ensure data consistency across all endpoints

# Mini Project

## Student Management REST API

The complete API includes:

* Add students with automatic validation
* View all students
* Search for specific students
* Update student information
* Delete students
* Comprehensive error handling
* Interactive Swagger UI for testing
* Clear error messages for invalid requests

# API Requests and Responses

### Example 1: Add a New Student

**Request:**
POST /students
Content-Type: application/json

{
"name": "Zainab",
"age": 20,
"program": "BSCS"
}

**Response (201 Created):**
```json
{
  "id": 3,
  "name": "Zainab",
  "age": 20,
  "program": "BSCS"
}
```

### Example 2: Get All Students

**Request:**
GET /students

**Response (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Ali",
    "age": 21,
    "program": "BSCS"
  },
  {
    "id": 2,
    "name": "Sara",
    "age": 22,
    "program": "BSCS"
  },
  {
    "id": 3,
    "name": "Zainab",
    "age": 20,
    "program": "BSCS"
  }
]
```

### Example 3: Update a Student

**Request:**
PUT /students/1
Content-Type: application/json

{
"name": "Ali Updated",
"age": 22,
"program": "BSEE"
}

**Response (200 OK):**
```json
{
  "id": 1,
  "name": "Ali Updated",
  "age": 22,
  "program": "BSEE"
}
```

### Example 4: Delete a Student

**Request:**
DELETE /students/2

**Response (200 OK):**
```json
{
  "message": "Student deleted successfully",
  "student": {
    "id": 2,
    "name": "Sara",
    "age": 22,
    "program": "BSCS"
  }
}
```

### Example 5: Invalid Data (Validation Error)

**Request:**
POST /students
Content-Type: application/json

{
"name": "A",
"age": 150,
"program": "X"
}

**Response (422 Unprocessable Entity):**
```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "ensure this value has at least 2 characters",
      "type": "value_error.string.too_short"
    },
    {
      "loc": ["body", "age"],
      "msg": "ensure this value is less than 100",
      "type": "value_error.number.not_lt"
    }
  ]
}
```

# Testing the API

The API can be tested using:

* **Swagger UI** — `http://localhost:8000/docs` (Interactive and recommended)
* **Thunder Client** — VS Code extension for API testing
* **Postman** — Desktop application for API testing
* **cURL** — Command-line tool for HTTP requests

# Challenges Faced

During this project, I faced several challenges:

* Understanding REST API principles and HTTP methods
* Structuring the project with proper separation of concerns
* Implementing data validation using Pydantic models
* Handling different HTTP status codes and error scenarios
* Managing application state with in-memory data storage
* Testing all endpoints systematically

# What I Learned

After completing this project, I learned:

* How REST APIs work and why they are important
* Difference between GET, POST, PUT, and DELETE methods
* Using FastAPI for rapid API development
* Data validation using Pydantic models
* Proper error handling and HTTP status codes
* Building a clean, modular project structure
* Testing APIs using Swagger UI and Thunder Client
* Organizing code into separate files following best practices

# Deployment

The API has been successfully deployed to **Render** (free platform):

* **Deployment Platform:** Render
* **Live API URL:** `https://student-api-xxxxx.onrender.com`
* **Swagger Documentation:** `https://student-api-xxxxx.onrender.com/docs`
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 8080`

# Possible Improvements

In future versions, I would like to add:

* Database integration (PostgreSQL or MongoDB) instead of in-memory storage
* User authentication and authorization
* Student enrollment tracking
* Course management
* Grade tracking system
* Bulk import/export functionality
* Advanced filtering and search
* API rate limiting
* Caching for improved performance
* Comprehensive logging
* Unit and integration tests
* Docker containerization
* CI/CD pipeline
