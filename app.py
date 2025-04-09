from flask import *
from datetime import *
import pandas as pd
from pandas import *
from Nasa_API_module import *
import Nasa_API_module as N
import os
import datetime
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from pytz import timezone
# Importing all dependencies with some being simplified to save on typing and make the code easier to read and understand.
# Have to set the timezone to American in order to avoid problems with trying to fetch a day that doesn't exist from the API.
tz = timezone('EST')
# To limit the calendars by the American date. 
date_ = datetime.datetime.now(tz).strftime("%Y-%m-%d")
# Start the app
app = Flask(__name__)
# Homepage route
@app.route('/')
def home_page():
    return render_template('index.html')
# Help page to assist users
@app.route('/help_page')
def help_page():
    return render_template('help.html')
# An about page to explain the purpose of the site
@app.route('/about_page')
def about_page():
    return render_template('about.html')
# A redirect to clear the history
@app.route('/clear_history_page')
def clear_histoy_page():
    open('history\history.txt', 'w').close()
    return redirect('/')
# The page to view and clear the history
@app.route('/history_page')
def history_page():
    f = open("history\history.txt", "r")
    # Check if history.txt is empty or not.
    if os.path.getsize("history\history.txt") == 0:
        history_clear="Yes"
        # A switch in order not to display an empty dataframe. I still have to pass history df but it won't show on the HTML site.
        history_df = pd.DataFrame(columns=["API type",'API parameters','Date of API fetch'])
    else:
        history_df = pd.DataFrame(columns=["API type",'API parameters','Date of API fetch'])
        i=0
        """  This loop goes through all of the rows and split the vaules by commas. 
        It then appends it to a seperate dataframe so that the website can clearly read it.
        """
        for x in f:
            x=x.split(",")
            i+=1
            history_df.loc[i,'API type'] = x[0]
            history_df.loc[i,'API parameters'] = x[1]
            # The line below is special as it has to remove the /n that is put in by the program to wrap them propely
            history_df.loc[i,'Date of API fetch'] = x[2][:-1]
        # Display the Opposite of the switch so that the DF does display on the HTML site. 
        history_clear="No"
    print(history_df)
    # Return the html with all of the vaules set.
    return render_template('history.html',History_clear=history_clear,tables=[history_df.to_html(classes='data')])
# App route to APOD
@app.route('/Apod',methods=['POST'])
def APOD():
    # Requests form to get the date to fetch API date
    Apod_date = request.form.get('Apod-date')
    Apod_date = str(Apod_date)
    Apod_data=N.APOD(Apod_date)
    """ The if else loop is an error handling statement. 
    It checks that APOD data is in fact valid before continuing with the code. Otherwise it takes you to the error page.
    """
    if Apod_data is not None:
        Apod_explanation = Apod_data['explanation']
        Apod_date = Apod_data['date']
        if Apod_data['media_type'] == "video":
            Apod_url = Apod_data['url']
            media_type = "Video"
        else:
            # To accomdate when the astornomy picture of the day is actually the astronomy video of the day 
            Apod_url = Apod_data['hdurl']
            media_type = "Photo"
        Apod_title = Apod_data['title']
        # Write the type , params and time of fetch to history
        f = open("history/history.txt", "a")
        local_date_=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"APOD,{Apod_date},{local_date_}\n")
        f.close()
        # Return the webpage with all vaules
        return render_template('apod.html',date=Apod_date,explanation=Apod_explanation,url=Apod_url,title=Apod_title,media_type=media_type)
    else:
        # Way to pass the error back to the program  without recoding the if statement and nasa api module.
        f = open("history/error.txt", "r")
        error=f.read()
        return render_template('error.html',Type="Apod",error_code=error)
# App route to NeoWs Lookup
@app.route('/NeoWs_Lookup',methods=['POST'])
def NeoWS_Lookup():
    # Fetch the NeoWs lookup data 
    Asteroid_id=request.form.get('Asteroid_id')
    NeoWs_lookup_data = N.NeoWs_lookup(Asteroid_id)
    """ The if else loop is an error handling statement. 
    It checks that the NeoWS data is in fact valid before continuing with the code. Otherwise it takes you to the error page.
    """
    if NeoWs_lookup_data is not None:
        Neo_data=NeoWs_lookup_data
        df = pd.DataFrame(columns=["Close Approach Date","Miss distance (Km)","Velocity (Km/h)"])
        # Set some of the vaules that don't change because of reoccurences. 
        dia = Neo_data['estimated_diameter']
        average_dia = dia['meters']['estimated_diameter_min'] + dia['meters']['estimated_diameter_max'] / 2
        Id= Neo_data['id']
        name= Neo_data['name']
        is_hazardous = Neo_data['is_potentially_hazardous_asteroid']
        Absolute_magnitude=Neo_data['absolute_magnitude_h']
        i=0
        """ This Loop goes through all of the data row by row and appends each part if the data to a diffrent column of a df."""
        for close_data in Neo_data['close_approach_data']:
            
            i+=1
            df.loc[i, 'Velocity (Km/h)'] = close_data['relative_velocity']['kilometers_per_hour']
            df.loc[i, 'Miss distance (Km)'] = close_data['miss_distance']['kilometers']
            df.loc[i, 'Close Approach Date']= close_data['close_approach_date_full']
        print(df)
        # Write the params, type and fetch time to history 
        f = open("history/history.txt", "a")
        local_date_=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"NeoWs Lookup,{Asteroid_id},{local_date_}\n")
        f.close()
        # Return the HTML page with all vaules set for the Jinja flask templates
        return render_template('NeoWs_look_up.html',Id=Id,Name=name,average_dia=average_dia,Absolute_magnitude=Absolute_magnitude,is_hazardous=is_hazardous,tables=[df.to_html(classes='data')])
    else:
        # Way to pass the error back to the program without recoding the if statement and nasa api module.
        f = open("history/error.txt", "r")
        error=f.read()
        return render_template('error.html',Type="NeoWS Lookup",error_code=error)


