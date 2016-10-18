"""
GrowShare

(c) Annie Fraysse, 2016

"""

import os
import csv
import json

from jinja2 import StrictUndefined 

from flask import Flask, render_template, flash, redirect, request, jsonify, url_for, session
from flask_debugtoolbar import DebugToolbarExtension 

# creates a flask app
app = Flask(__name__)

# requirement for flask session and debug toolbar
app.secret_key = "BCA"

# raise error in jinja if undefined 
app.jinja_env.undefined = StrictUndefined

####################################################

@app.route('/', methods=['GET'])
def index():
    """ Homepage with login/registration. """

    return render_template("main.html")



################################################################################################


if __name__ == "__main__":
    app.debug = True
    DebugToolbarExtension(app)

    app.run()


