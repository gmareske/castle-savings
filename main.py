from flask import Flask, request, redirect, render_template
from textblob import TextBlob
from castleio import parse_msg

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    """ respond to basic web request """
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(debug=True)
    msg = ("I spent 400 from the yacht")
    parse_msg(msg, None)
