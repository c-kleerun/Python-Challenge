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
        

    # print(names)
    print(votes)



# def total_votes (name, percent):
#         if x in name:
#             return name[percent]

#     votes['_found'] = total_votes

# k = total_votes["Khan"]
# c = total_votes["Correy"]
# l = total_votes["Li"]
# o = total_votes["O'Tooley"]


print('Election Results')
print('--------------------')
print(f'Total Votes: {vote_count}')
print('---------------------')
# print("{k} \n{c} \n{l} \n{o}")
# print('---------------------')
# print('Winner: {}')
# print('---------------------')