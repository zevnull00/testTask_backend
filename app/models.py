# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class GrossViolation(db.Model):
    __tablename__ = 'gross_violation'
    __table_args__ = {'schema': 'ob'}

    uid = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    oshs_inspection_uid = db.Column(db.Integer)
    report_uid = db.Column(db.Integer)
    is_threat = db.Column(db.Boolean)
    is_csho_notified = db.Column(db.Boolean)
    investigation_result = db.Column(db.String)
    number = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    note = db.Column(db.String)
    is_incident = db.Column(db.Boolean)
    gross_violation_section_uid = db.Column(db.Integer, nullable=False)

    object_gv = db.relationship('ObjectGv', secondary='ob.gross_violation_x_object', backref='gross_violations')



t_gross_violation_x_object = db.Table(
    'gross_violation_x_object',
    db.Column('gross_violation_uid', db.ForeignKey('ob.gross_violation.uid', ondelete='CASCADE'), primary_key=True, nullable=False),
    db.Column('object_gv_uid', db.ForeignKey('ob.object_gv.uid', ondelete='CASCADE'), primary_key=True, nullable=False),
    schema='ob'
)



class ObjectGv(db.Model):
    __tablename__ = 'object_gv'
    __table_args__ = {'schema': 'ob'}

    uid = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    object = db.Column(db.String, nullable=False)
