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
    lastprofit=0
    greatestchange = 0
    profit = 0
    change = 0
    biggestloser = 0
    for row in pybank_csv:
        numberofrows = numberofrows + 1
        profit = int(row[1])
        totalprofit = totalprofit + profit

        #find the biggest change
        change = profit - lastprofit
        if change > greatestchange:
            greatestchange = change
            greatestchangemonth = row[0]
        totalchange +=change
        lastprofit = profit

        #find biggest decrease (least change)
        if change < biggestloser:
            biggestloser = change
            biggestlosermonth = row[0]
        

    averagechange = totalchange/numberofrows
    print("Financial Analysis")
    print("------------------")
    print("Total Months: ", str(numberofrows))
    print("Total: $" + str(totalprofit))
    print("Greatest increase in profits: ", str(greatestchangemonth), " $", str(greatestchange))
    print("Greatest decrease in profits: ", str(biggestlosermonth), " $", str(biggestloser))
    