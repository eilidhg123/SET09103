from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    #home page
    if request.method=='POST':
        print(request.form)
        level=request.form['level']
        return "Hopefully this works" % level
    else:
        return render_template('home.html')

@app.route("/stageone/", methods=['POST','GET'])
def stageone():
    #stage one pagei
    if request.method=='POST':
        print(request.form)
        level=request.form['level']
        return "look you mad it to" % level
    else:
        return redirect(url_for('home'))

@app.route("/stagetwo/", methods=['POST','GET'])
def stagetwo():
    #stage two page
    if request.method=='POST':
        print(request.form)
        level=request.form['level']
        return "bruh this needs an actual page here" % level
    else:
        return "This is where stage two lives"

@app.errorhandler(404)
def pagenotfound():
    #a catch for pages and paths that don't exist
    return "Error, page doesn't exist"

@app.route('/config/')
def config():
    s=[]
    s.append('debug:'+app.config['DEBUG'])
    s.append('port:'+app.config['port'])
    s.append('url:'+app.config['url'])
    s.append('ip_address:'+app.config['ip_address'])
    return ', '.join(s)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
