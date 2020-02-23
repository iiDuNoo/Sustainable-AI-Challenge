#preprocessing dataset for Neural Network
import csv

for i in range (2013, 2020):
    demanddata = open('PUB_DemandZonal_' + i + '.csv')
    torontoweatherdata = open('toronto_weather_' + i + '.csv')
    ottawaweatherdata = open('ottawa_weather_' + i + '.csv')
    bruceweatherdata = open('bruce_weather_' + i + '.csv')
    csvdata = csv.reader(demanddata)
