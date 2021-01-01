import os
import csv

path = os.path.join('Resources', 'election_data.csv')

with open(path) as election:
    csvreader = csv.reader(election, delimiter=',')
    header = next(csvreader)
    
    vote_count = 0
    win = 0
    names = []
    votes = {}
    vote_percent= {}
    final_count = {}
    
    for row in csvreader:
        vote_count = vote_count+1
        if row[2] not in names:
            names.append(row[2])
            votes[row[2]] = 0

        votes[row[2]] = votes[row[2]]+1 
    # print(votes)    
    
    for k, v in votes.items():
        vote_percent[k] =  "{:.2%}".format(v/vote_count)
        # print(vote_percent)
    
    final_count = {key:(vote_percent[key], votes[key]) for key in votes}
    # print(final_count)
    
    win = [(value, key) for key, value in votes.items()]
    # print(max(win)[1])
        

print('Election Results')
print('-----------------------------')
print(f'Total Votes: {vote_count}')
print('-----------------------------')
print(f'Khan: {final_count.get("Khan")}')
print(f'Correy: {final_count.get("Correy")}')
print(f'Li: {final_count.get("Li")}')
print(f'''O'Tooley: {final_count.get("O'Tooley")}''')
print('-----------------------------')
print(f'Winner: {max(win)[1]}')
print('-----------------------------')

with open(os.path.join('Analysis/election_results.txt'), 'w') as txt:
    txt.writelines('Election Results\n')
    txt.writelines('------------------\n')
    txt.writelines(f'Total Votes: {vote_count}\n')
    txt.writelines('-------------------------\n')
    txt.writelines(f'Khan: {final_count.get("Khan")}\n')
    txt.writelines(f'Correy: {final_count.get("Correy")}\n')
    txt.writelines(f'Li: {final_count.get("Li")}\n')
    txt.writelines(f'''O'Tooley: {final_count.get("O'Tooley")}\n''')
    txt.writelines('---------------------\n')
    txt.writelines(f'Winner: {max(win)[1]}\n')
    txt.writelines('---------------------\n')