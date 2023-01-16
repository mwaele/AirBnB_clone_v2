#!/usr/bin/python3
"""
The 0-hello_route module
"""
from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Starts a Flask web application
        Return: a string
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
