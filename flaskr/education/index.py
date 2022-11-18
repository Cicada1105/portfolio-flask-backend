from flask import Blueprint, Response

import json

# Blueprint(name of blueprint, location, url_prefix)
bp = Blueprint('education', __name__, url_prefix = '/education')

@bp.route("/list-all", methods=['GET'])
def list_all():
	f = open('flaskr/education/institutions.json','r')
	data = json.load(f)
	f.close()
	
	return data