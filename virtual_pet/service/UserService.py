from pojo.User import User
from mapper.UserMapper import UserMapper
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

class UserService:
    def __init__(self):
        self.mapper = UserMapper()

    # get the username and password, and save it in json file
    def register(self, username, password):
        user = User(username, password, pet=None)
        return self.mapper.save_user(user)

    # authenticate user information
    def authenticate(self, username, password):
        user = self.mapper.get_user(username)
        # if user doesn't exist or password is not true, return false, else return true.
        if user is None:
            return False
        elif user.get_password() != password:
            return False
        else:
            return True
            
    # reset the password and username  
    def reset(self, username, password, user):
        User=self.mapper.get_user(username)
        if User is None or User.username==user.get_username():
            user.set_username(username)
            user.set_password(password)
            return True
        else:
            return False
