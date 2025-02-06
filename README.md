# Keep Notes App (Django)  

A simple note-taking app with user authentication, CRUD operations, and password reset functionality.  

## Features  
- User authentication (Sign Up, Login, Logout)  
- Password reset via email  
- CRUD operations for personal notes  
- User-specific access (each user sees only their notes)  

## Deployment  
The app is deployed on **Render**. You can access it [here](https://keep-notes-f4xt.onrender.com/notes).  

## Installation (For Local Setup)  
1. Clone the repository:  
   git clone https://github.com/rupeshg27/Keep_Notes
   cd keep_notes
   
2. Install dependencies:
    pip install -r requirements.txt

3. Apply migrations:
    python manage.py migrate

4. Create a superuser:
    python manage.py createsuperuser

5. Run the server:
    python manage.py runserver

6. Open http://127.0.0.1:8000/notes/

Usage:
    New users: Register and log in.
    Existing users: Log in to access their notes.
    Forgot password: Reset via email.
    Create, edit, delete personal notes.

Tech Stack:
    Backend: Django, SQLite
    Authentication: Django's built-in auth system
    Deployment: Render



