from flask import *
from datetime import *
from pandas import *
from Nasa_API_module import *
import Nasa_API_module as N
import datetime
import json
date_ = datetime.datetime.now().strftime("%Y-%m-%d")

app = Flask(__name__)
# Homepage route
@app.route('/')
def home_page():
    return render_template('index.html')
# Help page to assist users
@app.route('/help_page')
def help_page():
    return render_template('help.html')
# App route to APOD for better+cleaner intergration
@app.route('/Apod',methods=['POST'])
def APOD():
    #TO DO! 
    Apod_date = request.form.get('Apod-date')
    print(Apod_date)
    Apod_date =N.APOD(Apod_date)['date']
    if Apod_date == None:
        pass
    else:
        Apod_explanation =N.APOD(Apod_date)['explanation']
        Apod_url =N.APOD(Apod_date)['hdurl']
        return render_template('apod.html',date=Apod_date,explanation=Apod_explanation,url=Apod_url)
# App route to NeoWs Lookup for better+cleaner intergration
@app.route('/NeoWs_Lookup',methods=['POST'])
def NeoWS_Lookup():
    Asteroid_id=request.form.get('Asteroid_id')
    print(Asteroid_id)
    NeoWs_lookup_data =N.NeoWs_lookup(Asteroid_id)
    print(NeoWs_lookup_data)
    return render_template('NeoWs_look_up.html')
#App route to NeoWs Feed for better+cleaner intergration
@app.route('/NeoWs_Feed', methods=['POST'])
def NeoWS_Feed():
    start=request.form.get('start')
    end=request.form.get('end')
    print(start+end)
    NeoWs_feed_data =N.NeoWs_Feed(start,end)
    #TO DO! 
    # ADD function visualise the graph.
    return render_template('NeoWs_feed.html')
# Param App route
@app.route('/param',methods=['POST'])
def param_selection():
    Api_choice=request.form.get('API_Selection')
    return render_template('param_select.html',API_choice=Api_choice,today=date_)


""" The reason why all of the API fetching is seperate is because it allows the program to be cleaner and more organised. 
It makes the code more readable and allows the HTML to be simpler and more basic.
"""

if __name__ == '__main__':
    app.run(debug=True)
    