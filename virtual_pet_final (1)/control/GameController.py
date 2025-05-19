from service.GameService import GameService
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)

class GameController:
    def __init__(self):
        self.service = GameService()

    # call the function in GameService and start game
    def start_game(self, username):
        self.service.choose_pet(username)