# CLIPBOARD

Multi clipboard which copies any number of text, keeps them in stack so you can use any of them at anytime quickly.

## Dependencies
1. keyboard
2. xerox
3. psycopg2
4. flask
5. flask_cors

## Installation
Install dependencies using `pip install dependency-name`. 

Db connectivity is needed to save copied texts. Database used is postgreSQL. Change DB connection in clipboard.py and clipboard_server.py 

## Steps to start the application

#### 1. Run clipboard.py to listen to copy commands
> python3 clipboard.py

#### 2. Run clipboard_server.py to start the REST server
> python3 clipboard_server.py

#### 3. Open web/index.hmtl to view the clipboard
> clicking on the text content automatically copies the text
