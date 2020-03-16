#postprocessing dataset for Neural Network - adding holidays to demand_post processed dataset
import csv
from csv import writer, reader
from datetime import datetime
from pathlib import Path

def main(date,i):
    marker =0
    rows,cols = (1,4)
    arr = [[0] * cols] * rows
    holidays = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\holidays.csv','r')
    csvholidays = csv.reader(holidays,delimiter=',')
    next(csvholidays)

    for x in csvholidays:
        new =[x[0], x[1], x[2]]
        arr.append(new)

    #for i in range(2013, 2021): #repeats for data from 2003-2020

    #demanddata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\dataset_toronto.csv','r')
    #csvdemand = csv.reader(demanddata,delimiter=',') #converts to csv
    #next(csvdemand)
    #demandwrite= open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\dataset_toronto.csv', 'w',newline='')
    #writer = csv.writer(demandwrite, delimiter=',')
    #for count in range(len(arr)):
        #for y in csvdemand:
    if i < 2018:  # striping dates
        d = datetime.strptime(date, '%Y-%m-%d')
        dt = datetime.date(d)
    elif i == 2020:
        d = datetime.strptime(date, '%Y-%m-%d')
        dt = datetime.date(d)
    else:
        d = datetime.strptime(date, '%d/%m/%Y')
        dt = datetime.date(d)
    dem_day = dt.day
    dem_mon = dt.month
    dem_year = dt.year

    for count in range(len(arr)):

        hol_day = arr[count][0]
        hol_mon = arr[count][1]
        hol_year = arr[count][2]
        if hol_day == str(dem_day) and hol_mon == str(dem_mon) and hol_year == str(dem_year):
            marker = 1
            break

        else:
            marker =0
    #print(marker)
    return marker

#main("2013-02-18",2013)
