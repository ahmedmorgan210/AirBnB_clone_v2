#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask
""" the flask """

app = Flask(__name__, strict_slashes=False)

@app.route('/')
def hello():
    """rout to hello"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
