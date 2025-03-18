from flask import *
app = Flask(__name__)
# Homepage route for better+cleaner intergration
@app.route('/')
def home():
    return render_template('index.html')
# App route to NeoWs for better+cleaner intergration
@app.route('/apod')
def APOD():
    return render_template('apod.html',url="test")
# App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs')
def home():
    return render_template('NeoWs.html')


if __name__ == '__main__':
    app.run(debug=True)
    