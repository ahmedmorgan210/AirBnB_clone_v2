#!/usr/bin/python3
"""
A simple Flask web application demonstrating a basic route.

This module starts a Flask web server that listens on host 0.0.0.0 and port 5000.
It defines a single route ('/') which returns the string "Hello HBNB!" when accessed.
"""

import os
from flask import Flask

class Application:
    """
    A class to encapsulate the Flask application setup and routing.

    Attributes:
        app (Flask): The Flask web application instance.
    """

    def __init__(self):
        """
        Initializes the Flask application.

        This constructor sets up the Flask application with the name of the current module
        as the secret key and disables URL rule enforcement of slashes.
        """
        self.app = Flask(__name__, strict_slashes=False)

    def run(self):
        """
        Runs the Flask application.

        This method starts the Flask development server with the specified host and port.
        """
        self.app.run(host='0.0.0.0', port=os.getenv('PORT', 5000))

    def add_route(self, route, view_func):
        """
        Adds a new route to the Flask application.

        Args:
            route (str): The URL route.
            view_func (function): The view function to execute when the route is accessed.
        """
        self.app.add_url_rule(route, view_func=view_func)


if __name__ == '__main__':
    app = Application()
    app.add_route('/', lambda: "Hello HBNB!")
    app.run()
