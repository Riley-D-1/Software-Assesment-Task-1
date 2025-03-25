import requests
import time
# Here we have the fetching of the APOD data
def APOD(date):
    params={"api_key": API_KEY,'date': date}
    APOD_URL = "https://api.nasa.gov/planetary/apod"
    response = requests.get(APOD_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data  
    elif response.status_code == 429:
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
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
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
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
        print(f"The API key can make {response.headers['X-RateLimit-Remaining']} more requests.")
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
#print(APOD('2025-03-23'))
