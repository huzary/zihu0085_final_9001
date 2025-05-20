import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

# Here is the entity of user, we can set users' name account, pet's information here.
class User:
    def __init__(self, username, password, pet=None):
        self.username = username
        self.password = password
        self.pet = pet

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_pet(self):
        return self.pet
    
    def set_username(self,name):
        self.username=name
    
    def set_password(self,password):
        self.password=password

    def set_pet(self,pet):
        self.pet=pet
    