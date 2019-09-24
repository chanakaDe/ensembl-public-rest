from flask import request
from flask_restful import Resource
from Model import db, Gene, GeneSchema

genes_schema = GeneSchema(many=True)

class GeneResource(Resource):
    def get(self,query,species,limit):
        genes = Gene.query.filter(Gene.display_label.like("%"+ query + "%"),Gene.species == species).limit(limit).all()
        genes = genes_schema.dump(genes).data
        if not genes:
            return {'status': 'error', 'data': "Unable to find given object"}, 400
        else:
            return {'status': 'success', 'data': genes}, 200
        
