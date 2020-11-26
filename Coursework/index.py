from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def home():
    #home page
    if request.method=='POST':
        print(request.form)
        level=request.form['level']
        return "Hopefully this works" % level
    else:
        return "This is the home page that users will be greeted with when they first open the web app"

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

def init(app):
    config=ConfigParser.ConfigParser()
    try:
        config_location="references/defaults.cfg"
        config.read(config_location)

        app.config['DEBUG']=config.get("config","debug")
        app.config['ip_address']=config.get("config","ip_address")
        app.config['port']=config.get("config","port")
        app.config['url']=config.get("config","url")
    except:
        print("Could not read configs from: ",config_location)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
