# Dependencies
import os
import csv

# Specify the file read
csvpath = os.path.join('Resources', 'election_data.csv')

# Loop through the third column's elements and push to a separate array
total=[]

# Read .csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip Header
    next(csvreader)
    for row in csvreader:
        total.append(row[2])

        # Total Number of Votes
        votetotal = len(total)

        # Claculate List of Candidates With Vote Count and Percentage of Total
        def unique(total):
            listset = set(total) 
            uniquelist = (list(listset)) 
            for x in uniquelist:
                print(f'{x}: {round(total.count(x)/votetotal*100,3)}% ({total.count(x)})')
            return "-------------------------"

        # Claculate Winner
        def winner(total): 
            counter = 0
            num = total[0] 
            for i in total: 
                freq = total.count(i) 
                if freq > counter: 
                    counter = freq 
                    num = i 
                return 'Winner: ' + str(num)

    # Store and print analysis rows
    print("Election Results")
    print("-------------------------")
    row1 = "Total Votes: " + str(votetotal)
    print(row1)
    print("-------------------------")
    row2 = unique(total)
    print(row2)
    row3 = winner(total)
    print(row3)
    print("-------------------------")

# Export rows to analysis.txt
outputfile = os.path.join("Analysis","analysis.txt")
with open(outputfile, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    writer.writerow([row1])
    writer.writerow(["-------------------------"])
    writer.writerow([row2])
    writer.writerow([row3])
    writer.writerow(["-------------------------"])

# # Read and Print analysis.txt
# f = open('analysis/analysis.txt', 'r')
# contents = f.read()
# print (contents)
# f.close()
