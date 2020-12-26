import os
import csv

path = os.path.join('Resources', 'election_data.csv')

with open(path) as election:
    csvreader = csv.reader(election, delimiter=',')
    header = next(csvreader)
    
    row_count = sum(1 for row in csvreader)
    
    name:[]
    for row in csvreader:
        if row not in name:
            name.append(row)
        print(name)





print('Election Results')
print('--------------------')
print(f'Total Votes: {row_count}')
print('---------------------')
# print('Khan:', 'Correy: ', 'Li: ', "O'Tooley: " )
# print('---------------------')
# print('Winner: {}')
# print('---------------------')