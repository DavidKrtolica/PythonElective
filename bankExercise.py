class Bank:
    def __init__(self):
        self.accounts = []

    @property
    def accounts(self):
        return self.__accounts
    @accounts.setter
    def accounts(self, accounts):
        self.__accounts = accounts

    def addAccounts(self, *args):
        for acc in args:
            self.__accounts.append(acc)



class Account:
    def __init__(self, accNum, cust):
        self.accNum = accNum
        self.cust = cust

    @property
    def accNum(self):
        return self.__accNum
    @accNum.setter
    def accNum(self, accNum):
        self.__accNum = accNum

    @property
    def cust(self):
        return self.__cust
    @cust.setter
    def cust(self, cust):
        if cust.hasAcc == False:
            self.__cust = cust
            cust.hasAcc = True
        else:
            print('This customer already has an account!')



class Customer:
    def __init__(self, socNum, name, age):
        self.socNum = socNum
        self.name = name
        self.age = age
        self.hasAcc = False

    @property
    def socNum(self):
        return self.__socNum
    @socNum.setter
    def socNum(self, socNum):
        self.__socNum = socNum

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if age >= 18 :
            self.__age = age
        else:
            print('Too young to be a Customer! Setting age to 18...')
            self.__age = 18
    
    @property
    def hasAcc(self):
        return self.__hasAcc
    @hasAcc.setter
    def hasAcc(self, hasAcc):
        self.__hasAcc = hasAcc
            

bank = Bank()

cust1 = Customer(123456789, 'David', 20)
cust2 = Customer(987654321, 'Marko', 16)

acc1 = Account(1000, cust1)
acc2 = Account(2000, cust2)