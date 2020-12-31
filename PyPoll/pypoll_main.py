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
        
    for k,v in votes.items():
        pct = v * 100/vote_count
        # if k in votes:
        #     votes[k].append(pct)
        
        print(k, (round(pct)))

    # print(names)
    # print(votes)
    

print('Election Results')
print('--------------------')
print(f'Total Votes: {vote_count}')
print('---------------------')
print(f'Khan: {votes.get("Khan")}')
# print(f'Correy: {(round(pct, 2))}%, {votes.get("Correy")}')
# print(f'Li: {(round(pct, 2))}%, {votes.get("Li")}')
# print("O'Tooley:" + {(round(pct,2))} + {votes.get("O'Tooley")})
    # Correct formatting? 
    # There needs to be both single and double quotes to get this to work...
print('---------------------')
# print('Winner: {}')
# print('---------------------')

# with open(os.path.join('Analysis/election_results.txt'), 'w') as txt:
#     txt.writelines('Election Results\n')
#     txt.writelines('------------------\n')
#     txt.writelines(f'Total Votes: {vote_count}\n')
#     txt.writelines('-------------------------\n')
#     txt.writelines()
#     txt.writelines()
#     txt.writelines()
#     txt.writelines()