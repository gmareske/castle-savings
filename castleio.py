from textblob import TextBlob
from user import User
from goal import Goal
from word2number import w2n
def clean_text(text):
    text = text.replace("$", "").replace(",", "").replace("!", "").replace("@", " ").replace("#", "").replace("%", " ").replace("^", " ").replace("&", " ").replace("(", "").replace(")", "").replace("*", "").replace(":", "").replace(";", "")
    return(text)

def find_action(sent):
    action = None
    save_words = ["saved","save","stored","deposited",]
    spend_words = ["spent", "spend", "withdrew", "withdraw",]
    goal_words = ["goal", "buy", "new",]
    list_words = ["list",]
    for word, pos in sent.pos_tags:
        if pos[0] == "V":
            if word in save_words:
                action = "save"
            elif word in spend_words:
                action = "spend"
            elif word in goal_words:
                action = "goal"
            elif word in list_words:
                action = "list"
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
        try:
            amount = w2n.word_to_num(word)
        except:
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
    return generate_response(action,amount,goal,text,user)

def check_balance(user, goalobj):
    if goalobj.balance >= goalobj.target:
        user.remove_goal(goalobj.name)
        return "Congradulations: you reached your goal to buy a {}!".format(goalobj.name)
    else:
        pass

def change_money(user, goal, amt):
        goalobj = user.find_goal(goal)
        if not goalobj:
            return "{} isn't one of your goals.".format(goal)
        if action == "spend":
            amt *= -1
        goalobj.balance += amt
        return "Have saved ${} out of ${} for {}".format(goalobj.balance,goalobj.target,goalobj.name)
        check_balance(user, goalobj)

def set_goal(goal, amt):
        user.add_goal(goal,amt)
        print(user.goals)
        return "Now we're saving for {}, which will cost about ${}.".format(goal,amt)

def generate_response(action,amt,goal,text,user):
    if action in ["save", "spend"]:
        change_money(user, goal, amt)
    elif action == "goal":
        set_goal(goal,amt)
    elif action == "list" or goal == "goals":
        return ', '.join(g.name for g in user.goals)
    else:
        return "I didn't understand your message :("
