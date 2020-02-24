#postprocessing dataset for Neural Network - adding holidays to demand_post processed dataset
import csv
from datetime import datetime
import pprint
import sys
from pathlib import Path
for i in range (2013, 2021): #repeats for data from 2013-2020

    demanddata = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Postprocessed_Dataset\\demand'+ str(i) +'.csv','rt')
    holidays = open('C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\holidays.csv','rt')
    csvholidays = csv.reader(holidays,delimiter=',')
    csvdemand = csv.reader(demanddata,delimiter=',') #converts to csv