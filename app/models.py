# app/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Ассоциативная таблица
# создается в виде таблицы, а не модели, так как не содержит ничего, кроме связей
gv_x_object = db.Table(
    'gross_violation_x_object',
    db.Column('gross_violation_uid', db.Integer, db.ForeignKey('ob.gross_violation.uid')),
    db.Column('object_gv_uid', db.Integer, db.ForeignKey('ob.object_gv.uid')),
    schema='ob'
)

class ObjectGV(db.Model):
    __tablename__ = 'object_gv'
    __table_args__ = {'schema': 'ob'}

    uid = db.Column(db.Integer, primary_key=True)
    object_name = db.Column('object', db.String(255), nullable=False)

class GrossViolation(db.Model):
    __tablename__ = 'gross_violation'
    __table_args__ = {'schema': 'ob'}

    uid = db.Column(db.Integer, primary_key=True)
    oshs_inspection_uid = db.Column(db.Integer)
    report_uid = db.Column(db.Integer)
    is_threat = db.Column(db.Boolean)
    is_csho_notified = db.Column(db.Boolean)
    number = db.Column(db.String(255))
    description = db.Column(db.String(255))
    note = db.Column(db.String(255))
    is_incident = db.Column(db.Boolean)
    gross_violation_section_uid = db.Column(db.Integer)

# Отношения
ObjectGV.violations = db.relationship('GrossViolation', secondary=gv_x_object, back_populates='objects')
GrossViolation.objects = db.relationship('ObjectGV', secondary=gv_x_object, back_populates='violations')