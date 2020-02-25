import os
import csv

path = r'/Users/jaquelona/Documents/My_Work/homework/3_Python/python-challenge/PyBank/data.csv'

with open(path) as csvfile: 
    pybank_csv= csv.reader(csvfile, delimiter=",")
    csv_header=next(pybank_csv)
    #print(pybank_csv)
    numberofrows=0
    totalprofit = 0
    totalchange = 0
    change1=0
    change2=0
    lastprofit=0
    greatestchange = 0
    change = []
    for row in pybank_csv:
        numberofrows = numberofrows + 1
        profit = int(row[1])
        totalprofit = totalprofit + profit
        lastprofit = profit
        #find the biggest change
        change1= int(row[1])
        

    averagechange = totalchange/numberofrows
    print("Financial Analysis")
    print("------------------")
    print("Total Months: ", str(numberofrows))
    print("Total: $" + str(totalprofit))
    #print("Average Change: $", str(averagechange))
    print(greatestchange)