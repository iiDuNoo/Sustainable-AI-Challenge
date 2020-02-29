#preprocessing dataset for Neural Network - only demand data
import csv
from datetime import datetime
import pprint
import sys
import subprocess
from holidays import main
from prices import getprice
from pathlib import Path

def run():
    for i in range (2017, 2021): #repeats for data from 2013-2020
        #load yearly data

        demanddata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\PUB_DemandZonal_'+ str(i) +'.csv','rt')
        #torontoweatherdata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\toronto_weather_' + str(i) + '.csv')
        #ottawaweatherdata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\ottawa_weather_' + str(i) + '.csv')
        #bruceweatherdata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\bruce_weather_' + str(i) + '.csv')
        #holidays = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\holidays.csv','rt')
        #csvholidays = csv.reader(holidays,delimiter=',')
        csvdemand = csv.reader(demanddata,delimiter=',') #converts to csv

        #csvtoronto = csv.reader(torontoweatherdata,delimiter=',')
        #csvottawa = csv.reader(ottawaweatherdata,delimiter=',')
        #csvbruce = csv.reader(bruceweatherdata,delimiter=',')

        with open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\demand_' + str(i) +'.csv', mode='w',newline='') as demand_file:
            demand_writer = csv.writer(demand_file, delimiter=',',quoting=csv.QUOTE_ALL)
            demand_writer.writerow(("Year","Month","Day","Hour","Toronto","Ottawa","Bruce","Difference","Holiday & Weekends","Price_Tor","Price_Ott", "Price_Bruce",'\n')) #writes header
            next(csvdemand)#spacing
            next(csvdemand)
            next(csvdemand)
            next(csvdemand)
            count=0
            for row in csvdemand:
                count+=1
                date= (row[0])# finds data from csv row-column intercept
                hour =(row[1])
                toronto = (row[7])
                ott = (row[5])
                bruce = (row[9])
                diff = (row[14])
                holiday= main(date,i)
                price = getprice(count,i)
                torprice = price[0]
                ottprice = price[1]
                bruceprice = price[2]
                #holiday = subprocess.check_output([sys.executable, "holidays.py", date,str(i)])

                if i <2018: #striping dates
                    d = datetime.strptime(date,'%Y-%m-%d')
                    dt = datetime.date(d)
                elif i ==2020:
                    d = datetime.strptime(date,'%Y-%m-%d')
                    dt = datetime.date(d)
                else:
                    d = datetime.strptime(date,'%d/%m/%Y')
                    dt = datetime.date(d)

                demand_writer.writerow((dt.year, dt.month, dt.day,hour,toronto,ott,bruce,diff,holiday,torprice,ottprice,bruceprice)) #outputs to processed data

run()

