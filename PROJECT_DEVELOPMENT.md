# Software-Assesment-Task-1
## Data Science Assement Task

## Design 

#### Task Definiton:Objective

To enable users to view Astornomy Picture of the day and query Near Earth Object Web Service. The program aims to give users infomation about space and in particular astroids. It caters to those with an intreast about space and who are wanting to learn more.

### Functional Requirements (What the system should do)
- Users must be able to retrive data that is displayed in a logical and simple way in the user interface.
- Users should be able to request  Astornomy Picture of the day and/or Near Earth Object Web Servics. It would allow users to see the all of the astoroids in a table with a the results of each, the size  and  and a graph for the number of notificaitions a day 
- Users should be able to see the history of the requests made with the program.
- The app should allow users to look for specific data using an API. 
-
### Non functional requirements
- The system should be responsive and complete all actions within 2 seconds
- The system should be availble 98% of the time.
- It needs to be intuative and simple to navigate to a basic internet user 
- It should detect user errors such as
spelling or unexpected inputs. It should account for the use of upper- and lower-case characters. It
should handle errors and excepeptions gracefully and prevent run-time errors.
- The system should work on a wide variety of windows devices.
### Specificaitions
#### Functional Specifications
The user needs to able enter diffrent parameters to adjust the results of the program.

The sytem needs to be able to accept user inputs and will need to display infomation from the NASA API in a logical way through a GUI. This will include graphs, images, text and tables.

At the program's core it needs to Astrony picture of the day (APOD)data and be able to view Astroids that are close to earth with the NeoWs data. 
The program should allow users to navigate between their results by using a simple GUI.


The user will interact with the program with a flask GUI and the readme will provide all of the . The GUI will be easy to navigate for all users.

I will list the potential errors that users may run 
into and given them solutions in the readme file.The 
errors will be displayed in the terminal and on the 
website in a concise and clear way. The program will 
be reliable and shouldn't run into any errors due to 
extensive testing and debuggingthat are not in the 
readme.
#### Non-functional Specificaitons

Performance


The system needs to be as efficent as possible, I'm aiming that all pages/program parts load under 5 seconds. Users want fast websites and we need to keep the GUI as fast as possible. We can ensure that the program remains fast by optimising our code and removing unnesary parts. 

Useability / Accessibility

The user interface will designed to be "idiot proof" 
and is relatively simple for anyone to operate.
It won't require much coding knowledge and the 
README keeps it simple and explains install and run 
the program. It also explains the purpose of the 
program. The read me will be clear and gives the users all the knowledge they need to use the program.

Reliability

I will list the potential errors that users may run 
into and given them solutions in the readme file.The 
errors will be displayed in the terminal and on the 
website in a concise and clear way. The program will 
be reliable and shouldn't run into any errors due to 
extensive testing and debuggingthat are not in the 
readme.

### Use cases

Actor: User

Preconditions: Internet acess, Python installed, NASA API is available

Main flow:
1. **Program begining** - User downloads the program requirements and follows the steps to run the program and open the website 
2.  **Infomation selction** -  User selects the type of data they would like to view.
3. **Parameter slection** - If applicable the user selects/types in the parameter that would like to search the API dataset for.   
4.**Data Visualstion** System retrives and displays data. Could display images,tables, graphs or text based on the selection 
5. **Histoy update** Save the current users history in case they want to acess it. 
Postconditions: API data is retrieved, the history of the current data is temporaily saved and the infomation is displayed to the user. . 
Postconditions: API data is selected and retrieved, and stored/removed successfully.

Usecase diagram?
TBD

### Gantt Chart
![](Static\images\Gantt-chart.jpeg)

### Structure Chart 
![](Static\images\Structure-chart.png)
### Algorithms

Psudeocode
```
BEGIN main()
    choice = 0
    WHILE choice is not 4
        INPUT choice
        IF choice is 1 THEN
            Api Request
            IF API Request Valid THEN
                APOD
            ELSE
                DISPLAY 'Error, API request has failed'
            ENDIF
        ELIF choice is 1 THEN
            Api Request
            IF API Request Valid THEN
                APOD
            ELSE
                DISPLAY 'Error, API request has failed'
            ENDIF
        ELSEIF choice is 3 THEN
            History
        ELSE
            DISPLAY 'Error, unknown inpit'
        ENDIF
    ENDWHILE
END main()    
```
Flowchart
 
