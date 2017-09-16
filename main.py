from flask import Flask, request, redirect

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    """ respond to basic web request """
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
