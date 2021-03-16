class Machine:
    def __init__(self):
        self.power = False
    @property
    def power(self):
        if self.__power == False:
            return 'Not working...'
        else:
            return 'Working!'
    @power.setter
    def power(self, power):
        self.__power = power

    def runMachine(self):
        self.__power = True
        return 'Powered on!'

    def turnOff(self):
        self.__power = False
        return 'Powered off...'

class Papertray:
    def __init__(self, paperAmount):
        self.paperAmount = paperAmount
    
    @property
    def paperAmount(self):
        return self.__paperAmount
    @paperAmount.setter
    def paperAmount(self, paperAmount):
        self.__paperAmount = paperAmount

    def usePaper(self):
        self.__paperAmount -= 1
        print('1 paper used...')
        if self.__paperAmount == 0:
            print('Papertray empty!!!')
    
    def loadPaper(self):
        self.__paperAmount += 1
        print('Added 1 paper...')


class Printer(Machine, Papertray):
    def __init__(self, paperAmount):
        Machine.__init__(self)
        Papertray.__init__(self, paperAmount)

    def runPrinter(self):
        self.runMachine()
        return f'Started printer with {self.paperAmount} papers...'

    def turnOffPrinter(self):
        self.turnOff()
        return f'Shut printer down with {self.paperAmount} papers...'

    def printSomething(self, printing):
        print(printing)
        self.usePaper()
        print(f'Current amount of paper left: {self.paperAmount}')

    def addPaper(self):
        self.loadPaper()
        print(f'Current amount of paper left: {self.paperAmount}')


printer = Printer(10)