![](Static\images\flowchart.jpeg)
 
### Data Dictionary 
| Variable | Data Type |Format for Display|Size in bytes|Size for display|Description|Example| Validation|Default*|
| -------- | --------- | -----------------|------------ | -------------- | --------- |-------|---------- |--------|
|Date (APOD)|International Date Time|YYYY-MM-DD | 4 bytes| 10 bytes| The date for Astronomy picture of the day. | 2025/02/11|Must be a valid year in international date time in the correct format.|today|
|Start Date (NeoWs)|International Date Time|YYYY-MM-DD| 4 bytes| 10 bytes|The start date for the NeoWS query |2025/02/11|Must be a valid year in international date time in the correct format.|N/A|
|End Date (NeoWs)|International Date Time|YYYY-MM-DD| 4 bytes| 10 bytes|The end date for the NeoWS query|2025/02/11|Must be a valid year in international date time in the correct format. It also must be after Start Date (NeoWs) |7 days after Start Date (NeoWs)|
|Asteroid Id| Int       |  NNNNN   | 2 bytes|3 bytes|The identification for an Astroid in the NeoWs system|3542519|Must be a valid astroid id that is recognised by the NeoWs system|N/A|
|API Key    | string    | xxxxxxxxxxxxxxxxxx | 15 bytes| 15 bytes|The Nasa API key to validate the requests| f79dEOc4JG9**|Must be a valid NASA API key|DEMO_KEY|
 
*If applicable. If the varible doesn't have a default then N/A will be put into the column.

**Length and combination of characters can change.

> **_NOTE:_**
The Table content wraps and is laid out weird because of the amount of content when viewing the source code.
 
## Development
#### App.py
```python
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
    return render_template('apod.html',url=image_url,info=descripion)
# App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs_Lookup',methods=['POST'])
def NeoWS_Lookup():
    # ADD function calling the API dtaa and then sort it using pandas and visualise any graphs or data.
    return render_template('NeoWs_look_up.html',info=descripion)
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


""" The reason why all of the API fetching is seperate is because it allows the program to be cleaner and more organised. 
It makes the code more readable and allows the HTML to be simpler and more basic.
"""

if __name__ == '__main__':
    app.run(debug=True)
    
```
#### Nasa_API_module.py
```python
import requests
import datetime
import pandas
import time
API_KEY = "b9Df79dEOc4JG9m3nfKxBpK9REKk8uuAENIxKcKc"
# Here we have the fetching of the APOD data
def APOD(date):
    params={"api_key": API_KEY,}
    APOD_URL = "https://api.nasa.gov/planetary/apod"
    response = requests.get(APOD_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 429:
        print(f"The API key can make{response.headers['X-RateLimit-Remaining']} more requess")
        print(f"The server has been requested too many times. The program will resume in {response.headers['Retry-After']} seconds")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(APOD_URL, param=params)
            data = response.json()
            return data
        except:
            print("Failed to fetch APOD. The server responded with the status code of "+str(response.status_code)) 
            return None
    else:
        print("Failed to fetch APOD. The server responded with the status code of "+str(response.status_code)) 
        return None
# Here we have the fetching of the NeoWs Feed data
def NeoWs_Feed(startdate,enddate):
    NeoWs_Feed_URL = "https://api.nasa.gov/neo/rest/v1/feed" 
    params={"api_key": API_KEY, "start_date":startdate,"end_date":enddate}
    response = requests.get(NeoWs_Feed_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 429:
        print(f"The API key can make{response.headers['X-RateLimit-Remaining']} more requess")
        print(f"The server has been requested too many times. The program will resume in {response.headers['Retry-After']} seconds")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(NeoWs_Feed_URL, params=params)
            data = response.json()
            return data
        except:
            print("Failed to fetch NeoWs Feed. The server responded with the status code of "+str(response.status_code))  
            return None
    else:
        print("Failed to fetch NeoWs Feed. The server responded with the status code of "+str(response.status_code))  
        return None
# Here we have the fetching of the NeoWs lookup data    
def NeoWs_lookup(astroid_id):
    NeoWs_lookup_URL = f"https://api.nasa.gov/neo/rest/v1/neo/{astroid_id}" 
    params={"api_key": API_KEY}
    response = requests.get(NeoWs_lookup_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 429:
        print(f"The API key can make{response.headers['X-RateLimit-Remaining']} more requess")
        print(f"The server has been requested too many times. The program will resume in {response.headers['Retry-After']}")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(NeoWs_lookup_URL, params=params)
            data = response.json()
            return data
        except:
            print("Failed to fetch NeoWs lookup. The server responded with the status code of "+str(response.status_code)) 
            return None

    else:
        print("Failed to fetch NeoWs lookup. The server responded with the status code of "+str(response.status_code)) 
        return None
```


