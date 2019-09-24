from flask import Blueprint
from flask_restful import Api
from resources.Gene import GeneResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(GeneResource, '/gene_suggest/<string:query>/<string:species>/<int:limit>')