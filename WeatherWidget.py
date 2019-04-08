# This widget will use free openweathermap.org/api in order to show weather information
#
# Im using Gdansk id : either 7531890 or 3099434

import time
import requests
import json
import IconSelector
from apiKey import key


class ApiCaller:

    def __init__(self):
        self.linesToBeDisplayed = 4
        self.key = key
        self.serverName = "api.openweathermap.org"
        self.cityId = "3099434"
        self.units = "units=metric"
        self.iconName = ""
        self.call = "http://api.openweathermap.org/data/2.5/forecast?id={0}&APPID={1}&{2}&cnt={3}"\
            .format(self.cityId, key, self.units, self.linesToBeDisplayed)
        self.jsonData = {}
        self.lastUpdate = None

    def makeWeatherRequest(self):
        # Making call to openweather.com api, and saves result in json. Also writes timestamp for freshness checking
        try:
            self.lastUpdate = time.strftime("%H:%M:%S")
            response = requests.get(self.call)
            self.jsonData = json.loads(response.text)
            self.dumpJson()
        except requests.exceptions.RequestException as err:
            print("Check your internet connection: \ndetails: {}".format(err))

    def dumpJson(self):
        with open("responseInJson.txt", "w") as file:
            json.dump(self.jsonData, file)

    def getCurrentTemp(self):
        self.makeWeatherRequest()
        # Not implemented functionality to check if weather info is up-to-date
        # checkIfUpdated()
        with open("responseInJson.txt", "r") as jsonData:
            self.jsonData = json.load(jsonData)
        try:
            return self.jsonData['list'][0]['main']["temp"]
        except KeyError as k:
            print("Check your ApiKey file for proper configuration")
            return "Error"


    def getFutureTemp(self, numbersof3hrs):
        # Takes as argument number of future forecast each number increase 3 hrs i.e. numebersof3hrs = 2 is equal 6 hrs
        with open("responseInJson.txt", "r") as jsonData:
            self.jsonData = json.load(jsonData)
            try:
                return self.jsonData['list'][numbersof3hrs]['main']["temp"]
            except KeyError as k:
                print("Check your ApiKey file for proper configuration")
                return "Error"



    def getIconCode(self):
        with open("responseInJson.txt", "r") as jsonData:
            self.jsonData = json.load(jsonData)
        self.iconName = self.jsonData['list'][0]['weather'][0]['description']
        return IconSelector.returnIconName(self.iconName)



