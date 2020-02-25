import os
import csv
path = r'/Users/jaquelona/Documents/My_Work/homework/3_Python/python-challenge/PyPoll/Resources/election_data.csv'

with open(path) as csvfile:
    pypoll_csv= csv.reader(csvfile, delimiter=",")
    csv_header=next(pypoll_csv)
    numberofvoters = 0
    khanvotes=0
    correyvotes=0
    livotes=0
    otooleyvotes=0

    for row in pypoll_csv:
        numberofvoters = numberofvoters + 1
        onevote = row[2]
        if onevote == "Khan":
            khanvotes=khanvotes+1
        if onevote == "Correy":
            correyvotes= correyvotes+1
        if onevote == "Li":
            livotes=livotes+1
        if onevote == "O'Tooley":
            otooleyvotes= otooleyvotes+1
        
        khanpercent= float(khanvotes/numberofvoters * 100)
        correypercent=float(correyvotes/numberofvoters*100)
        lipercent=float(livotes/numberofvoters*100)
        otooleypercent=float(otooleyvotes/numberofvoters*100)

        winnervotes = correyvotes
        winner = "Correy"
        if khanvotes > correyvotes:
            winnervotes = khanvotes
            winner = "Khan"   
        if livotes > winnervotes:
            winnervotes = livotes
            winner = "Li"
        if otooleyvotes > winnervotes:   
            winnerwinnervotes= otooleyvotes
            winner = "O'Tooley"
        

    print("Election Results")
    print("----------------")
    print("Total Votes: ", str(numberofvoters))
    print("----------------")
    print("Khan: ", str(round(khanpercent,2)), "% ", "(", str(round(khanvotes,2)), "votes)")
    print("Correy: ", str(round(correypercent,3)), "% ", "(", str(correyvotes), "votes)")
    print("Li: ", str(round(lipercent,2)), "% ", "(", str(livotes), "votes)")
    print("O'Tooley: ", str(round(otooleypercent,2)), "% ", "(", str(otooleyvotes), "votes)")
    print("----------------")
    print("Winner: ", str(winner))
    
with open('PyPollOutput.py', 'w') as csvfile3:
    csvwriter = csv.writer(csvfile3)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Total Votes: "+ str(numberofvoters)])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Khan: "+ str(round(khanpercent,2))+ "% "+ "("+ str(round(khanvotes,2))+ "votes)"])
    csvwriter.writerow(["Correy: "+ str(round(correypercent,3))+ "% "+ "("+ str(correyvotes)+ "votes)"])
    csvwriter.writerow(["Li: "+ str(round(lipercent,2))+ "% "+ "("+ str(livotes), "votes)"])
    csvwriter.writerow(["O'Tooley: "+ str(round(otooleypercent,2))+ "% "+ "("+ str(otooleyvotes)+ "votes)"])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Winner: "+ str(winner)])
