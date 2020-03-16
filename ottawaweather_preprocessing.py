#preprocessing dataset for Neural Network - only weather data
import csv
from datetime import datetime
from pathlib import Path

for i in range (2003, 2013): #repeats for data from 2003-2020
    #load yearly data

    #demanddata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\PUB_DemandZonal_'+ str(i) +'.csv','rt')
    #torontoweatherdata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\toronto_weather_' + str(i) + '.csv')
    ottawaweatherdata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\ottawa_weather_' + str(i) + '.csv')
    #bruceweatherdata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\bruce_weather_' + str(i) + '.csv')
    #csvdemand = csv.reader(demanddata,delimiter=',')
    #csvtoronto = csv.reader(torontoweatherdata,delimiter=',')
    csvottawa = csv.reader(ottawaweatherdata,delimiter=',') #converts to csv
    #csvbruce = csv.reader(bruceweatherdata,delimiter=',')

    with open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\ottawa_' + str(i) +'.csv', mode='w',newline='') as ott_file:
        ott_writer = csv.writer(ott_file, delimiter=',',quoting=csv.QUOTE_ALL)
        ott_writer.writerow(("Year","Month","Day","Hour","Temperature","Dew Point","Relative Humidity","Wind Speed",'\n')) #writes header
        next(csvottawa)
        for row in csvottawa:

                year= (row[5])# finds data from csv row-column intercept
                month =(row[6])
                day= (row[7])
                hour = (row[8])
                h = datetime.strptime(hour, "%H:%M")
                hour = h.hour
                temp = (row[9])
                dew = (row[11])
                relhum = (row[13])
                wspeed = (row[17])

                ott_writer.writerow((year, month, day,hour,temp,dew,relhum,wspeed)) #outputs to processed data
