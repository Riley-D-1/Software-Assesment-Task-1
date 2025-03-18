import requests
import datetime
import pandas
import time
API_KEY = "b9Df79dEOc4JG9m3nfKxBpK9REKk8uuAENIxKcKc"
# Here we have the fetching of the APOD data
def APOD():
    params={"api_key": API_KEY,}
    APOD_URL = "https://api.nasa.gov/planetary/apod"
    response = requests.get(APOD_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 429:
        print(f"The API key can make{response.headers["X-RateLimit-Remaining"]} more requess")
        print(f"The server has been requested too many times. The program will resume in {response.headers["Retry-After"]} seconds")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(APOD_URL, params=params)
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
    response = requests.get(NeoWs_Feed, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 429:
        print(f"The API key can make{response.headers["X-RateLimit-Remaining"]} more requess")
        print(f"The server has been requested too many times. The program will resume in {response.headers["Retry-After"]} seconds")
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
        print(f"The API key can make{response.headers["X-RateLimit-Remaining"]} more requess")
        print(f"The server has been requested too many times. The program will resume in {response.headers["Retry-After"]} seconds")
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

# Here we have the fetching of the NeoWs overview data.

def NeoWs_overview():
    NeoWs_overview_URL = "https://api.nasa.gov/neo/rest/v1/neo/browse" 
    params={"api_key": API_KEY}
    response = requests.get(NeoWs_overview_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 429:
        print(f"The API key can make{response.headers["X-RateLimit-Remaining"]} more requess")
        print(f"The server has been requested too many times. The program will retry/resume in {response.headers["Retry-After"]} seconds")
        time.sleep(int(response.headers["Retry-After"]))
        try:
            response = requests.get(NeoWs_overview_URL, params=params)
            data = response.json()
            return data
        except:
            print("Failed to fetch NeoWs Overview. The server responded with the status code of "+str(response.status_code))  
            return None
    else:
        print("Failed to fetch NeoWs Overview. The server responded with the status code of "+str(response.status_code))  
        return None

#print(NeoWs_Feed("2025-03-18","2025-03-19"))
#print(NeoWs_overview())
#print(NeoWs_lookup(3542519))
print(APOD())