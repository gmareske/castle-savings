import random
import re

RESPS = {
    'unknown': [],
    'congrats': [],
    'balance': [],
    'new_goal': [],
    'list_goal': [],
    'hello': [],
    
    }

def get_response(kind,**kwargs):
    resp = RESPS.get(kind)
    assert resp
    resp = random.choice(resp)
    return resp.format(**kwargs)
    
