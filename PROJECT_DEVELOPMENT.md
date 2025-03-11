# Software-Assesment-Task-1
## Data Science Assement Task

## Design 

#### Task Definiton:Objective

To enable users to view Astornomy Picture of the day, Near Earth Object Web Service and view Space Weather Database Of Notifications, Knowledge, Information (DONKI). The program aims to give users infomation about space. It caters to those with an intreast about space and who are wanting to learn more.

### Functional Requirements (What the system should do)
- Users must be able to retrive data that is displayed in a logical and simple way in the user interface.
- Users should be able to request  Astornomy Picture of the day, Near Earth Object Web Service and view Space Weather Database Of Notifications, Knowledge, Information (DONKI).
- Users should be able to see the history of the requests made with the program.
-Users must be able to 
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

The user needs to able enter diffrent parameter to adjust the results of the program. 


The sytem needs to be able to accept 

At its core the program needs to display infomation from the NASA API in a logical way through a GUI.
#### Functional Specifications

#### Non-functional Specificaitons

Performance

How quickly should we try to get the system to perform tasks, what efficiency is required to maintain user engagement? How can we ensure our program remains efficient?

Useability / Accessibility

How might you make your application more accessible? What could you do with the User Interface to improve usability?

Reliability

Reliability is important 

### Use cases

Actor: User

Preconditions: Internet acess, Python installed, NASA API is available

Main flow:
1. Program begining 
2.  **Infomation selction** -  User selects the type of data they would like to view.
3. **Parameter slection** - If applicable the user selects/types in the parameter that would like to search the API dataset for.   
4. System retrives and displays data. Could display images,
5. **Histoy update** Save the current users history in case they want to acess it. 
Postconditions: API data is retrieved, the history of the current data is temporaily saved and the infomation is displayed to the user. . 


Use case diagram 


Post Conditions

### Gantt Chart
![](Static\images\Gantt-chart.jpeg)

### Structure Chart 

### Algorithms

Psudeocode
```
 
```
Flowchart
 
![](Static\images\flowchart.jpeg)
 
### Data Dictionary 
| Variable | Data Type |Format for Display|Size in bytes|Size for display|Description|Example| Validation|
| -------- | --------- | -----------------|------------ | -------------- | --------- |-------|---------- |
 
 
 
 
## Development
Evaulation 
 
 
 
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

Final Evaluation
Evaluate the current functionality of the program in terms of how well it addresses the functional and non-functional requirements.

Discuss areas for improvement or new features that could be added.

Evaluate how the project was managed throughout its development and maintenance, including your time management and how challenges were addressed during the software development lifecycle.

Discuss
Identify issues and provide points for and/or against.

Evaluate
Make a judgement based on criteria.

Determine the value of.