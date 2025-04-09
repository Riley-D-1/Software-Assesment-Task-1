# Software-Assessment-Task-1
### Data Science Assessment Task: Solar Sonar
## Objective
The objective of my program is to enable users to view NASA data, allowing easier access to space data and allowing space enthusiasts to interact with the wide variety of data supplied. My program allows users to see the Astronomy Picture of the day (APOD) and query Near Earth Object Web Service(NeoWs). The APOD is a fun snapshot that highlights the breathtaking astronomy photography of others which highlights an astronomical idea or event and it builds public interest in space. NeoWs gives real time extensive data about the hundreds of objects that wizz past our earth every week. The program aims to give users information about space and in particular asteroids. It caters to those with an interest in space and who are wanting to learn more.


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
```
pip install -r requirements.txt
```
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
- Error: Selecting over 7 days in the NeoWs feed will result in an error as the dataset cannot be fetched.
   - Solution: Keep NeoWs feed under or equal to 7 days.
- Error: The NeoWS feed dataset breaks and returns nothing because in the parameters you put the end date before the start date.
   - Solution: Don't. Seriously, what did you think was going to happen?
- Error: The program returned the error page with the message. "Failed to fetch {{Type}}. The server responded with the status code of {{error_code}}."
    - Solution: Google the status code to understand the issue and  then check the terminal to see if the API key has reached the limit. Also check that all of the NASA API's  are functional and that your internet connection is functioning as expected.
    