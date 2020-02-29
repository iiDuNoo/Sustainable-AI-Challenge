#connecting demand csv files
import csv
from datetime import datetime
count=0
for i in range (2013, 2021): #repeats for data from 2013-2020
    data = open(
        'C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\demand_' + str(i) + '.csv','rt')
    csvdata = csv.reader(data, delimiter=',')  # converts to csv
    with open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\combined_demand.csv', mode='a', newline='') as demand_file:
        demand_writer = csv.writer(demand_file, delimiter=',', quoting=csv.QUOTE_ALL)

        if count ==0:
            demand_writer.writerow(("Year","Month","Day","Hour","Toronto","Ottawa","Bruce","Difference","Holiday & Weekends","Price_Tor","Price_Ott", "Price_Bruce",'\n')) #writes header
            count+=1

        next(csvdata)
        for row in csvdata:
            year = (row[0])  # finds data from csv row-column intercept
            month = (row[1])
            day = (row[2])
            hour = (row[3])
            toronto = (row[4])
            ott = (row[5])
            bruce = (row[6])
            diff = (row[7])
            holiday = (row[8])
            torprice = (row[9])
            ottprice = (row[10])
            bruceprice = (row[11])
            demand_writer.writerow((year, month, day,hour,toronto,ott,bruce,diff,holiday,torprice,ottprice,bruceprice))  # outputs to processed data

