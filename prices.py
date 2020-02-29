#postprocessing dataset for Neural Network - adding prices to demand_post processed dataset
import csv
from csv import writer, reader

def getprice(row,i):
    pricedata = open(
            'C:\\Users\\Adam\\Documents\\GitHub\\Sustainable-AI-Challenge\\Raw_Dataset\\nodal_price_' + str(i) + '.csv',
            'rt')
    csvprice = list(csv.reader(pricedata, delimiter=','))  # converts to csv

    torprice = csvprice[row+4][11]
    ottprice = csvprice[row + 4][9]
    bruceprice = csvprice[row + 4][13]
    price=[torprice,ottprice,bruceprice]
    #print(price)
    return price
