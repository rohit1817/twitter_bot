import tweepy
from datetime import datetime
import holidays

#Authentication
API_key= "Insert API key"
API_secret_key= "Insert API secret key"
Bearer_token= "Insert bearer token"
Access_token= "Insert access token"
access_secret_token= "Insert access secret token"


auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(Access_token, access_secret_token)

#API creation
api = tweepy.API(auth)

def get_date_and_day():
    now = datetime.now()
    date_string = now.strftime("%B %d, %Y")
    day_string = now.strftime("%A")
    return date_string, day_string

def holiday_message():
    US_holidays = holidays.UnitedStates()
    India_holidays = holidays.India()
    holiday = ""
    now = datetime.now()
    
    if now.date() in US_holidays or now.date() in India_holidays:
        if now.date() in US_holidays:
            holiday = US_holidays.get(now.date())
        else:
            holiday = India_holidays.get(now.date())
        if holiday!= "":
            greeting = f"Happy {holiday}. Hope you have a great day today!"
            api.update_status(greeting)
        else: return None 
        
def greeting_message():
    date_string, day_string = get_date_and_day()
    now = datetime.now()
    if now.hour == 6 and now.minute == 0:
        message = f"Good morning people, Today is {date_string} and it's {day_string}. Have a great day!"
        api.update_status(message)
    elif now.hour == 12 and now.minute == 0:
        message = f"It's noon people, don't forget to eat your lunch and stay hydrated always!"
        api.update_status(message)
    elif now.hour == 22 and now.minute == 0:
        message = f"Hope you had a good day today. Good night guys!"
        api.update_status(message)
        
        
def hydrated_message():
    now = datetime.now()
    list_time = (6, 9, 15, 18, 21)
    if now.hour in list_time and now.minute == 0:
        hour = now.strftime("%I")
        #meridian = now.strftime("%p")
        message = f"Hey guys, it's {hour} o'clock. Don't forget to drink water. #StayHydrated"
        api.update_status(message)
        
greeting_message()
holiday_message()
hydrated_message()

