import csv
from sys import platform

''' +
hrprocid,ctrlnum,pulineno,puage,pufname,hrmis,hrintsta,hrstate,prjobstatus,
prjobname,prsuperhero,prheroname

/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/hhldsPers.csv
+ '''

# hhdVarnamesL = ['HRSTATE','CTRLNUM']

'''*
  a list of variables kept from the input file; i.e.
    input file -> data/hhldsPers.csv
      variables to keep are:
        'HRSTATE', 'CTRLNUM', 'PULINENO'

      new variables can be created by adding them into the list, these new
      variables are assigned "" (a blank value) i.e. the csv file with the
      variable names as its header:

        HRSTATE, NEWVAR2, CTRLNUM, PULINENO, NEWVAR1
             NY,        , 123DEFG,        1,

    output file -> hhlds.csv
*'''
if platform == "linux" or platform == "linux2":
  inputDS = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/hhldsPers.csv"
  outputDS = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/hhlds.csv"
elif platform == "win32":
  inputDS = "d:/compilers/githubRepo/pydmedit-repos/data/hhldsPers.csv"
  outputDS = "d:/compilers/githubRepo/pydmedit-repos/data/hhlds.csv"
else:
  inputDS = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/hhldsPers.csv"
  outputDS = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/hhlds.csv"

hhdVarnamesL = ['HRSTATE','NEWVAR2', 'CTRLNUM', 'NEWVAR1']

with open(outputDS,'w') as csvOF:
  csvWriter=csv.DictWriter(csvOF,fieldnames=hhdVarnamesL,extrasaction='ignore',
    lineterminator='\n')
  csvWriter.writeheader()

  with open(inputDS,'r') as csvF:
    csvReader=csv.DictReader(csvF,delimiter=',')
    #csvReader=csv.DictReader(csvF,fieldnames=hhdVarnamesL,delimiter=',') -> doesn't work because variables are skipped
    csvHeader=csvReader.fieldnames

    for row in csvReader:
      csvWriter.writerow(row)