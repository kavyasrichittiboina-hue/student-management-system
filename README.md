# Student Registration Website

## Description

Student Registration Website is a Flask-based web application that allows users to register student details, view all registered students, update student information, and delete records. The application uses SQLite for data storage and provides complete CRUD (Create, Read, Update, Delete) functionality.

## Features

* Student Registration Form
* Store Student Information in SQLite Database
* View All Registered Students
* Update Student Details
* Delete Student Records
* About Page
* Contact Page
* Flask Routing
* Database Integration

## Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS

## Website Pages

### Home Page

Students can enter:

* Name
* Age
* Email
* Password

### Students Page

Displays all registered students stored in the database.

### Update Page

Allows modification of student details.

### Delete Page

Allows deletion of student records.

### About Page

Provides information about the website.

### Contact Page

Displays contact information.

## Database

The project automatically creates:

### studentregistration Table

| Column   | Type    |
| -------- | ------- |
| id       | Integer |
| name     | Text    |
| age      | Integer |
| email    | Text    |
| password | Text    |

## Project Structure

```text
student-registration-website/
│
├── app.py
├── studentregistration.db
│
├── templates/
│   ├── home.html
│   ├── students.html
│   ├── update.html
│   ├── delete.html
│   ├── about.html
│   └── contact.html
│
└── static/
    └── style.css
```

## How to Run

1. Install Flask

```bash
pip install flask
```

2. Run the application

```bash
python app.py
```

3. Open your browser

```text
http://127.0.0.1:5000
```

## Learning Outcomes

* Flask Routing
* Form Handling
* SQLite Database Operations
* CRUD Operations
* Dynamic HTML Rendering
* Web Application Development

## Author

Kavya Sri
