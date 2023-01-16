#!/usr/bin/python3
"""
The 6-number_odd_or_even module
Starts a Flask web application
"""
from flask import Flask, escape, request, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Return: a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """
        Return: a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        Return: a string followed by the value of the text variable
    """
    return ('C {}'.format(text).replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
        Return: a string followed by the value of the text variable
        with its default value as "is cool"
    """
    return ('Python {}'.format(text).replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    ""
        Return: 'n is a number' only if n is an integer
    """
    return ("{} is a number".format(n))



@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
    """ Displays a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False
def n_odd_or_even(n):
    """ Displays a HTML page only if n is an integer

    """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, t="even")
    else:
        return render_template('6-number_odd_or_even.html', n=n, t="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
