
class Game:
    def __init__(self):
            self.difficulty = None

    def difficulty(self):
        if self == "Easy":
            return self.difficulty == "Easy"
        elif self.difficulty == "Hard":
            return self.difficulty == "Hard"
        elif self.difficulty == "Extreme":
            return self.difficulty == "Extreme"
        return self.difficulty


if __name__ == '__main__':
    Game()