## Intergration
#### Nasa_API_module.py
```python
import requests
import time
API_KEY='6lXf2VMVjbgJvxD2ShduRpGqSWQwWnBpiHtsiE9T'
# Here we have the fetching of the APOD data
def APOD(date):
    params={"api_key": API_KEY,'date': date}
    APOD_URL = "https://api.nasa.gov/planetary/apod"
    # Fetch the API data using requests
    response = requests.get(APOD_URL, params=params)
    # Check that the repsonse is valid before returning the data 
    if response.status_code == 200:
        data = response.json()
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
        return data  
    # Error handling if the API key has reached it's limit 
    elif response.status_code == 429:
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
        print(f"The server has been requested too many times. The program will resume in {response.headers['Retry-After']} seconds")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(APOD_URL, param=params)
            data = response.json()
            return data
        # Error handling that writes the error to a txt file. 
        except:
            print("Failed to fetch APOD. The server responded with the status code of "+str(response.status_code)) 
            f = open("history/error.txt", "w")
            f.write(str(response.status_code))
            f.close() 
            return None
    # Error handling that writes the error to a txt file. 
    else:
        print("Failed to fetch APOD. The server responded with the status code of "+str(response.status_code))
        f = open("history/error.txt", "w")
        f.write(str(response.status_code))
        f.close()  
        return None
# Here we have the fetching of the NeoWs Feed data
def NeoWs_Feed(startdate,enddate):
    NeoWs_Feed_URL = "https://api.nasa.gov/neo/rest/v1/feed" 
    params={"api_key": API_KEY, "start_date":startdate,"end_date":enddate}
    response = requests.get(NeoWs_Feed_URL, params=params)
    # Check that the repsonse is valid before returning the data 
    if response.status_code == 200:
        data = response.json()
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
        return data
    # Error handling if the API key has reached it's limit 
    elif response.status_code == 429:
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
        print(f"The server has been requested too many times. The program will resume in {response.headers['Retry-After']} seconds")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(NeoWs_Feed_URL, params=params)
            data = response.json()
            return data
        # Error handling that writes the error to a txt file. 
        except:
            print("Failed to fetch NeoWs Feed. The server responded with the status code of "+str(response.status_code))
            f = open("history/error.txt", "w")
            f.write(str(response.status_code))
            f.close()
            return None
    # Error handling that writes the error to a txt file. 
    else:
        print("Failed to fetch NeoWs Feed. The server responded with the status code of "+str(response.status_code)) 
        f = open("history/error.txt", "w")
        f.write(str(response.status_code))
        f.close() 
        return None

# Here we have the fetching of the NeoWs lookup data    
def NeoWs_lookup(astroid_id):
    NeoWs_lookup_URL = f"https://api.nasa.gov/neo/rest/v1/neo/{astroid_id}" 
    params={"api_key": API_KEY}
    response = requests.get(NeoWs_lookup_URL, params=params)
    # Check that the repsonse is valid before returning the data 
    if response.status_code == 200:
        data = response.json()
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
        return data
    # Error handling if the API key has reached it's limit 
    elif response.status_code == 429:
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
        print(f"The server has been requested too many times. The program will resume in {response.headers['Retry-After']}")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(NeoWs_lookup_URL, params=params)
            data = response.json()
            return data
        # Error handling that writes the error to a txt file. 
        except:
            print("Failed to fetch NeoWs lookup. The server responded with the status code of "+str(response.status_code))
            f = open("history/error.txt", "w")
            f.write(str(response.status_code))
            f.close() 
            return None
    # Error handling that writes the error to a txt file. 
    else:
        print("Failed to fetch NeoWs lookup. The server responded with the status code of "+str(response.status_code))
        f = open("history/error.txt", "w")
        f.write(str(response.status_code))
        f.close() 
        return None
```
#### ap.py

