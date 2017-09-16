from goal import Goal

class User(object):
    
    def __init__(self, name, number):
        self.goals = []
        self.messages = []
        self.name = name
        self.number = number
        
    def add_msg(self, msg, from_user=True):
        """
        Add a message to the message history
        """
        self.message.append({'msg': msg, 'from_user': from_user})

    def add_goal(self, name, amt, balance=0):
        goal = Goal(name,amt,balance)
        self.goals.append(goal)

    def find_goal(self, query):
        for goal in self.goals:
            if goal.name == query:
                return goal
        return None

