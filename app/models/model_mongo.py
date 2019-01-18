from app import db2

class Inspection_Method(db2.Document):
    __tablename__ = 'inspection_method'
    english_name = db2.StringField(required=True, unique=True)
    chinese_name = db2.StringField(required=True, unique=True)

