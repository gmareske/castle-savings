from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello():
    """ respond to basic web request """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
