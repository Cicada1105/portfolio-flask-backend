from flask import Blueprint

import json

# Blueprint(name of blueprint, location, url_prefix)
bp = Blueprint('projects', __name__, url_prefix = '/projects')

@bp.route("/list-all", methods=['GET'])
def list_all():
	f = open('flaskr/projects/projects.json','r')
	data = json.load(f)
	f.close()

	return data