import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

total=[]
months=[]

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        
        total.append(int(row[1]))
        months.append(row[0])

    min1 = min(total)
    minindex = total.index(min1)
    monthmin = months[minindex]
        
    max1 = max(total)
    maxindex = total.index(max1)
    monthmax = months[maxindex]

    monthtotal = len(months)
    
    sum = 0

    for x in total:

        sum = sum + int(x)

        avg_change = sum/monthtotal

    row1 = 'Total Months: ' + str(monthtotal)
    row2 = 'Total: $' + str(sum)
    row3 = 'Average Change: $' + str(avg_change)
    row4 = 'Greatest Increase in Profits: ' + str(monthmax) + ' ($' + str(max1) + ')'
    row5 = 'Greatest Decrease in Profits: ' + str(monthmin) + ' ($' + str(min1) + ')'

outputfile = os.path.join("Analysis","analysis.txt")
with open(outputfile, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow([row1])
    writer.writerow([row2])
    writer.writerow([row3])
    writer.writerow([row4])
    writer.writerow([row5])

f = open('analysis/analysis.txt', 'r')
contents = f.read()
print (contents)
f.close()