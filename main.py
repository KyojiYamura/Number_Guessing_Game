import random


class Game:
    player_score = 0
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
        print("Current score: ", self.player_score)
        exit()
    def play_difficult_easy(self):
        self.x = 3
        turns=0
        answer = str(''.join(self.get_random_number()))
        for i in range(11):
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            turns+=1
            if i == 10:
                print("You have lost!")
                print(f"The number was: {answer}")
                break
            elif user_guess == answer:
                print(f"You have won in {turns} turns!")
                Game.player_score +=1
                break
            else:
                user_numbers = [str(i) for i in user_guess]
                hidden_number =[str(i) for i in answer]
                green_color = "\033[92m"
                red_color = "\033[91m"
                yellow_color = "\033[93m"
                reset_color = "\033[0m"

                for i in range(len(user_numbers)):
                    if user_guess[i]==hidden_number[i]:
                        print(green_color + user_guess[i]+ reset_color,end="")
                    elif user_numbers[i] in hidden_number:
                        print(yellow_color + user_guess[i] + reset_color, end="")
                    elif user_numbers[i] not in hidden_number:
                        print(red_color + user_guess[i] + reset_color, end="")


    def play_difficult_hard(self):
        self.x = 5
        turns = 0
        answer = str(''.join(self.get_random_number()))
        for i in range(11):
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            turns += 1
            if i == 10:
                print("You have lost!")
                print(f"The number was: {answer}")
                break
            elif user_guess == answer:
                print(f"You have won in {turns} turns!")
                Game.player_score += 1
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
    def play_difficult_extreme(self):
        self.x = 7
        turns = 0
        answer = str(''.join(self.get_random_number()))
        for i in range(11):
            user_guess = str(''.join(list(input("\nGuess the number: "))))
            turns += 1
            if i == 10:
                print("You have lost!")
                print(f"The number was: {answer}")
                break
            elif user_guess == answer:
                print(f"You have won in {turns} turns!")
                Game.player_score += 1
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

    def get_random_number(self):
        generated_number = set()
        while len(generated_number) < self.x:
            n = random.randint(0, 9)
            generated_number.add(str(n))
        return generated_number
def get_difficulty():
    while True:
        difficulty = input("Select your difficulty (Easy, Hard or Extreme): ").lower()
        if difficulty in ["easy","hard","extreme","exit"]:
            return difficulty

        else:
            print("Invalid difficulty! Please select either Easy, Hard or Extreme.\n")



if __name__ == '__main__':
    print("________________Welcome to the game!________________")
    while True:
        print("________________Guess the new number________________")
        print(f"________________Current streak is: {Game.player_score}________________")
        difficulty = get_difficulty()
        game = Game(difficulty)
