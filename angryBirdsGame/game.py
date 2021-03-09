class Bird:
    def __init__(self, x, y, direction, icon):
        self.x = x
        self.y = y
        self.direction = direction
        self.icon = icon
    def move(userInput):
        if (userInput == 'r'):
            direction += 1 
        elif (userInput == 'l'):
            direction -= 1
        if (userInput == 'f' and direction == 0 or direction == 2):
            y += 1
        elif (userInput == 'f' and direction == 1 or direction == 3):
            x += 1

class Pig:
    def __init__(self, x, y, icon):
        self.x = x
        self.y = y
        self.icon = 'P'


class Board:
    def __init__(self):
        self.Bird = Bird(2, 4, 1, 'B')
        self.Pig = Pig(6, 5, 'P')
    def createBoard(self):
        x = 10
        y = 10
        for i in range(y):
            print (' *' * x + ' ')
