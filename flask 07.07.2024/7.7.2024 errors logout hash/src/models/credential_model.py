from email_validator import validate_email 

class CredentialModel:
    def __init__(self, email, password):
        
        self.email = email 
        self.password = password 


    def validate(self):
        if not self.email:return "email"
        if not self.password:return "password"
        if not validate_email(self.email): return "not validate not correct"
        return None


