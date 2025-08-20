import csv
with open('t.csv', 'w') as f:
    w = csv.writer(f)
    w.writerow([1, 2])