# Software-Assessment-Task-1
## Data Science Assessment Task
## Demonstration of completed program
<video width="1000" controls>
  <source src="Demonstration.mp4" type="video/mp4">
</video>


### Task Definition:Objective


The objective of my program is to enable users to view NASA data (https://api.nasa.gov/), allowing easier access to space data and allowing space enthusiasts to interact with the wide variety of data supplied. My program allows users to see the Astronomy Picture of the day (APOD) and query Near Earth Object Web Service(NeoWs). The APOD is a fun snapshot that highlights the breathtaking astronomy photography of others which highlights an astronomical idea or event and it builds public interest in space. NeoWs gives real time extensive data about the hundreds of objects that wizz past our earth every week. The program aims to give users information about space and in particular asteroids. It caters to those with an interest in space and who are wanting to learn more.


### Functional Requirements (What the system should do)


- Users must be able to request an Astronomy Picture of the day and/or Near Earth Object Web Service. It would allow users to see the all of the asteroids in a table with a the results of each, the size  and  and a graph for the number of notifications a day
- Users must be able to see the history of the requests made with the program
- Users must be able to retrieve NASA data that is displayed in a logical and simple way in the user interface.
- The app must allow users to look for specific data using the program.


### Non functional requirements
- The system should be responsive and complete all actions within 5 seconds.
- The system should be available 98% of the time.
- It needs to be intuitive and simple to navigate to a basic internet user.
- It should detect user errors such as spelling or unexpected inputs or not allow user errors in the first place. It should account for the use of upper- and lower-case characters. It should handle errors and exceptions gracefully and prevent run-time errors.
- The system should work on a wide variety of Windows devices.
## Specifications
### Functional Specifications
### User Requirements
- The user needs to be able enter different parameters to adjust the results of the program.
- Users need to be able to request Astronomy Picture of the day and Near Earth Object Web Service.
- Users need to be able to see the history of the requests made with the program and be able to clear their history.
### Inputs & Outputs
- The system needs to be able to accept user inputs and will need to display information from the NASA API in a logical way through a GUI. This will include graphs, images, text and tables.
### Core Features
- At the program's core it needs Astronomy picture of the day (APOD) data, search for all instances of a specific asteroid with the NeoWs lookup data  and be able to view Asteroids that have recently been closed to Earth with the NeoWs Feed data.
- The program must be able to display all of this data to the user.


### User Interaction
- The user will interact with the program with a flask GUI and the readme will provide all of the information that users need to install and use the program. The GUI will be easy to navigate for all users and include detailed explanations for what the data is and how to use it in specific pages of the website that you are guided to by link if the user is unsure on how to use the program or wants to understand the point of the program.




### Error Handling
- I will list the potential errors that users may run into and give them solutions in the readme file. The errors will be displayed in the terminal and on the website in a concise and clear way. The program will be reliable and shouldn't run into any errors that are not in the readme. I will ensure this by using extensive testing and debugging of all potential inputs.
### Non-functional Specifications
### Performance
- The system needs to be as efficient as possible, I'm aiming that all pages/program parts load under 5 seconds. Users want fast websites and we need to keep the GUI as fast as possible. We can ensure that the program remains fast by optimising our code and removing unnecessary parts.


### Useability / Accessibility
- The user interface is designed to be "idiot proof" and is relatively simple for anyone to operate. It will include information pages to explain how the API and program works and the program's purpose.
The README will be concise, clear and give users all the knowledge they need to use the program.




### Reliability
- API retrieval problems will be solved to the best of my ability. The data integrity is well maintained and is unlikely to fall in quality as it is maintained by a reputable government agency. Furthermore the program will be accurate and have proper error handling if the data is not returned correctly.
## Use Case
Actor: User


Preconditions: Internet access, Python installed, NASA API is available.
Main flow:
1. **Program beginning** - User downloads the program's requirements and follows the steps to run the program in the readme and opens the website
2.  **Information selection** -  User selects the type of API data they would like to view.
3. **Parameter selection** - The user selects/types in the parameter that would like to search the API dataset for.  
4. **Data Visualisation** System retrieves and displays the API data. Could display images, tables, graphs or text based on the selection.
5. **History update** Save the current user's history for display and fetching later.


Postconditions: API data is retrieved, the history of the current data is temporarily saved and the information is displayed to the user.
Postconditions: API data is selected and retrieved, and stored/removed successfully.


## Design
### Gantt Chart
<img src="Static\images\Gantt-chart.jpeg"  width="1000"/>


### Structure Chart
<img src="Static\images\Structure_chart.png"  width="500"/>


### Algorithms


### Main Flow Pseudocode
```
BEGIN main()
    WHILE Program is running
        INPUT sublink
        IF Sublink = "/about_page" THEN
            About
        ELIF Sublink = "/help_page" THEN
            Help
        ELIF Sublink = "/history_page" THEN
            History
        ELSE
            Home
        ENDIF
    ENDWHILE
END main()    
```
### Main Flow Flowchart


<img src="Static\images\main_flowchart.png"  width="500"/>




### Home Pseudocode


```
BEGIN Home()
    OUTPUT Home
    INPUT API Choice
    IF API Choice = NeoWS feed THEN
        Parameter Selection
        NeoWs Feed
    ELIF API Choice = NeoWs Lookup THEN
        Parameter Selection
        NeoWs Lookup
    ELSE
        Parameter Selection
        Home
    ENDIF
END Home()
```
### Home flowchart
<img src="Static\images\home_flowchart.png"  width="500"/>


### Parameter selection Pseudocode
```
BEGIN Parameter Selection()
    OUTPUT Parameter Selection
    Fetch API Choice
    IF API Choice = NeoWS feed THEN
        INPUT NeoWs Feed Start and End date
    ELIF API Choice = NeoWs Lookup THEN
        INPUT NeoWs Asteroid ID  
    ELSE
        INPUT APOD Date
    ENDIF
END Parameter Selection()    
```
### Parameter selection Flowchart
<img src="Static\images\param_flowchart.png"  width="500"/>


### NeoWs feed pseudocode


```
BEGIN NeoWs Feed()
    Fetch NeoWs Feed Start and End date
    IF API Request Valid THEN
        Sort Data
        Save Matplotlib Graph
        OUTPUT NeoWs Feed
    ELSE
        Error
    ENDIF
END NeoWs Feed()    
```
### NeoWs feed flow chart


<img src="Static\images\Neows_feed_flowchart.png"  width="500"/>

### Data Dictionary
#### Please scroll to the right to see all of the infomation.
| Variable | Data Type |Format for Display|Size in bytes|Size for display|Description|Example    | Validation|Default*|
| -------- | --------- | -----------------|------------ | -------------- | --------- |------------------------|---------- |--------|
|Date (APOD)|International Date Time|YYYY-MM-DD | 4 bytes| 10 bytes| The date for the Astronomy picture of the day. | 2025/02/11|Must be a valid year in international date time in the correct format.|Today|
|Start Date (NeoWs)|International Date Time|YYYY-MM-DD| 4 bytes| 10 bytes|The start date for the NeoWS query |2025/02/11|Must be a valid year in international date time in the correct format.|N/A|
|End Date (NeoWs)|International Date Time|YYYY-MM-DD| 4 bytes| 10 bytes|The end date for the NeoWS query|2025/02/11|Must be a valid year in international date time in the correct format. It also must be after Start Date (NeoWs) |N/A|
|Asteroid Id| Int       |  NNNNN**   | 2 bytes|3 bytes|The identification for an Asteroid in the NeoWs system|3542519|Must be a valid astroid id that is recognised by the NeoWs system|N/A|
|API Key    | String    | xxxxxxxxxxxxxxxxxx**| 15 bytes**| 15 bytes**|The Nasa API key to validate the requests| f79dEOc4JG9|Must be a valid NASA API key|N/A|
|Title (APOD)|String|xxxxxxxxxxxxxxxxxx**|15 bytes**|15 bytes**|The Astronomy picture of the day title|The Gargoyles' Eclipse|Must be the title of the Astronomy picture of the day| N/A|
|Date (APOD)|International Date Time|YYYY-MM-DD | 4 bytes| 10 bytes| The date that the API returns for Astronomy picture of the day. | 2025/02/11|Must be a valid year that matches the API result in the correct format. | N/A|
|Image/Video Url (APOD)|String (technically)|xxxxxxxxxxxxxxxxxx**|15 bytes**|15 bytes**|The URL returned for the APOD Image or video of the day|https://apod.nasa.gov/apod/image/2504/AldrinSeismometer_Apollo11_3000.jpg|Must be a valid url to youtbe embed or APOD |N/A|
|Description (APOD)| String|xxxxxxxxxxxxxxxxxx**|15 bytes**|15 bytes**|The description that the APOD API returns that explains or gives context to the image.|Comet C/2023 A3 (Tsuchinshan–ATLAS) is growing brighter in planet Earth's sky. Fondly known as comet A3, this new visitor to the inner Solar System is traveling from the distant Oort cloud. The comet reached perihelion, its closest approach to the Sun, on September 27 and will reach perigee, its closest to our fair planet, on October 12, by then becoming an evening sky apparition.****|Must be a valid string returned by the NASA APOD API that matches.|N/A|
|Asteroid Id (NeoWs Feed)| Int  |  NNNNN**   | 2 bytes|3 bytes|The identification for an Asteroid in the NeoWs system|3542519|Must be a valid astroid id that is recognised by the NeoWs system|N/A|
| Asteroid Name (NeoWs Feed)|String|xxxxxxxxxxxxxxxxxx**|15 bytes**|15 bytes**|The name for the asteroid returned by the API|(2004 FC18)|Must be a valid string returned by the NASA NeoWs API that matches.|N/A|
|Absolute Magnitude (NeoWs Feed)| Float  |  NNNNN.NN**   | 4 bytes|4 bytes|The absoulte magintude for a NeoWs asteroid|	24.43|Must be the Abosolute maginitude response for the asteroid by the API|N/A|
|Estimated Diameter (NeoWs)| Float  |  NNNNN.NN**   | 4 bytes|4 bytes|The identification for an Asteroid in the NeoWs system|21.403653|The division of the valid NASA min and max diameter in the NeoWs API response|N/A|
|Is it potentially hazardous(NeoWS)|Boolean*** |xxxx|1byte***| 4 bytes***| If the asteroid could be potentially hazardous to Earth|True|Must be the NASA response for the potentially hazadous field in NeoWs|N/A|
|Velocity (NeoWs)| Float |  NNNNN.NN**   | 4 bytes|4 bytes|The identification for an Asteroid in the NeoWs system|3542519|Must be the NASA reponse for the velocity in KM field in NeoWs  |N/A|
|Miss distance (NeoWS)| Float |  NNNNN.NN**   | 4 bytes|4 bytes|The miss distance in Km for an Asteroid returned by the NeoWs API|354322.519|Must be the NASA response for the miss distance in KM field in NeoWs |N/A
|Close Approach Date(NeoWs)|String|YYYY-XXX-DD hh:mm| 16 bytes| 16 bytes| The date when the asteroid is closest to Earth that the API returns for a specific asteroid or date of an id of an asteroid. | 2025-Apr-04 00:04|Must be a valid date that matches the API result in the correct format. | N/A|
|


 
*If applicable. If the variable doesn't have a default then N/A will be put into the column.


**Length and combination of characters can change.


*** In python a boolean is technically an Int. Furthermore, despite that a boolean should be 1 bit, most program languages treat it as 8 bits or a byte for consistency in the program. For the sake of simplicity for display it's going to be treated as a 4 long byte string and treated as a Bolean with 1 byte being the computation size as most programming languages treat it.

**** Shortened example

> **_NOTE:_**
The table includes both API parameters and API results and has some overlap between the two. There is also overlap with both the NeoWs and I will only do them once if they return them. The above statements describe some of the important information about the * content. Furthermore the Table content wraps and is laid out weirdly because of the amount of content when viewing the source code of the markdown file.


 
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
    # ADD function calling the API data and then sort it using pandas and visualise any graphs or data.
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
    
```
## Installation


#### README.md
```md
# Software-Assessment-Task-1
### Data Science Assessment Task: Solar Sonar
## Objective
The objective of my program is to enable users to view NASA data, allowing easier access to space data and allowing space enthusiasts to interact with the wide variety of data supplied. My program allows users to see the Astronomy Picture of the day (APOD) and query Near Earth Object Web Service(NeoWs). The APOD is a fun snapshot that highlights the breathtaking astronomy photography of others which highlights an astronomical idea or event and it builds public interest in space. Neows gives real time extensive data about the hundreds of objects that wizz past our earth every week. The program aims to give users information about space and in particular asteroids. It caters to those with an interest in space and who are wanting to learn more.


## Features
- Users can request  Astronomy Picture of the day and Near Earth Object Web Service.
- Display NASA data with a combination of graphs, tables, text and images.
- Users are able to retrieve data that is displayed in a logical and simple way in the user interface.
- Users can see the history of the requests made with the program and can clear their history .
- The app allows users to look for specific data using an API.


## Requirements
To run this program you need the following python import libraries.
- Flask


Flask is a web framework that runs on python. It is powering the GUI in my project.
- Requests


Requests allows you to make HTTP requests to websites. I use it to fetch and retrieve my NASA data.
- Pandas


Pandas allows you to create, delete and edit data frames for data analysis and manipulation. Panda is used in my project to sort and edit the data.
- Datetime


A python library that allows you to work with date and time. Datetime is used to work with the date and time parameters that exist within my program.
- Matplotlib


A visualization python library that allows you to make graphs and other visualizations.  It's used to plot the graph that shows the asteroid count per day that is returned when fetching NeWs feed. The program is
- Pytz


A python library that allows you to receive different timezone information. Pytz is critical as it allows me to avoid errors by trying to access the NASA information before it is published.


** os isn't included as it comes preinstalled with python.


## How to use the program
1. Firstly if you are reading this on github you will need to open it in a suitable IDE with python 3.11 or higher installed.
2. Simply click the download button or alternatively use github desktop to open it.


3. Next navigate to python's terminal in your IDE and run the following command.

pip install -r requirements.txt

*Optional* If an upgrade pip prompt appears in your terminal, I heavily recommend you update it by copy and pasting the command there.


4. Click the run button in your preferred IDE (In App.py) and then give the program a second.


5. Follow the terminal instructions and open the link. (Shown below)


6. The program is running and you can navigate around the GUI. Infomation on how to understand the parameters and API responses are in the Help page. Further infomation about the diffrent NASA data and a reiteration of the programs focus are found on the About page.

7. Once you are finished click into the terminal and then press Ctrl+C at the same time and wait for the errors to stop. Once they finish the locally hosted website has closed. Please note that your history will be saved locally, if you want to clear it after the GUI you can simply delete history.txt's contents. However do not delete the file itself.

## Demonstation of the program.
<video width="320" height="240" controls>
  <source src="Demonstration.mp4" type="video/mp4">
</video>

## Common Errors and Solutions
- Error: Can't select today in the date paramters for APOD or NeoWs?
    - Solution: The NASA dataset is updated by the american timezone date and therefore cannot display the data for the current date in places like Australia. The limitations on the date params  are set to the american timezone and are hardcoded in to prevent errors.
- Error: Reaches the API key's rate limit really quickly on the certain WIFI configurations (School WIFI).
    - Solution: Unfortunately I was unable to find one. I did implement a special error handling due to this issue by delaying until the API key can reassess. However sometimes you can get away with just breaking the current run instance by using CTR + C and then rerunning the program.
- Error: Selecting over 5 days will result in an error as the dataset breaks.
   - Solution: Keep NeWs feed under 5 days.
- Error: The NeoWS feed dataset breaks and returns nothing because in the parameters you put the end date before the start date.
   - Solution: Don't. Seriously, what did you think was going to happen?
- Error: The program returned the error page with the message. "Failed to fetch {{Type}}. The server responded with the status code of {{error_code}}."
    - Solution: Google the status code to understand the issue and  then check the terminal to see if the API key has reached the limit. Also check that all of the NASA API's  are functional and that your internet connection is functioning as expected.
```
#### requirements.txt
```
flask
requests
pandas
datetime
matplotlib
pytz
```

## Testing and Debugging cont.

### Commit History
<video width="1000" controls>
  <source src="Commit_History.mp4" type="video/mp4">
</video>

I used git to add infomation to one or two of my commits however it changed all of the commit history to be the date of last push. The above video shows the commit history with the old dates as github desktop has it for some reason.

### Peer reviews:
Peer review 1: Max

4/5

- Nice data in tables and graphs integrated into the website!
- It has comprehensive help and about pages for beginner users to understand how it works, could have been improved through showing help next to the data so you don't have to pull up 2 windows side-by-side to look up what the data means.
- It has a history for when you want to revisit previous data, but could have been improved by storing the entire request data so you can simulate a web request without having wifi to see all the graphs and charts in detail.
- Very detailed instructions on how to use the program for anyone to run it, even with a section on common errors!

Peer review 2 Will:

4.5/5

The program respons to errors in a consise and meaningful fasion allowing for users to understand where the error occured. The program has a very aesthetic and intuitive GUI that is easy to use. The program also records  all API uses to refer to at a later time which is extremely useful. The readme and infomation on the website is great making it easy to use for all users.

# Maintenance
### Explain how you would handle issues caused by changes to the API over time.




I would handle changes to the NASA API overtime by adapting my program and then updating the program on github with a new version and list the fixed bug changes in the version description. As I do not have control of other programs, I cannot use the standard implementation systems and must wait for them to update their version when the issue arises.


### Explain how you would ensure the program remains compatible with new versions of Python and libraries like requests and matplotlib.




The program deliberately uses features of the libraries that aren't going to be depreciated in the near future and are unlikely to be changed. If the issues were changed, I would either update the code and change the library function to a modern equivalent or change the requirements.txt import to be a specific version of the library.




### Describe the steps you would take to fix a bug found in the program after deployment.




I would first recreate the steps of the bug found and then look through the terminal. Next I would bug fix the program by using a mixture of unit and function testing and print statements to print each part of the code. I would then find a solution and confirm proper functionality of the program before commiting to github.
Finally, on github I would publish a new version and list the fixed bug changes in the version description. As I do not have control of other programs, I cannot use the standard implementation systems and must wait for them to update their version when the issue arises.


### Outline how you would maintain clear documentation and ensure the program remains easy to update in the future.


The documentation will be kept simple with step by step explanations and the in depth explanations evident on the website to guide new users. I would avoid maintenance heavy features and would update the program. By using proper coding practices I would continue to code in app functions which ensures readability and keeps the code clean. I would use peer testing to maintain clear documentation and make sure that all explanations make sense to my target audience. The above steps is how I would clearly ensure that my documentation is concise and clear and that the program remains easy to update in the future.


### Final Evaluation
### Evaluate the current functionality of the program in terms of how well it addresses the functional and non-functional requirements.
The functionality of the program successfully addresses all of the functional and nonfunctional requirements and completes them all to a high degree. My project can successfully fetch and sort the API data from APOD and NeoWs. I make sure that users can easily visualize the API data in a clear way and clearly. My GUI is intuitive to navigate and usually loads all of the pages in under 5 seconds. The program successfully handles errors and prevents most user errors such as mispelling or incorrect use of capitals. I successfully keep my program reliable and accessible by having clear documentation on the website and readme files that allows users to understand how to use the API. My program works with a wide range of windows devices. It's clear that my project successfully completes all of the functional and nonfunctional requirements.




### Discuss areas for improvement or new features that could be added.


I could incorporate more NASA API features to allow my users to gain a deeper understanding about Space and planets. I would first incorporate DONKI (Space Weather) as I originally had this in my plans however I had to drop it due to logistical and time reasons. I would also add the satellite images of earth as it builds our understanding of the planet. Furthermore I would add an offline mode that would fix the API rate limit problems with the school wifi.


### Evaluate how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.


The project was managed by clearly outlining the requirements. I also clearly stated my next steps in the development program and I made sure to stick as close as possible to my initial timeline.
I did lots of testing in this project by using print statements, using the flask debug terminal and simply running the program.I have faced a lot of bugs in this part of the program and I fixed them by incorporating the debugging strategies of function testing, debug statements and whole system testing. I also solved some of my problems with specific libraries/datasets with some help from the internet (mainly stack overflow).


# Thank you to
- Max and Oliver who helped with verbal problem solving.
- Pyguru who helped me understand NeoWs data and how to break it up.
https://www.youtube.com/watch?v=JNL71zQHe3Q
-  W3 schools for their css header which I modified to suit
https://www.w3schools.com/howto/howto_css_responsive_header.asp
- The Nasa Api Documentation.
https://api.nasa.gov/
- The hundreds of stack overflow forums I scoured for an answer to my specific problems.
https://stackoverflow.com/questions  

