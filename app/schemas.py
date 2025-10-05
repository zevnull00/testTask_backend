# app/schemas.py

from marshmallow_sqlalchemy import ModelSchema
from .models import ObjectGv, GrossViolation, db


class ObjectGVSchema(ModelSchema):
    class Meta:
        model = ObjectGv
        sqla_session = db.session
        load_instance = True

class ObjectGVSchema_easy(ModelSchema):
    class Meta:
        model = ObjectGv
        sqla_session = db.session
        load_instance = True

# а вот тут немного не уверен
# в приципе, хорошо, что выдаются полные данные по объекту
# но, возможно, их надо урезать?
# хз, мб TODO
class GrossViolationSchema(ModelSchema):
    class Meta:
        model = GrossViolation
        sqla_session = db.session
        load_instance = True

