from random import choice

GAME_CHOICES = ("r", "p", "s")  # rock, paper, scissor
RULES = {
    ('p', 'r'): 'p',
    ('p', 's'): 's',
    ('r', 's'): 'r',
}


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
    @staticmethod
    def find_winner(player, system):
        match = {player, system}
        if len(match) == 1:
            return None

        return RULES[tuple(sorted(match))]


class Play:
    massage = None

    def __init__(self):
        self.winner = Winner

    def play_on_hand(self):
        result = {"system": 0, "player": 0}

        while result["system"] < 3 and result["player"] < 3:
            player_choice = Player.get_user_choice()
            system_choice = System.get_system_choice()
            winner_of_game = self.winner.find_winner(player_choice, system_choice)

            if winner_of_game == player_choice:
                self.massage = "you win"
                result["player"] += 1
            elif winner_of_game == system_choice:
                self.massage = "system win"
                result["system"] += 1
            else:
                self.massage = "Draw"

            print(f"player choice: {player_choice}, "
                  f"system choice: {system_choice},winner: {self.massage}")
        self.update(result)

    def update(self, result):
        scoreboard = {"system": 0, "player": 0}
        if result["player"] == 3:
            scoreboard["player"] += 1
        elif result["system"] == 3:
            scoreboard["system"] += 1

        print("#" * 30)
        print("##", f'\t user:{scoreboard["player"]}'.ljust(24), "##")
        print("##", f'\t system:{scoreboard["system"]}'.ljust(24), "##")
        print("##", f"\t last game: {self.massage}".ljust(24), "##")
        print("#" * 30)
        self.play_again()

    def play_again(self):
        again = input("do you want play again? (y/n) ")
        if again == "y":
            self.play_on_hand()
        elif again == "n":
            return f"goodbye!"
        else:
            print("wrong choice, try again please")
            self.play_again()

    def run(self):
        self.play_on_hand()
        self.play_again()


if __name__ == "__main__":
    play = Play()
    play.run()