```python
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
        # Go through all of the rows and split the vaules by commas.
        for x in f:
            x=x.split(",")
            i+=1
            history_df.loc[i,'API type'] = x[0]
            history_df.loc[i,'API parameters'] = x[1]
            # This line is special as it has to remove the /n that is put in by the program to wrap them propely
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
    if NeoWs_lookup_data is not None:
        Neo_data=NeoWs_lookup_data
        df = pd.DataFrame(columns=["Close Approach Date","Miss distance (Km)","Velocity in Km/h"])
        # Set some of the vaules that don't change because of reoccurences. 
        dia = Neo_data['estimated_diameter']
        average_dia = dia['meters']['estimated_diameter_min'] + dia['meters']['estimated_diameter_max'] / 2
        Id= Neo_data['id']
        name= Neo_data['name']
        is_hazardous = Neo_data['is_potentially_hazardous_asteroid']
        Absolute_magnitude=Neo_data['absolute_magnitude_h']
        i=0
        for close_data in Neo_data['close_approach_data']:
            # Loop through all of the data and append it to a df 
            i+=1
            df.loc[i, 'Velocity in Km/h'] = close_data['relative_velocity']['kilometers_per_hour']
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
        # Way to pass the error back to the program  without recoding the if statement and nasa api module.
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
    if NeoWs_feed_data is not None:
        # Creting the dataframe and dropping unessary parts of the data.
        Neo_data=NeoWs_feed_data['near_earth_objects']
        df = pd.DataFrame(columns = ["ID", "Name","Abosulute_Magintude", "Estimated Diameter", "Is it potentially hazardous","Velocity in Km/h","Miss distance","Close Approach Date"])
        current_date=datetime.datetime.strptime(start, '%Y-%m-%d').date()
        simple_date = start
        j=0
        while simple_date <= end:
            for near in Neo_data[simple_date]:
                # The data is looped through with all of the vaules being set for all of the data in the date. 
                # Once it is complete the program moves onto the next date
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
            # Converting back and forth from strings to add a day to loop through all the next day's data.
            current_date += timedelta(days=1)
            simple_date = current_date.strftime("%Y-%m-%d")
        print(df)
        final_df=df
        # Drop all of the columns from the previous df that are not needed.
        final_df=final_df.drop(['ID', 'Name','Abosulute_Magintude', 'Estimated Diameter', 'Is it potentially hazardous','Velocity in Km/h','Miss distance'],axis=1)
        i=0
        # Drop the timestamp in close approach date to prepare for matplotlib plotting.
        for vaule in final_df['Close Approach Date']:
            i+=1
            vaule=vaule.split(" ")
            final_df.loc[i,'Close Approach Date']=vaule[0]
        # Plot the vaules to a matplotlib chart 
        final_df['Close Approach Date'].value_counts().sort_index().plot(kind="bar")
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


""" The reason why all of the API fetching is seperate is because it allows the program to be cleaner and more organised. 
It makes the code more readable and allows the HTML to be simpler and more basic. I put everything into seperate html files to keep it readable.
"""
# The main loop! Debug is left on as the App is not being deployed and none of the data is particularly sensitive. 
if __name__ == '__main__':
    app.run(debug=True)
```






Installation
You're on the home stretch! Your program works and you just need to finish up a little documentation to make sure people can use it!

For installation, all we're going to include in this project is a requirements.txt file to assist users in installing dependencies and a README.md file to give users instructions necessary to run our software.

PROJECT_DEVELOPMENT.md
Add a code block for each of these files into your project documentation and add under the heading Installation. 



## Testing and Debugging

Peer review 1:



Peer reciew 2:


# Maintence 
Maintenance
Almost there! We now just need to answer the following questions.

Maintenance Questions
Explain how you would handle issues caused by changes to the weather API over time.

Explain how you would ensure the program remains compatible with new versions of Python and libraries like requests and matplotlib.

Describe the steps you would take to fix a bug found in the program after deployment.

Outline how you would maintain clear documentation and ensure the program remains easy to update in the future.

Describe
Provide characteristics and features.

Explain:
Relate cause and effect.

Make the relationships between things evident.

Provide why and/or how.

Outline 
Sketch in general terms; indicate the main features of.

### Final Evaluation
Evaluate the current functionality of the program in terms of how well it addresses the functional and non-functional requirements.

Discuss areas for improvement or new features that could be added.

Evaluate how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.

Discuss
Identify issues and provide points for and/or against.

Evaluate
Make a judgement based on criteria.

Determine the value of.