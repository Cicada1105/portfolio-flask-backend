from flask import Blueprint

import json

# Blueprint(name of blueprint, location, url_prefix)
bp = Blueprint('employment', __name__, url_prefix = '/employment')

@bp.route("/list-all", methods=['GET'])
def list_all():
	f = open('flaskr/employment/employment.json','r')
	data = json.load(f)
	f.close()
	
	return data