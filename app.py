from flask import *
from datetime import *
import datetime
date_ = datetime.datetime.now().strftime("%Y-%m-%d")

app = Flask(__name__)
# Homepage route for better+cleaner intergration
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
    # ADD function calling the API dtaa and then sort it using pandas and visualise any graphs or data.
    return render_template('apod.html')
# App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs_Lookup',methods=['POST'])
def NeoWS_Lookup():
        #TO DO! 
    # ADD function calling the API dtaa and then sort it using pandas and visualise any graphs or data.
    return render_template('NeoWs_look_up.html')
#App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs_Feed', methods=['POST'])
def NeoWS_Feed():
    #TO DO! 
    # ADD function calling the API dtaa and then sort it using pandas and visualise any graphs or data.
    return render_template('NeoWs_feed.html')

@app.route('/param',methods=['POST'])
def param_selection():
    Api_choice=request.form.get('API_Selection')
    return render_template('param_select.html',API_choice=Api_choice,today=date_)


""" The reason why all of the API fetching is seperate is because it allows the program to be cleaner and  
"""



if __name__ == '__main__':
    app.run(debug=True)
    