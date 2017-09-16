from flask import Flask, request, redirect, render_template
#from textblob import TextBlob
from twilio.twiml.messaging_response import MessagingResponse, Message

from castleio import parse_msg
from user import User

app = Flask(__name__)


USERS = {}
# multiple users support
def add_user(name, phone_str):
    user = User(name,phone_str)
    USERS[phone_str] = user

# TEST DATA
add_user("Griffin", "+19132068204")
add_user("Philip", "+15155081003")
USERS["+19132068204"].add_goal("loans", 100000) # Griffin
USERS["+15155081003"].add_goal("flamethrower",6900)
# END TEST DATA

@app.route("/hello",methods=['GET'])
def hello():
    """ respond to basic web request """
    return render_template('index.html')

@app.route("/",methods=['GET','POST'])
def reply():
    print("got a text!")
    msg = request.form['Body']
    sender = request.form['From']
    user = USERS[sender]
    if not user:
        return
    print(sender)
    print(msg)
    reply = parse_msg(msg,user)
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

