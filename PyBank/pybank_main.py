import os
import csv

path = os.path.join('Resources', 'budget_data.csv')

with open(path) as bank:
    csvreader = csv.reader(bank, delimiter=',')
    header = next(csvreader)
    print(header)
    
    row_count = sum(1 for row in csvreader)
    print(row_count)

    total = 0
    for row in csvreader:
        total += (row[1])
    print(total)
    
    # total = sum(row[1] for row in csvreader)
    # print(total)

    # max_num = max(row[1] for x in csvreader if x >=0)
    # print(max_num)

    # min_num = min(row[1] for x in csvreader if x <0)
    # print(min_num)
    

    # changes = 0
    # for row in csvreader:
    #     changes_total = (int(row[1])+1)
    #     print(changes_total)
    #     print(changes_total.mean())
    
    

# print('Financial Analysis')
# print('---------------------')
# print(f'Total Months: {row_count}')
# print(f'Net Total Profit/Loss: {total}')
# # print(f'Average Change: {average_change}')
# # print(f'Greatest Increase in Profits: {max_num}')
# # print(f'Greatest Decrease in Profits: {min_num}')

# with open('financial_analysis.txt', 'w') as txt:
#     txt.writelines('Financial Analysis Results')