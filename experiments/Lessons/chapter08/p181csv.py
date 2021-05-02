import csv

villains = [
  ['doctor', 'no'],
  ['rosa', 'klebb'],
  ['mister', 'big'],
  ['auric', 'goldfinger'],
  ['ernst', 'blofeld']
]

with open('villains.txt', 'w', newline='') as fout:
  csvout = csv.writer(fout)
  csvout.writerows(villains)

print("reading villains.txt")
villains = []
with open('villains.txt', 'r') as fin:
  cin = csv.reader(fin)
  villains = [row for row in cin]
print(villains)

print("reading villains.txt with DictReader")
villains = []
with open('villains.txt', 'r') as fin:
  cin = csv.DictReader(fin, fieldnames=['first', 'last'])
  villains = [row for row in cin]
print(villains)