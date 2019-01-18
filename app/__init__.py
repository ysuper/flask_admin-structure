from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from app.views import *
from app.models import *

@app.route('/')
def index():
    return '<a href="/admin/">Click me to get to Admin!</a>'

# Create admin
admin = Admin(app, name='ysuper測試', template_mode='bootstrap3')

# Add views
admin.add_view(view.UserView(model.UserRegister, db.session, name='測試表'))  
admin.add_view(view2.UserView2(model2.UserRegister2, db.session, name='測試表2'))  
admin.add_view(view3.UserView3(model3.UserRegister3, db.session, name='測試表3'))  

