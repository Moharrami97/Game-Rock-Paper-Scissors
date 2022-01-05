from random import choice

GAME_CHOICES = ("r", "p", "s")  # rock, paper, scisseor
RULLES = {
    ("p", "r"): "p",
    ("p", "s"): "s",
    ("r", "s"): "r"
}


class Player:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_user_choice():
        user_input = input("enter your choice please: ")
        if user_input is not GAME_CHOICES:
            print("oops! wrong choice, try again please")
            Player.get_user_choice()
        return user_input


class System:
    @staticmethod
    def get_system_choice():
        return choice(GAME_CHOICES)


class Winner:
    @staticmethod
    def find_winner():
        match = {Player.get_user_choice(), System.get_system_choice()}
        if len(match) == 1:
            return None
        return RULLES[tuple(sorted(match))]


class PlayOnHand:
    pass


class PlayAgain:
    pass


class Play:
    PlayOnHand()
    PlayAgain()


if __name__ == "__main__":
    play = Play()
