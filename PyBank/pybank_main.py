import os
import csv

bank = os.path.join('Resources', 'budget_data.csv')

with open(bank) as csvfile:
    csvreader = csv.reader(bank, delimiter=',')
