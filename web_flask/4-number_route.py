#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the text
        variable (replace underscore _ symbols with a space )
            The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text: str):
    """display “C ” followed by the value of the text variable"""
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_route(text: str):
    """display “Python ”, followed by the value of the text"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<n>", strict_slashes=False)
def number_route(n):
    """display “n is a number” only if n is an integer"""
    try:
        number_float = float(n)
        if number_float.is_integer():
            return f"{int(number_float)} is a number"
        abort(404)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
