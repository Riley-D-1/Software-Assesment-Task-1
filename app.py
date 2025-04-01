from flask import *
from datetime import *
import pandas as pd
from pandas import *
from Nasa_API_module import *
import Nasa_API_module as N
import datetime
import matplotlib.pyplot as plt
from pytz import timezone
# Importing all dependencies with some being simplified to save on typing and make the code easier to read and understand
# Have to set the timezone to American in order to avoid problems with trying to fetch a day that doesn't exist
tz = timezone('EST')
date_ = datetime.datetime.now(tz).strftime("%Y-%m-%d")

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
    # Requests form to get the date to fetch API date
    Apod_date = request.form.get('Apod-date')
    print(Apod_date)
    Apod_date = str(Apod_date)
    Apod_data=N.APOD(Apod_date)
    if Apod_data is not None:
        Apod_explanation = Apod_data['explanation']
        Apod_date = Apod_data['date']
        Apod_url = Apod_data['hdurl']
        Apod_title = Apod_data['title']
        df1=pd.DataFrame(columns = ["Apod_date","Apod_Url","Apod_title","Apod_explanation"])
        df1.loc[len(df1)] = [Apod_date, Apod_url,Apod_title,Apod_explanation]
        df1.to_csv('history/history_APOD.csv', encoding='utf-8', index=True)
        return render_template('apod.html',date=Apod_date,explanation=Apod_explanation,url=Apod_url,title=Apod_title)
    else:
        # Way to pass the error back to the program  without recoding the if statement and nasa api module.
        f = open("history/error.txt", "r")
        error=f.read()
        return render_template('error.html',Type="Apod",error_code=error)
# App route to NeoWs Lookup for better+cleaner intergration
@app.route('/NeoWs_Lookup',methods=['POST'])
def NeoWS_Lookup():
    Asteroid_id=request.form.get('Asteroid_id')
    print(Asteroid_id)
    NeoWs_lookup_data = N.NeoWs_lookup(Asteroid_id)
    if NeoWs_lookup_data is not None:
        Neo_data=NeoWs_lookup_data
        df = pd.DataFrame(columns=["Close Approach Date","Miss distance (Km)","Velocity in Km/h"])
        dia = Neo_data['estimated_diameter']
        average_dia = dia['meters']['estimated_diameter_min'] + dia['meters']['estimated_diameter_max'] / 2
        Id= Neo_data['id']
        name= Neo_data['name']
        is_hazardous = Neo_data['is_potentially_hazardous_asteroid']
        Absolute_magnitude=Neo_data['absolute_magnitude_h']
        i=0
        for close_data in Neo_data['close_approach_data']:
            i+=1
            df.loc[i, 'Velocity in Km/h'] = close_data['relative_velocity']['kilometers_per_hour']
            df.loc[i, 'Miss distance (Km)'] = close_data['miss_distance']['kilometers']
            df.loc[i, 'Close Approach Date']= close_data['close_approach_date_full']
        print(df)
        df.to_csv('history/History_Neows_Lookup.csv', encoding='utf-8', index=True)
        return render_template('NeoWs_look_up.html',info_table=df,Id=Id,Name=name,average_dia=average_dia,Absolute_magnitude=Absolute_magnitude,is_hazardous=is_hazardous,tables=[df.to_html(classes='data')])
    else:
        # Way to pass the error back to the program  without recoding the if statement and nasa api module.
        f = open("history/error.txt", "r")
        error=f.read()
        return render_template('error.html',Type="NeoWS Lookup",error_code=error)


#App route to NeoWs Feed for better+cleaner intergration
@app.route('/NeoWs_Feed', methods=['POST'])
def NeoWS_Feed():
    start=request.form.get('start')
    end=request.form.get('end')
    print(start+end)
    NeoWs_feed_data = N.NeoWs_Feed(start,end)
    #print(NeoWs_feed_data)
    if NeoWs_feed_data is not None:
        total = NeoWs_feed_data['element_count']
        Neo_data=NeoWs_feed_data['near_earth_objects']
        df = pd.DataFrame(columns = ["ID", "Name","Abosulute_Magintude", "Estimated Diameter", "Is it potentially hazardous","Velocity in Km/h","Miss distance","Close Approach Date"])
        current_date=datetime.datetime.strptime(start, '%Y-%m-%d').date()
        simple_date = start
        j=0
        while simple_date <= end:
            for near in Neo_data[simple_date]:
                # HOLY this is nightmare to read
                dia = near['estimated_diameter']
                average_dia = dia['meters']['estimated_diameter_min'] + dia['meters']['estimated_diameter_max'] / 2
                j+=1
                df.loc[j, 'ID'] = near['id']
                df.loc[j, 'Name'] = near['name']
                df.loc[j, 'Abosulute_Magintude'] = near['absolute_magnitude_h']
                df.loc[j, 'Estimated Diameter'] = average_dia
                df.loc[j, 'Is it potentially hazardous'] = near['is_potentially_hazardous_asteroid']
                close_data=near['close_approach_data']
                df.loc[j, 'Velocity in Km/h'] = close_data[0]['relative_velocity']['kilometers_per_hour']
                df.loc[j, 'Miss distance'] = close_data[0]['miss_distance']['kilometers']
                df.loc[j, 'Close Approach Date']= close_data[0]['close_approach_date_full']
            current_date += timedelta(days=1)
            simple_date = current_date.strftime("%Y-%m-%d")
        print(df)
        df.to_csv('history/history_NeoWs_feed.csv', encoding='utf-8', index=True)
        """ date_occurence = (df['Close Approach Date'] == '').sum()
        print(date_occurence)
        plt.bar(date_occurence,df['Close Approach Date'])
        
        plt.ylabel("Astroids per Day")
        plt.xlabel("Timestamp")
        plt.title(f"Occurence of Astroids by close aproach date over the last days")
        plt.legend()
        # This pulls an error and it says its unlikely to work becuase its outside the main loop (not really but matplotlib thinks that).
        # Saves plot to a file in static (flask checks here )
        plot_path = 'static/data/data.jpg'
        plt.savefig(plot_path)
        plt.show()
        plt.close()"""
        return render_template('NeoWs_feed.html',tables=[df.to_html(classes='data')],start=start,end=end)
    else:
        # Way to pass the error back to the program  without recoding the if statement and nasa api module.
        f = open("history/error.txt", "r")
        error=f.read()
        return render_template('error.html',Type="NeoWS Feed",error_code=error)
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
    