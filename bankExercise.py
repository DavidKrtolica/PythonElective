class Bank:
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

class Customer:
    def __init__(self, *args):
        self.name = args[0]
