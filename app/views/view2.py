from flask_admin.contrib.sqla import ModelView

class UserView2(ModelView):
	can_view_details = True
