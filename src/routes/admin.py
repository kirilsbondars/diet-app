from flask import Blueprint
from src.controllers.admin import admin_panel, delete_user, user_details, add_meal, edit_meal, delete_meal
from flask_login import login_required

admin_blueprint = Blueprint('admin', __name__)

admin_blueprint.route('/admin', methods=['GET'])(login_required(admin_panel))
admin_blueprint.route('/delete-user/<int:user_id>', methods=['POST'])(login_required(delete_user))
admin_blueprint.route('/user-details/<int:user_id>', methods=['GET'])(login_required(user_details))

admin_blueprint.route('/add-meal', methods=['GET', 'POST'])(login_required(add_meal))
admin_blueprint.route('/edit-meal/<int:meal_id>', methods=['GET', 'POST'])(login_required(edit_meal))
admin_blueprint.route('/delete-meal/<int:meal_id>', methods=['POST'])(login_required(delete_meal))
