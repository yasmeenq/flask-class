from enum import Enum

class StatusCode(Enum):
    OK = 200
    BadRequest = 400
    Unautherized = 401 
    NotFound = 404 
    InternalServerError = 500 



#print(RoleModel.Admin.value) # 1 
#print(RoleModel.Admin.name) # Admin 