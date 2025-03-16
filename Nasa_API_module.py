import requests
import datetime
import pandas
API_KEY = "DEMO_KEY"
def APOD():
    params={"api_key": API_KEY,}
    APOD_URL = "https://api.nasa.gov/planetary/apod"
    response = requests.get(APOD_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch APOD.") 
        return None
    
def NeoWs_Feed(startdate,enddate):
    APOD_URL = "https://api.nasa.gov/planetary/apod" 
    params={"api_key": API_KEY, "start_date":startdate,"end_date":enddate}
    response = requests.get(APOD_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch NeoWs Feed.") 
        return None
    
def NeoWs_lookup(astroid_id):
    
    NeoWs_lookup_URL = "https://api.nasa.gov/neo/rest/v1/neo/" 
    params={"api_key": API_KEY, "astroid_id":astroid_id}
    response = requests.get(NeoWs_lookup_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch NeoWs lookup.") 
        return None

def NeoWs_overview():
    NeoWs_lookup_URL = "https://api.nasa.gov/neo/rest/v1/neo/browse/" 
    params={"api_key": API_KEY}
    response = requests.get(NeoWs_lookup_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to fetch NeoWs Overview.") 
        return None
     
