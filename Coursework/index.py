from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def start():
    render_template('form.html')
    return render_template('home.html')

@app.route("/home/", methods=['POST','GET'])
def home():
    #home page
    return render_template('home.html')

@app.route('/accessability')
def accessability():
    return "Welcome to the Accessability menu"

@app.route("/stageone/", methods=['POST','GET'])
def stageone():
    #stage one page
    return render_template('stageone.html')

@app.route("/stagetwo/", methods=['POST','GET'])
def stagetwo():
    #stage two page
    return render_template('stagetwo.html')

@app.errorhandler(404)
def pagenotfound(error):
    #a catch for pages and paths that don't exist
    return "Error, page doesn't exist"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
