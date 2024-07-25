from logic.auth_logic import AuthLogic
from flask import request
from models.user_model import UserModel
from models.role_model import RoleModel
from models.client_error import * 
class AuthFacade:
    def __init__(self):
        self.logic = AuthLogic() 


    def register(self):
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = UserModel(None, first_name, last_name, email, password, RoleModel.User.value)
        error = user.validate_insert()
        if error: raise ValidationError("register error....")
        if self.logic.is_email_taken(email): raise ValidationError("email already exists") # user for refresh 
        self.logic.add_user(user)






def close(self):
    self.logic.close() 
