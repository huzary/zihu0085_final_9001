from service.UserService import UserService
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

class UserController:
    def __init__(self):
        self.service = UserService()

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

    def reset(self, username, password, user):
        if self.service.reset(username,password,user):
            print("You have successfully reset your account!")
            print(f"Your new username: {user.get_username()}")
            print(f"Your new password: {user.get_password()}")
        else:
            print("Username already exists, try another.")