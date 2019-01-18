from flask_admin.contrib.sqla import ModelView

class UserView(ModelView):
	can_view_details = True
