import os
import csv

path = os.path.join('Resources', 'budget_data.csv')

with open(path) as bank:
    csvreader = csv.reader(bank, delimiter=',')
    header = next(csvreader)
    # print(header)
    
    total = 0
    row_count = 0
    previous = 0
    change = 0
    change_list = []
    average_change = 0
    max_increase = ["", 0]
    min_decrease = ["", 999999]
    for row in csvreader:
        row_count = row_count+1
        total = total + int(row[1])
        change = int(row[1])-previous
        change_list.append(change)
        previous = int(row[1])

        if change > max_increase[1]: 
            #  if 86000 >0:
            max_increase[1] = change 
                #  max_increase = ["Jan-2010", 86000]
            max_increase[0] = row[0]
        
        if change < min_decrease[1]:
            #  if 86000 < 99999:
            min_decrease[1] = change
            #  // min_decrease = ["Jan-2010", 86000]
            min_decrease[0] = row[0]

    average_change = sum(change_list[1:])/(len(change_list)-1)

    # print(total)
    # print(row_count)
    # print (round(average_change, 2))
    # print(min_decrease[0], min_decrease[1])
    # print(max_increase[0], max_increase[1])
    

print('Financial Analysis')
print('---------------------')
print(f'Total Months: {row_count}')
print(f'Net Total Profit/Loss: {total}')
print(f'Average Change: {round(average_change, 2)}')
print(f'Greatest Increase in Profits: {min_decrease[0], min_decrease[1]}')
print(f'Greatest Decrease in Profits: {max_increase[0], max_increase[1]}')

with open(os.path.join('Analysis/financial_analysis.txt'), 'w') as txt:
    txt.writelines('Financial Analysis Results\n')
    txt.writelines('---------------------\n')
    txt.writelines(f'Total Months: {row_count}\n')
    txt.writelines(f'Net Total Profit/Loss: {total}\n')
    txt.writelines(f'Average Change: {round(average_change, 2)}\n')
    txt.writelines(f'Greatest Increase in Profits: {min_decrease[0], min_decrease[1]}\n')
    txt.writelines(f'Greatest Decrease in Profits: {max_increase[0], max_increase[1]}\n')