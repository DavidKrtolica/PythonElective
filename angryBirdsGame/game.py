import random

class Bird:
    def __init__(self, x, y, direction, icon):
        self.x = x
        self.y = y
        self.direction = direction
        self.icon = icon


class Pig:
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = icon


class Board():
    def __init__(self):
        self.Bird = Bird(random.randint(1,10), random.randint(1,10), 1, 'B')
        self.Pig = Pig(random.randint(1,10), random.randint(1,10), 'P')

    def printBoard(self):
        board = [["*" for a in range(10)] for b in range(10)]
        board[self.Bird.y-1][self.Bird.x-1] = self.Bird.icon
        board[self.Pig.y-1][self.Pig.x-1] = self.Pig.icon
        for i in board:
            print(" ".join(i))        


class Workspace():
    def __init__(self):
        self.instructions = ("What steps do you want to perform? \n"
        "Options: move forward(f), turn left(l), turn right(r) \n"
        "Type \"q\" when finished")

    def printInstr(self):
        print(self.instructions)


class Game():
    def __init__(self):
        self.Board = Board()
        self.Workspace = Workspace()

    def run(self):
        self.Board.printBoard()
        self.Workspace.printInstr()
        userInput = ""
        while (userInput != 'q'):
            userInput = input("Move: ")
            if (userInput == 'r'):
                self.Board.Bird.direction += 1
                self.Board.printBoard()
            elif (userInput == 'l'):
                self.Board.Bird.direction -= 1
                self.Board.printBoard()
            if (userInput == 'f'):
                if (self.Board.Bird.direction == 0):
                        self.Board.Bird.y -= 1
                        self.Board.printBoard()
                elif (self.Board.Bird.direction == 2):
                        self.Board.Bird.y += 1
                        self.Board.printBoard()
                elif (self.Board.Bird.direction == 1):
                    self.Board.Bird.x += 1
                    self.Board.printBoard()
                elif (self.Board.Bird.direction == 3):
                    self.Board.Bird.x -= 1
                    self.Board.printBoard()
        if (self.Board.Bird.x == self.Board.Pig.x and self.Board.Bird.y == self.Board.Pig.y):
            print("Ufff the pig is dead!")
            print(f'Birds position: [{self.Board.Bird.x}, {self.Board.Bird.y}]')
            print(f'Pigs position: [{self.Board.Pig.x}, {self.Board.Pig.y}]')
        else:
            print("You missed :(")
            print(f'Birds position: [{self.Board.Bird.x}, {self.Board.Bird.y}]')
            print(f'Pigs position: [{self.Board.Pig.x}, {self.Board.Pig.y}]')

#RUN THE GAME
g = Game()
g.run()