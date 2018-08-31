# Context Application Support/Developer exercise

This repository contains a basic application where only admin users can upload files; users in the user group cannot.

Setup instructions
===
1. Copy the project
2. Install python 2.7.9 or newer
3. Set up the python virtual environment with:
```
    pip install virtualenv
    cd qa-support-interview-master
    virtualenv venv
    source venv/bin/activate #for linux
    .\venv\Scripts\activate #for windows
```
4. Install the required packages:
```
    pip install -r requirements.txt
```
5. Setup the database:
```
    python manage.py migrate
    python manage.py setup
```
6. Run the application with:
```
    python manage.py runserver
```
7. View the application at http://127.0.0.1:8000

The two users available are:

    admin:password
    user:password
    
There are two issues with this application:
* PDF files cannot be uploaded
* Only admins should have permission to upload files, but this is not the case

Task
===
1. Produce a bug report for each of these isues.
2. Provide a fix that fixes each issue
