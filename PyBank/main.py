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

    
    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {monthtotal}')
    print(f'Total: ${sum}')

    print(f'Average Change: ${avg_change}')

    print(f'Greatest Increase in Profits: {monthmax} (${max1})')
    print(f'Greatest Decrease in Profits: {monthmin} (${min1})')

   




    
 
    
    