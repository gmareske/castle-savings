import random
import re

RESPS = {
    'unknown': [
        'I didn\'t catch that, let my put my hearing aids in. Send a new message.',
        'What\'d ya say?? Forgettaboutit',
    ],
    'congrats': ['Look at you go, you completed your savings goal for {goal}!'],
    'balance': [
        'A penny saved is a penny earned, and you\'ve saved ${amt} out of ${target} for the {goal}',
    ],
    'new_goal': [
        'A journey of a thousand miles starts with a single text message, and you\'re on your way to a {goal}',
    ],
    'list_goal': ['Here are your missions, if you choose to accept them: {goal}'],
    'hello': ['Howdy, {user}'],
    
    }

def get_response(kind,**kwargs):
    resp = RESPS.get(kind)
    assert resp
    resp = random.choice(resp)
    return resp.format(**kwargs)
    
