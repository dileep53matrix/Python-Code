import csv 
values = []

with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        values.append(float(row["temp"]))
        
print("Max:",max(values))
print("Min:",min(values))
print("Average:",sum(values)/len(values))