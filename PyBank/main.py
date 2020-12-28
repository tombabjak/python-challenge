# Dependencies
import os
import csv

# Specify the file read
csvpath = os.path.join('Resources', 'budget_data.csv')

# Loop through each column's elements and push to separate arrays
total=[]
months=[]
change=[]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        total.append(int(row[1]))
        months.append(row[0])
    
    # Find Total Number of Months
    monthtotal = len(months)
    
    # Find Total
    sum = 0
    for x in total:
        sum = sum + int(x)
        avg_change = sum/monthtotal

    # Find Average Change
    for i in range(1,monthtotal):
        change.append(total[i]-total[i-1])
        sumchange = 0
        for y in change:
            sumchange = sumchange + int(y)
            avgchange = sumchange/(monthtotal-1)

    # Find Greatest Decrease, Amount and Month/Year
    min1 = min(total)
    minindex = total.index(min1)
    monthmin = months[minindex]

    # Find Greatest Increase, Amount and Month/Year    
    max1 = max(total)
    maxindex = total.index(max1)
    monthmax = months[maxindex]

    # Store analysis rows
    row1 = 'Total Months: ' + str(monthtotal)
    row2 = 'Total: $' + str(sum)
    row3 = 'Average Change: $' + str(round(avgchange,2))
    row4 = 'Greatest Increase in Profits: ' + str(monthmax) + ' ($' + str(max1) + ')'
    row5 = 'Greatest Decrease in Profits: ' + str(monthmin) + ' ($' + str(min1) + ')'

# Export rows to analysis.txt
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

# Read and Print analysis.txt
f = open('analysis/analysis.txt', 'r')
contents = f.read()
print (contents)
f.close()