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
app = Flask(__name__)
# Homepage route for better+cleaner intergration
@app.route('/')
def home_page():
    return render_template('index.html')
# App route to NeoWs for better+cleaner intergration
@app.route('/Apod')
def APOD():
    return render_template('apod.html',url="test")
# App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs_Lookup')
def NeoWS_Lookup():
    return render_template('NeoWs_look_up.html')
#App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs_Overview')
def NeoWS_Overview():
    return render_template('NeoWs_overview.html')
#App route to NeoWs for better+cleaner intergration
@app.route('/NeoWs_Feed')
def NeoWS_Feed():
    return render_template('NeoWs_feed.html')

""" The reason why there are 3 is because it allows the program to be cleaner and  
"""



if __name__ == '__main__':
    app.run(debug=True)
    
```
#### Nasa_API_module.py
```python
 
```


## Intergration
 
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