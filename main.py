from random import choice

GAME_CHOICES = ("r", "p", "s")  # rock, paper, scissor


class Player:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_user_choice():
        user_input = input("enter your choice please: ")
        if user_input not in GAME_CHOICES:
            print("oops! wrong choice, try again please")
            user_input = Player.get_user_choice()
        return user_input


class System:
    @classmethod
    def get_system_choice(cls):
        return choice(("r", "p", "s"))


class Winner:
    RULES = {
        ('r', 'p'): 'p',
        ('p', 's'): 's',
        ('r', 's'): 'r',
    }

    def __init__(self):
        self.player = Player.get_user_choice()
        self.system = System.get_system_choice()

    def find_winner(self):
        match = {self.player, self.system}
        if len(match) == 1:
            print("equal")
            return None
        print(tuple(sorted(match)))
        return self.RULES[tuple(sorted(match))]


class PlayOnHand:
    pass


class PlayAgain:
    pass


class Play:
    PlayOnHand()
    PlayAgain()


if __name__ == "__main__":
    winner = Winner()
    play = Play()
    winner.find_winner()
