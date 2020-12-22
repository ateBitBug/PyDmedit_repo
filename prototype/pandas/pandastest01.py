import pandas as pd
from sys import platform

data = {
  'apples': [3,2,0,1],
  'oranges': [0,3,7,2]
}

purchases = pd.DataFrame(data, index=['june', 'robert', 'lily', 'tom'])
print(f"{purchases}")

junePurchase = purchases.loc['june']
print(f"{junePurchase}")

pdseries = pd.Series([1,2,3])
print(f"{pdseries}")

d = {'one': pd.Series([1,2,3])}
df = pd.DataFrame(d)
print(f"{df}")

print(f"reading temp.csv file")
if platform == "linux" or platform == "linux2":
  inputTemp = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/temp.csv"
elif platform == "win32":
  inputTemp = "d:/compilers/gitRepo/pydmedit-repos/data/temp.csv"
else:
  inputTemp = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/temp.csv"

df = pd.read_csv(inputTemp)
print(df)