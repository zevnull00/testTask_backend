# app/api/routes.py

from flask import jsonify
from ..models import GrossViolation
from ..schemas import ObjectGVSchema
from . import api_bp

@api_bp.route('/gross_violations/<int:violation_uid>/objects_gv')
def get_violation_objects(violation_uid):
    violation = GrossViolation.query.get(violation_uid)
    if violation:
        schema = ObjectGVSchema(many=True)
        return jsonify(schema.dump(violation.objects))
    else:
        # думаю, что 404 возвращать не стоит
        return jsonify([])