#App route to NeoWs Feed for better+cleaner intergration
@app.route('/NeoWs_Feed', methods=['POST'])
def NeoWS_Feed():
    # Fetch the NeoWs feed data and params
    start=request.form.get('start')
    end=request.form.get('end')
    NeoWs_feed_data = N.NeoWs_Feed(start,end)
    """ The if else loop is an error handling statement. 
    It checks that the NeoWS data is in fact valid before continuing with the code. Otherwise it takes you to the error page.
    """
    if NeoWs_feed_data is not None:
        #Creating the dataframe and dropping unessary parts of the data.
        Neo_data=NeoWs_feed_data['near_earth_objects']
        df = pd.DataFrame(columns = ["ID", "Name","Absolute Magnitude", "Estimated Diameter (Meters)", "Is it potentially hazardous","Velocity (Km/h)","Miss distance (Km)","Close Approach Date"])
        current_date=datetime.datetime.strptime(start, '%Y-%m-%d').date()
        simple_date = start
        j=0
        """The data is looped through with all of the vaules being set for all of the data in the date. 
        Once it is complete the program moves onto the next date by adding a day to the previous time (this is initally set to the start date).
        """
        while simple_date <= end:
            for near in Neo_data[simple_date]:
                dia = near['estimated_diameter']
                average_dia = dia['meters']['estimated_diameter_min'] + dia['meters']['estimated_diameter_max'] / 2
                j+=1
                df.loc[j, 'ID'] = near['id']
                df.loc[j, 'Name'] = near['name']
                df.loc[j, 'Absolute Magnitude'] = near['absolute_magnitude_h']
                df.loc[j, 'Estimated Diameter (Meters)'] = average_dia
                df.loc[j, 'Is it potentially hazardous'] = near['is_potentially_hazardous_asteroid']
                close_data=near['close_approach_data']
                df.loc[j, 'Velocity (Km/h)'] = close_data[0]['relative_velocity']['kilometers_per_hour']
                df.loc[j, 'Miss distance (Km)'] = close_data[0]['miss_distance']['kilometers']
                df.loc[j, 'Close Approach Date']= close_data[0]['close_approach_date_full']
            # Converting back and forth from strings to add a day to loop through all the next day's data.
            current_date += timedelta(days=1)
            simple_date = current_date.strftime("%Y-%m-%d")
        print(df)
        final_df=df
        # Drop all of the columns from the previous df that are not needed.
        final_df=final_df.drop(['ID', 'Name','Absolute Magnitude', 'Estimated Diameter (Meters)', 'Is it potentially hazardous','Velocity (Km/h)','Miss distance (Km)'],axis=1)
        i=0
        # Drop the timestamp in close approach date to prepare for matplotlib plotting.
        for vaule in final_df['Close Approach Date']:
            i+=1
            vaule=vaule.split(" ")
            final_df.loc[i,'Close Approach Date']=vaule[0]
        # Plot the vaules to a matplotlib chart 
        print(final_df['Close Approach Date'].value_counts().sort_index())
        final_df['Close Approach Date'].value_counts().sort_index().plot.bar()
        plt.ylabel("Asteroids per Day")
        plt.xlabel("Timestamp")
        plt.xticks(rotation=0)
        plt.title("Occurence of Asteroids over the last days")
        # Saves plot to a file in static (flask checks here )
        plt.savefig('Static\images\data\data.webp')
        # Save params, type and date to history.
        f = open("history/history.txt", "a")
        local_date_=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"NeoWs Feed,{start} {end},{local_date_}\n")
        f.close()
        return render_template('NeoWs_feed.html',tables=[df.to_html(classes='data')],start=start,end=end)
    else:
        # Way to pass the error back to the program  without recoding the if statement and nasa api module.
        f = open("history/error.txt", "r")
        error=f.read()
        return render_template('error.html',Type="NeoWS Feed",error_code=error)
# Param selection App route
@app.route('/param',methods=['POST'])
def param_selection():
    Api_choice=request.form.get('API_Selection')
    return render_template('param_select.html',API_choice=Api_choice,today=date_)


#The reason why all of the API fetching is seperate is because it allows the program to be cleaner and more organised. 
#It makes the code more readable and allows the HTML to be simpler and more basic. I put everything into seperate html files to keep it readable.

# The main loop! Debug is left on as the App is not being deployed and none of the data is particularly sensitive. 
if __name__ == '__main__':
    app.run(debug=True)
    