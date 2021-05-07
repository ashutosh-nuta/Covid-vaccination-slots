# IMPORTS
import requests
import time
from time import sleep
import datetime
import pyttsx3

# Initialise engine for text to speech
engine = pyttsx3.init()

# Configure AGE_GROUP and DISTRICTS as per your preference
AGE_GROUP = 18
DISTRICTS = {"THANE": '392', "RAIGAD": '393', "PUNE": '363', "MUMBAI": '395'}

# To prevent Forbidden Access error
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}

def getDate(week):
    
    '''
    Gives the date in required format for the given week number (week 0 is today)
    '''
    
    return (datetime.date.today() + datetime.timedelta(weeks = week)).strftime('%d-%m-%y')


def getSlots(district_id, week):
    
    '''
    Gives important details for centers with available slots for vaccination.
    '''
    
    date = getDate(week)
    url = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={date}"
    try:
        response = requests.get(url, headers = headers, timeout=5)
        
        # Check if request was succesful
        if response.status_code == 200:
            try:
                res = response.json()
                total_centers = len(res['centers'])
                
                for center in res['centers']:
                    for session in center['sessions']:
                        
                        # You can tweak the conditions to match your preferences 
                        # e.g check for a specific center only by adding check for center['name']
                        
                        if session['available_capacity'] > 0 and session['min_age_limit'] == AGE_GROUP:
                            print(f"Center Name: {center['name']}")
                            print(f"Center Address: {center['address']}")
                            print(f"Center Pincode: {center['pincode']}")
                            print(f"Available Capacity: {session['available_capacity']}")
                            print()
                            
                            engine.say(f"Available slots in center {center['name']}")
                            engine.runAndWait()
                            engine.say(f"Address of center is {center['address']}")
                            engine.runAndWait()
                            engine.say(f"Available capacity is {session['available_capacity']}")
                            engine.runAndWait()
                            
                            break
            except KeyError:
                print('[ERROR] Script Stopped')
        else:
            print(f"[ERROR] Error Code {response.status_code}")
            
    except requests.exceptions.SSLError:
        print('[ERROR] SSL Certificate issue')
        pass
    except requests.exceptions.ConnectionError:
        print('[ERROR] Connection issue')
        pass
    except requests.exceptions.ReadTimeout:
        print('[ERROR] Timeout issue')
        pass 


if __name__ == "__main__":
    
    # Number of weeks' data that you want to check (week 0 is the 7 days starting from today)
    num_weeks = 1
    
    # Number of requests shouldn't exceed 100 in 5 minutes, adjust sleep time accordingly
    while True:
        
        for district, district_id in DISTRICTS.items():
            print("\033[1m" + "******************************************************************" + "\033[0m")
            print("\033[1m" + f"   Checking availability in {district} at {datetime.datetime.now()}" + "\033[0m")
            print("\033[1m" + "******************************************************************" + "\033[0m")
            print()
            
            for week in range(0, num_weeks):
                getSlots(district_id, week)
                
            sleep(3)
        break