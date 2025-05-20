from control.UserController import UserController
from control.GameController import GameController

import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

def main():

    login_ctrl = UserController()
    game_ctrl = GameController()

    ### Here is the place to start the game, you can register your account, login it and start game, or quit the game.
    while True:
        print("\nVirtual Pet Game")
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "3":
            print("Goodbye!")
            break

        if choice not in ["1", "2"]:
            print("Invalid choice. Please try again.")
            continue

        username = input("Username: ")
        password = input("Password: ")

        if choice == "1":
            login_ctrl.register(username, password)
        elif choice == "2":
            if login_ctrl.login(username, password):
                game_ctrl.start_game(username)
            else:
                print("Please try again.")

if __name__ == "__main__":
    main()