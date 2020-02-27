#postprocessing dataset for Neural Network - adding prices to demand_post processed dataset
import csv
from csv import writer, reader

def getprice(row,i):
    pricedata = open(
            'C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\price_' + str(i) + '.csv',
            'rt')
    csvprice = list(csv.reader(pricedata, delimiter=','))  # converts to csv

    price = csvprice[row+3][2]
    #print(price)
    return price