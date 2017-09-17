import random
import re

RESPS = {
    'unknown': [
        'I didn\'t catch that, let my put my hearing aids in. Send a new message.',
        'What\'d ya say?? Forgettaboutit',
    ],
    'congrats': [
    'Look at you go, you completed your savings goal for your {goal}!',
    'There is shade today because of a tree planted long ago. Enjoy the shade of your {goal}',
    'Enjoy the {goal}, you sure earned it.'
    ],
    'balanceup': [
        'A penny saved is a penny earned, and you\'ve saved ${amt} out of ${target} for the {goal}',
        'You\'re ${amt} closer to ${target} for the {goal}',
        'You just saved ${amt}, ${target} is right around the corner! Look out, {goal}'
    ],
    'balancedown': [
        'Your {goal} will stay "someday" if you withdraw ${amt} everyday.',
        'No matter how great to talent or effort, goals like your {goal} take time and consitency.',
        'It is not one extraordianry effort won\'t beat consistency when saving {amount} toward your {goal}',
    ],
    'new_goal': [
        'A journey of a thousand miles starts with a single text message, and you\'re on your way to your {goal}',
        'Pretty soon, you\'ll have your {goal}',
        'Today, save, tomorrow, your {goal}',
        'Price is what you pay. Your {goal} is what you get.'
    ],
    'del_goal': [
        'You are no longer saving towards a {goal}. Be sure to save the money somewhere else.'
    ],
    'change_goal_name': [
        'Your goal is now a {goal}, go and get it!',
    ],
    'change_goal_target': [
        'Your target for your {goal} is now {amt}, go forth and conquer',
    ],
    'list_goal': [
        'Here are your missions, if you choose to accept them: {goal}',
        'You have some big plans, here they are: {goal}',
        'You\'ll be all the way to {goal} before you know it',
        'You made a list, check it twice: {goal}',
        'Line them up, knock them down: {goal}',
        'It\'s the journey and the destination when you\'re talking about {goal}',
    ],
    'hello': ['Howdy, {user}'],

    }

def get_response(kind,**kwargs):
    resp = RESPS.get(kind)
    assert resp
    resp = random.choice(resp)
    return resp.format(**kwargs)
