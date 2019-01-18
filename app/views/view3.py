from flask_admin.contrib.sqla import ModelView

class UserView3(ModelView):
	can_view_details = True
