from app import db

class UserRegister3(db.Model):
    """記錄使用者資料的資料表"""
    __tablename__ = 'UserRegisters3'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)

db.create_all()
