import os
import json
from pojo.User import User
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FILE = os.path.join(ROOT_DIR, "users.json")

# Here is the class connect with json file，it can map the object 'User' to the information in users.json.
class UserMapper:
    def __init__(self):
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'w') as f:
                json.dump({}, f)

    # read the information in json file, and map it to the object User.
    def get_user(self, username):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        user_data = data.get(username)
        return User(**user_data) if user_data else None

    # save the new registered user information in json file, if the username exisist, return false, else return true.
    def save_user(self, user):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        if user.username in data:
            return False
        data[user.username] = user.__dict__
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        return True

    # update user information when there is anything change in their status.
    def update_user(self, user, id):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        data[id] = user.__dict__
        data[user.get_username()]=data.pop(id)
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)