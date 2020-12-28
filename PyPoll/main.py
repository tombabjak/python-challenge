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

    # Open output file
    f = open("Analysis/analysis.txt", "w")
    print("Election Results", file=f)
    print("-------------------------", file=f)

    # Total Number of Votes
    votetotal = len(total)
    row1 = "Total Votes: " + str(votetotal)

    # Export rows to output file
    print(row1, file=f)
    print("-------------------------", file=f)

    # Calculate List of Candidates With Vote Count, Percentage of Total, and Winner
    def unique(total):
        uniquelist = list(set(total))
        votecount=[]
        names=[]
        for x in uniquelist:
            votecount.append(total.count(x))
            names.append(x)
            print(f'{x}: {round(total.count(x)/votetotal*100,3)}% ({total.count(x)})', file=f)
        win1 = max(votecount)
        windex = votecount.index(win1)
        winner = names[windex]
        print("-------------------------", file=f)
        print(f'Winner: {winner}', file=f)
        print("-------------------------", file=f)
    
    # Run function and export to output file
    unique(total)

    # Read, print, and close output file
    f = open('analysis/analysis.txt', 'r')
    contents = f.read()
    print (contents)
    f.close()