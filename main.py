from flask import Flask, request, redirect, render_template
#from textblob import TextBlob
from twilio.twiml.messaging_response import MessagingResponse, Message

from castleio import parse_msg
from user import User

app = Flask(__name__)

GOD = User("Griffin", "+19132068204")
GOD.add_goal("yacht", 100000)

@app.route("/hello",methods=['GET'])
def hello():
    """ respond to basic web request """
    return render_template('index.html')

@app.route("/",methods=['GET','POST'])
def reply():
    print("got a text!")
    msg = request.form['Body']
    print(msg)
    reply = parse_msg(msg,GOD)
    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
    
