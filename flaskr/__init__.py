import os

from flask import Flask, url_for

from . import employment
from . import education
from . import projects

def create_app(test_config = None):
	# Create a new flask instance, passing in the name of the application and options
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register page routes/blueprints
    app.register_blueprint(employment.bp)
    app.register_blueprint(education.bp)
    app.register_blueprint(projects.bp)

    return app
