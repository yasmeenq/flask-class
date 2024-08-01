from logic.auth_logic import AuthLogic
from flask import request, session 
from models.user_model import UserModel
from models.role_model import RoleModel
from models.client_error import * 
from models.credential_model import * 
from utils.cyber import Cyber 

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
        if error: raise ValidationError("register error....", user)
        if self.logic.is_email_taken(email): raise ValidationError("email already exists", user) # user for refresh 
        user.password = Cyber.hash(user.password)
        self.logic.add_user(user)



    def login(self):
        email = request.form.get("email")
        password = request.form.get("password")
        credentials = CredentialModel(email, Cyber.hash(password)) # dont forget to make hash 
        error = credentials.validate()
        if error : raise ValidationError(error, credentials)
        user = self.logic.get_user(credentials)
        if not user : raise AuthError("Incorrect email or password", user)
        del user["password"] # delete from session dictionary password key 
        session["current_user"] = user 

    # block guest - users that didnt make logo in 
    def block_anonymous(self): 
        user = session.get("current_user")
        if not user : raise AuthError("you are not logged in")

    # block guest or users that doesnt have admin permission 
    def block_non_admin(self):
        user = session.get("current_user")
        if not user : raise AuthError("you are not logged in")
        if user["role_id"] != RoleModel.Admin.value: raise AuthError("you are not allowed")
         
    def close(self):
        self.logic.close() 

    def logout(self):
        session.clear()
