from flask import *
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/apod')
def APOD():
    return render_template('apod.html',url="test")

@app.route('/NeoWs')
def home():
    return render_template('NeoWs.html')


if __name__ == '__main__':
    app.run(debug=True)
    