from service.LoginService import LoginService
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

class LoginController:
    def __init__(self):
        self.service = LoginService()

    # call the login function in LoginService
    def login(self, username, password):
        if self.service.authenticate(username, password):
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Login failed. Invalid credentials.")
            return False

    # call the register function in LoginService check whether username is existed or not
    def register(self, username, password):
        if self.service.register(username, password):
            print("Registration successful.")
        else:
            print("Username already exists.")