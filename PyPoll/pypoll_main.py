import os
import csv

path = os.path.join('Resources', 'election_data.csv')

with open(path) as election:
    csvreader = csv.reader(election, delimiter=',')
    header = next(csvreader)
    
    vote_count = 0
    names = []
    votes = {}
    for row in csvreader:
        vote_count = vote_count+1
        if row[2] not in names:
            names.append(row[2])
            votes[row[2]] = 0

        votes[row[2]] = votes[row[2]]+1 
        # votes[khan]=1 +1
        
    # for x in votes: 
    #     vote_percent = votes[1]/vote_count
    #     print(vote_percent)

    print(names)
    print(votes)
    

print('Election Results')
print('--------------------')
print(f'Total Votes: {vote_count}')
print('---------------------')
# print("{k} \n{c} \n{l} \n{o}")
# print('---------------------')
# print('Winner: {}')
# print('---------------------')