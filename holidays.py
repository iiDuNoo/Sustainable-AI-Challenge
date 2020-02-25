#postprocessing dataset for Neural Network - adding holidays to demand_post processed dataset
import csv
from csv import writer, reader
from datetime import datetime
from pathlib import Path
marker =0
remembercount=0
p=0
total=0
rows,cols = (1,4)
arr = [[0] * cols] * rows
holidays = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\holidays.csv','r')
csvholidays = csv.reader(holidays,delimiter=',')
next(csvholidays)

for x in csvholidays:
    new =[x[0], x[1], x[2]]
    arr.append(new)

for i in range(2013, 2021): #repeats for data from 2013-2020

    demanddata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\demand_'+ str(i) +'.csv','r')
    csvdemand = csv.reader(demanddata,delimiter=',') #converts to csv
    next(csvdemand)
    demandwrite= open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\demand_' + str(i) + '.csv', 'a')
    writer = csv.writer(demandwrite, delimiter=',')
    for count in range(114):
        for y in csvdemand:
            dem_day = y[2]
            dem_mon = y[1]
            dem_year = y[0]
            hol_day = arr[count+1][0]
            hol_mon = arr[count+1][1]
            hol_year = arr[count+1][2]

            print("holiday: " +str(hol_day)+ "/" + str(hol_mon) + "/" +str(hol_year)+ " versus day: " + dem_day + "/" + dem_mon + "/" + dem_year)

            if str(hol_day) == dem_day and str(hol_mon) == dem_mon and str(hol_year) == dem_year:
                marker = 1
                p+=1
                total+=1
                print(dem_day + "/" + dem_mon + "/" + dem_year)

            else:
                marker =0
                #y[8]=(hol)
                #demandwrite.writerow(y+[marker])
            if p == 24:
                p=0
                count+=1

            print("p: " +str(p))
            print("total " +str(total))