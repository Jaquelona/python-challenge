import os
import csv

path = r'/Users/jaquelona/Documents/My_Work/homework/3_Python/python-challenge/PyBank/data.csv'

with open(path) as csvfile: 
    pybank_csv= csv.reader(csvfile, delimiter=",")
    csv_header=next(pybank_csv)
    #define my variables
    numberofrows=0
    totalprofit = 0
    totalchange = 0
    lastprofit=0
    greatestchange = 0
    profit = 0
    change = 0
    biggestloser = 0
    #count number of rows and total profit
    for row in pybank_csv:
        numberofrows = numberofrows + 1
        profit = int(row[1])
        totalprofit = totalprofit + profit

        #find the biggest change
        change = profit - lastprofit
        if numberofrows != 1:
            totalchange = totalchange + change
        if change > greatestchange:
            greatestchange = change
            greatestchangemonth = row[0]
        
        lastprofit = profit

        #find biggest decrease (least change)
        if change < biggestloser:
            biggestloser = change
            biggestlosermonth = row[0]
        
        print(change)

    averagechange = (totalchange) /(numberofrows-1)
    print("Financial Analysis")
    print("------------------")
    print("Total Months: ", str(numberofrows))
    print("Total: $" + str(totalprofit))
    print("Greatest increase in profits: ", str(greatestchangemonth), " $", str(greatestchange))
    print("Greatest decrease in profits: ", str(biggestlosermonth), " $", str(biggestloser))
    print("The average change is: $", str(round(averagechange,2)))
    


with open('PyBankOutput.py', 'w', newline='') as csvfile2:
csvwriter = csv.writer(csvfile2)
csvwriter.writerow(["Financial Analysis"])
csvwriter.writerow(["------------------"])
csvwriter.writerow(["Total Months: ", str(numberofrows)])
csvwriter.writerow(["Total: $" + str(totalprofit)])
csvwriter.writerow(["Greatest increase in profits: ", str(greatestchangemonth), " $", str(greatestchange)])
csvwriter.writerow(["Greatest decrease in profits: ", str(biggestlosermonth), " $", str(biggestloser)])
csvwriter.writerow(["The average change is: $", str(averagechange)])
        
