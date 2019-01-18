from flask import Flask, redirect
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
db2 = MongoEngine(app)

#from .api.inspection__method import get_INSPECTION__METHOD_all
from app.api import *
from app.views import *
from app.models import *

@app.route('/')
def index():
    return redirect('/admin')

# Create admin
admin = Admin(app, name='ysuper測試', template_mode='bootstrap3')

# Add views
admin.add_view(view.UserView(model.UserRegister, db.session, name='測試表'))  
admin.add_view(view2.UserView2(model2.UserRegister2, db.session, name='測試表2'))  
admin.add_view(view3.UserView3(model3.UserRegister3, db.session, name='測試表3'))  
admin.add_view(view_mongo.Inspection_Method_View(model_mongo.Inspection_Method, name='檢驗工具'))  
