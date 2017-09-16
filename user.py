class User(object):
    
    def __init__(self, name, number):
        self.goals = []
        self.messages = []
        self.name = name
        self.number = number
        
    def add_msg(self, from_who, msg):
        """
        Add a message to the message history
        """
        pass

    def add_goal(self, goal):
        self.goals.append(goal)

