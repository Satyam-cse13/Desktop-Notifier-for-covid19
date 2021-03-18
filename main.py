from plyer import notification
import datetime
import time
import requests



covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/India")
except:
    #if the data is not fetched due to lack of internet
    print("Please! Check your internet connection")

#loop for notification
if (covidData != None):

    data = covidData.json()['Success']


    while (True):
        notification.notify(

            title="COVID19 Stats on {}".format(datetime.date.today()),


            message="Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                totalcases=data['cases'],
                todaycases=data['todayCases'],
                todaydeaths=data['todayDeaths'],
                active=data["active"]),

           
            # the notification stays for 50sec
            timeout=20
        )

        # notification repeats after every 1 hrs
        time.sleep(60 * 60 )