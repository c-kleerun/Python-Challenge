import os
import csv

path = os.path.join('Resources', 'budget_data.csv')

with open(path) as bank:
    csvreader = csv.reader(bank, delimiter=',')
    header = next(csvreader)
    print(header)

    row_count = sum(1 for row in csvreader)
    print(row_count)
    #


# total_months = x
# for x in row[0]
#     x = (x+1)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {row_count}")
# print(f"")