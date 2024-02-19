import random
import sqlite3
from colorama import init, Fore, Style

class Game:
    hot_streak_easy = 0
    hot_streak_hard = 0
    hot_streak_extreme = 0
    lost = False

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.conn = sqlite3.connect('scores.db')
        if self.difficulty == "easy":
            self.play_difficult_easy()
        if self.difficulty == "hard":
            self.play_difficult_hard()
        if self.difficulty == "extreme":
            self.play_difficult_extreme()
        if self.difficulty == "exit":
            self.exit()
        if self.difficulty =="scores":
            self.print_scoreboard()
    def print_scoreboard(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM scoreboard")
        print("ID\tName\tScore")
        print("---------------------")
        rows = cursor.fetchall()
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t{row[2]}")

        self.conn.close()  # Close the database connection
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
               CREATE TABLE IF NOT EXISTS scoreboard(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name varchar(20),
                   score int
               )
           ''')
        self.conn.commit()

    def add_score(self, name, score):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO scoreboard (name, score) VALUES (?, ?)", (name, score))
        self.conn.commit()

    def exit(self):
        print("Your score was: ", self.score())
        self.create_table()
        player_name = get_player_name()
        game.add_score(player_name, game.score())

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
                    print(f"You have won in {turns} turns!\n\n")
                    Game.hot_streak_easy += 1
                    break
                else:
                    user_numbers = [str(i) for i in user_guess]
                    hidden_number = [str(i) for i in answer]
                    green_color = Fore.GREEN
                    red_color = Fore.RED
                    yellow_color = Fore.YELLOW
                    reset_color = Style.RESET_ALL
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
                    print(f"You have won in {turns} turns!\n\n")
                    Game.hot_streak_hard += 3
                    break
                else:
                    user_numbers = [str(i) for i in user_guess]
                    hidden_number = [str(i) for i in answer]
                    green_color = Fore.GREEN
                    red_color = Fore.RED
                    yellow_color = Fore.YELLOW
                    reset_color = Style.RESET_ALL
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
        print("Game difficulty: Extreme (XXXXXXX)")
        while True:
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            if len(user_guess) == self.x:
                turns += 1
                if turns == 10:
                    print("You have lost!")
                    print(f"The number was: {answer}")
                    break
                elif user_guess == answer:
                    print(f"You have won in {turns} turns!\n\n")
                    Game.hot_streak_extreme += 10
                    break
                else:
                    user_numbers = [str(i) for i in user_guess]
                    hidden_number = [str(i) for i in answer]
                    green_color = Fore.GREEN
                    red_color = Fore.RED
                    yellow_color = Fore.YELLOW
                    reset_color = Style.RESET_ALL

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

def get_player_name():
    return input("Enter your nickname: ")

def get_difficulty():
    while True:
        difficulty = input("Select your difficulty (Easy, Hard or Extreme): ").lower()
        if difficulty in ["easy", "hard", "extreme", "exit",'scores']:
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

