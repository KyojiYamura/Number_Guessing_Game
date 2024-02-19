import random


class Game:
    hot_streak_easy = 0
    hot_streak_hard = 0
    hot_streak_extreme = 0
    lost= False


    def __init__(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == "easy":
            self.play_difficult_easy()
        if self.difficulty == "hard":
            self.play_difficult_hard()
        if self.difficulty == "extreme":
            self.play_difficult_extreme()
        if self.difficulty == "exit":
            self.exit()

    def exit(self):
        print("Your score was: ", self.score())
        Game.lost = True
        exit()
    def score(self):
        x = sum((Game.hot_streak_easy, Game.hot_streak_hard, Game.hot_streak_extreme))
        return x
    def play_difficult_easy(self):
        self.x = 3
        turns = 0
        answer = str(''.join(self.get_random_number()))
        print("Game difficulty: Easy (XXX)")
        while True:
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            if len(user_guess) == 3:
                turns += 1
                if turns == 10:
                    print("You have lost!")
                    print(f"The number was: {answer}")
                    self.exit()
                elif user_guess == answer:
                    print(f"You have won in {turns} turns!")
                    Game.hot_streak_easy += 1
                    break
                else:
                    user_numbers = [str(i) for i in user_guess]
                    hidden_number = [str(i) for i in answer]
                    green_color = "\033[92m"
                    red_color = "\033[91m"
                    yellow_color = "\033[93m"
                    reset_color = "\033[0m"

                    for i in range(len(user_numbers)):
                        if user_guess[i] == hidden_number[i]:
                            print(green_color + user_guess[i] + reset_color, end="")
                        elif user_numbers[i] in hidden_number:
                            print(yellow_color + user_guess[i] + reset_color, end="")
                        elif user_numbers[i] not in hidden_number:
                            print(red_color + user_guess[i] + reset_color, end="")
            else:
                print("You need 3 numbers")

    def play_difficult_hard(self):
        self.x = 5
        turns = 0
        answer = str(''.join(self.get_random_number()))
        print("Game difficulty: Hard (XXXXX)")
        while True:
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            if len(user_guess) == self.x:
                turns += 1
                if turns == 10:
                    print("You have lost!")
                    print(f"The number was: {answer}")
                    break
                elif user_guess == answer:
                    print(f"You have won in {turns} turns!")
                    Game.hot_streak_hard += 3
                    break
                else:
                    user_numbers = [str(i) for i in user_guess]
                    hidden_number = [str(i) for i in answer]
                    green_color = "\033[92m"
                    red_color = "\033[91m"
                    yellow_color = "\033[93m"
                    reset_color = "\033[0m"

                    for i in range(len(user_numbers)):
                        if user_guess[i] == hidden_number[i]:
                            print(green_color + user_guess[i] + reset_color, end="")
                        elif user_numbers[i] in hidden_number:
                            print(yellow_color + user_guess[i] + reset_color, end="")
                        elif user_numbers[i] not in hidden_number:
                            print(red_color + user_guess[i] + reset_color, end="")
            else:
                print("You need 5 numbers")

    def play_difficult_extreme(self):
        self.x = 7
        turns = 0
        answer = str(''.join(self.get_random_number()))
        print("Game difficulty: Hard (XXXXX)")
        while True:
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            if len(user_guess) == self.x:
                turns += 1
                if turns == 10:
                    print("You have lost!")
                    print(f"The number was: {answer}")
                    break
                elif user_guess == answer:
                    print(f"You have won in {turns} turns!")
                    Game.hot_streak_extreme += 10
                    break
                else:
                    user_numbers = [str(i) for i in user_guess]
                    hidden_number = [str(i) for i in answer]
                    green_color = "\033[92m"
                    red_color = "\033[91m"
                    yellow_color = "\033[93m"
                    reset_color = "\033[0m"

                    for i in range(len(user_numbers)):
                        if user_guess[i] == hidden_number[i]:
                            print(green_color + user_guess[i] + reset_color, end="")
                        elif user_numbers[i] in hidden_number:
                            print(yellow_color + user_guess[i] + reset_color, end="")
                        elif user_numbers[i] not in hidden_number:
                            print(red_color + user_guess[i] + reset_color, end="")
            else:
                print("You need 7 numbers")

    def get_random_number(self):
        generated_number = set()
        while len(generated_number) < self.x:
            n = random.randint(0, 9)
            generated_number.add(str(n))
        return generated_number


def get_difficulty():
    while True:
        difficulty = input("Select your difficulty (Easy, Hard or Extreme): ").lower()
        if difficulty in ["easy", "hard", "extreme", "exit"]:
            return difficulty

        else:
            print("Invalid difficulty! Please select either Easy, Hard or Extreme.\n")


if __name__ == '__main__':
    print("________________Welcome to the game!________________")
    game = None
    while Game.lost != True:
        print("________________Guess the new number________________")
        if game:
            print(f"________________Current score is: {game.score()}________________")
        difficulty = get_difficulty()
        game = Game(difficulty)

