#!/usr/bin/python3

"""
app module
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:%password%@localhost/Akiwacu"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


"""
@app.route('/')
def index():
    return 'Hello, World!'
"""

if __name__ == '__main__':
    app.run(debug=True)

