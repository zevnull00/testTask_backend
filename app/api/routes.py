# app/api/routes.py

from flask import jsonify
from ..models import GrossViolation
from ..schemas import ObjectGVSchema
from . import api_bp
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import joinedload

@event.listens_for(Engine, "before_cursor_execute")
def receive_before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    print(">>> SQL:", statement)

@api_bp.route('/gross_violations/<int:violation_uid>/objects_gv')
def get_violation_objects(violation_uid):
    violation = GrossViolation.query.options(
        joinedload(GrossViolation.object_gv)
    ).filter(GrossViolation.uid == violation_uid).first()
    if violation:
        schema = ObjectGVSchema(many=True, only=('uid', 'object'))
        res =  jsonify(schema.dump(violation.object_gv))
        # сюда включен также случай, что список объектов пуст
    else:
        res = jsonify({"error" : 'There is no such thing as GrossViolation.'}), 400
    return res
