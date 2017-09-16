from textblob import TextBlob
from user import User
from goal import Goal

def clean_text(text):
    return text

def find_action(sent):
    action = None
    save_words = ["saved","save","stored","deposited"]
    spend_words = ["spent", "spend", "withdrew", "withdraw"]
    goal_words = ["goal", "buy", "new"]
    for word, pos in sent.pos_tags:
        if pos[0] == "V":
            if word in save_words:
                action = "save"
            elif word in spend_words:
                action = "spend"
            elif word in goal_words:
                action = "goal"
            else:
                action = word
    return action

def find_amount(sent):
    amount = None
    for word, pos in sent.pos_tags:
        try:
            amount = float(word)
        except ValueError:
            pass
    return amount

def find_goal(sent):
    goal = None
    for word, pos in sent.pos_tags:
        if "NN" in pos:
            goal = word

    return goal

def find_candidates(blob):
    action, amount, goal = (None, None, None)
    for sent in blob.sentences:
        action = find_action(sent)
        amount = find_amount(sent)
        goal = find_goal(sent)

    return action, amount, goal

def parse_msg(text, user):
    text = clean_text(text)
    blob = TextBlob(text.lower())
    action, amount, goal = find_candidates(blob)
    print(action, amount, goal)
    print(generate_response(action,amount,goal,text,user))

def generate_respone(action,amt,goal,text,user):
    if action in ["save", "spend"]:
        goal = user.find_goal(goal)
        if action == "spend":
            amt *= -1
        goal.balance += amt
        return generate_report(goal)
        
    elif action == "goal":
        user.add_goal(amt,goal)
        return "Now we're saving for a {}, which will cost about {}.".format(goal,amt)

def generate_report(goal):
    return "Savings for goal {}: ${} out of ${}".format(goal.name,goal.balance,goal.target)
