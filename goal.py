class Goal(object):

    def __init__(self, name, target, balance=0):
        self.name = name
        self.balance = balance
        self.keywords = [name]
        self.target = target
