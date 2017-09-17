from textblob import TextBlob, Word
from word2number import w2n
from user import User
from goal import Goal
from responses import get_response

def clean_text(text):
    text = text.replace("$", "").replace(",", "").replace("!", "").replace("@", " ").replace("#", "").replace("%", " ").replace("^", " ").replace("&", " ").replace("(", "").replace(")", "").replace("*", "").replace(":", "").replace(";", "")
    return(text)

def find_action(sent):
    action = None
    save_words = ["saved","save","stored","deposited","sabed", "savd", "sav", "socked", "put", "desposited", "pay towards", "pay"]
    spend_words = ["spent", "spend", "withdrew", "withdraw","reduced", "borrowed", "stole", "took", "took out", "removed"]
    new_goal_words = ["goal", "buy", "new", "take a", "create"]
    del_goal_words = ["remove", "delete"]
    list_words = ["list", "tell", "tell me"]

    for word, pos in sent.pos_tags:
        if pos[0] == "V":
            if word in save_words:
                action = "save"
            elif word in spend_words:
                action = "spend"
            elif word in del_goal_words:
                action = "del_goal"
            elif word in new_goal_words:
                action = "new_goal"
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
    for word, pos in sent.pos_tags:
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

def find_extra(sent):
    action = None
    greeting_words = ["hello","hi","hey","wassup"]
    for word,pos in sent.pos_tags:
        if word in greeting_words:
            action = 'greet'

    return action

def find_candidates(blob):
    action, amount, goal = (None, None, None)
    for sent in blob.sentences:
        action = find_extra(sent)
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

def check_goal_helper(goal, user):
    goalobj = user.find_goal(goal)
    if goalobj:
        return goalobj

def check_goal(goal, user):
    if check_goal_helper(goal, user):
        return check_goal_helper(goal, user)
    goal = goal.pluralize()
    if check_goal_helper(goal, user):
        return check_goal_helper(goal, user)
    goal = goal.singularize()
    if check_goal_helper(goal, user):
        return check_goal_helper(goal, user)
    goal = Word(goal)
    goal = goal.lemmatize()
    if check_goal_helper(goal, user):
        return check_goal_helper(goal, user)

def change_money(user, goal, amt):
        goalobj = check_goal(goal, user)
        if not goalobj:
            return "{} isn't one of your goals".format(goal)
        goalobj.balance += amt
        if goalobj.balance >= goalobj.target:
            return get_response('congrats', amt=goalobj.target, goal=goalobj.name)
        elif amt <= 0:
            return get_response('balancedown',amt=abs(amt),target=goalobj.target,goal=goalobj.name)
        else:
            return get_response('balanceup',amt=amt,target=goalobj.target,goal=goalobj.name)

def set_goal(user,goal, amt):
        user.add_goal(goal,amt)
        print(user.goals)
        return get_response('new_goal',goal=goal,amt=amt)

def unset_goal(user,goal):
        goalobj = check_goal(goal, user)
        user.remove_goal(goalobj)
        print(user.goals)
        return get_response('del_goal',goal=goal)

def generate_response(action,amt,goal,text,user):
    if action in ["save", "spend"]:
        if not amt:
            return "How much are we talking here? Please send the message again, with a monetary amount"
        if action == "spend":
            amt *= -1
        return change_money(user, goal, amt)
    elif action == "new_goal":
        return set_goal(user,goal,amt)
    elif action == "del_goal":
        return unset_goal(user, goal)
    elif action == "list" or goal == "goals":
        return get_response('list_goal',goal=', '.join(g.name for g in user.goals))
    elif action == "greet":
        return get_response('hello',user=user.name)
    elif goal == None:
        return "I didn't understand your goal. Please send the message again, with a goal at the end."
    elif amt == None:
        return "How much are we talking here? Please send the message again, with a monetary amount"
    else:
        return "I didn't understand your message :("
