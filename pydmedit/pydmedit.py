import csv
import copy
import importlib
from sys import platform



class Pers(object):
  def __init__(self):
    self.hrstate={}
    self.ctrlnum={}
    self.pulineno={}
    self.pufname={}
    self.puage={}
    self.pulinenoList=[]
    self.test=None

  def initializeVars(self,_row,_key):
    self.hrstate[_row[_key]]=_row['HRSTATE']
    self.ctrlnum[_row[_key]]=_row['CTRLNUM']
    self.pulineno[_row[_key]]=_row['PULINENO']
    self.pufname[_row[_key]]=_row['PUFNAME']
    self.puage[_row[_key]]=_row['PUAGE']

  def reset(self):
    self.hrstate.clear()
    self.ctrlnum.clear()
    self.pulineno.clear()
    self.pufname.clear()
    self.puage.clear()
    self.pulinenoList=[]



class Heros(object):
  def __init__(self):
    self.hrprocid={}
    self.ctrlnum={}
    self.pulineno={}
    self.prjobstatus={}
    self.prjobname={}
    self.prsuperhero={}
    self.prheroname={}
    self.pulinenoList=[]

  def initializeVars(self,_row,_key):
    self.hrprocid[_row[_key]]=_row['HRPROCID']
    self.ctrlnum[_row[_key]]=_row['CTRLNUM']
    self.pulineno[_row[_key]]=_row['PULINENO']
    self.prjobstatus[_row[_key]]=_row['PRJOBSTATUS']
    self.prjobname[_row[_key]]=_row['PRJOBNAME']
    self.prsuperhero[_row[_key]]=_row['PRSUPERHERO']
    self.prheroname[_row[_key]]=_row['PRHERONAME']

  def reset(self):
    self.hrprocid.clear()
    self.ctrlnum.clear()
    self.pulineno.clear()
    self.prjobstatus.clear()
    self.prjobname.clear()
    self.prsuperhero.clear()
    self.prheroname.clear()
    self.pulinenoList=[]







class KeyMonitor(object):
  def __init__(self, keys):
    self._keys = keys
    self._index = 0
    self._key = None


  def __iter__(self):
    # self._index = 0
    return self


  def __next__(self):
    if self._index < len(self._keys):
      self._key = self._keys[self._index]
      self._index += 1
      return self._key
    else:
      raise StopIteration


  def nextKey(self):
    return self._keys[self._index]


  def currentKey(self):
    return self._key




class Dataset(object):
  def __init__(self, data, kM, fn):
    self._data = data
    self._keyMonitor = kM
    self._inputPer = fn
    self._key = ""
    self._buffer = []

    # open the input file; this will remain open until the eof is reached
    self._openDataset = open(fn, 'r')

    # csv.DictReader() returns an "orderedDict" type (ordered dictionary); it is
    # a list of a pair of tuples:
    #  i.e. [(key1, val1), (key2, val2), (key3, val3)]
    #  python 3.6 -> returns orderedDict
    #  python 3.8 -> returns dict
    # https://www.journaldev.com/21807/python-ordereddict
    # https://www.programiz.com/python-programming/reading-csv-files
    #
    # more on DictReader:
    #   https://thispointer.com/python-read-a-csv-file-line-by-line-with-or-without-header/
    self._csvReader = csv.DictReader(self._openDataset)
    self._csvHeader = self._csvReader.fieldnames


  def getRecords(self, key):
    self._key = key
    csvKey = None

    print(f'\n*** searching for self._key: {self._key}')
    
    # this try-except is needed to handle the last group of records with same
    # csvKey
    try:
      curLine = next(self._csvReader)
      csvKey = curLine['CTRLNUM']
      # print(f"csvKey: {csvKey} -> curLine: {curLine}")
    except StopIteration:
      # https://realpython.com/copying-python-objects/
      yield copy.deepcopy(self._data)
      # print("!!!!! 1 blanking...")
      self._data.reset()

    while csvKey:
      if self._key == csvKey:
        # print(f"+++ appending self._key: {self._key} -- csvKey: {csvKey}")
        self._data.pulinenoList.append(curLine['PULINENO'])
        self._data.initializeVars(curLine, 'PULINENO')
        print(f"   so far added... {self._data.pulinenoList}")
      else:
        # curLine's (current line) csvKey is not same as the search key; which
        # indicates that curLine is pointing to the beginning of new records of
        # a new csvKey records; sends all collected records in 'self._data' for
        # an edit by sending a copy
        yield copy.deepcopy(self._data)

        # returns from the edit
        print("!!!!! 2 blanking...")
        self._data.reset()

        # saves the curLine record
        self._data.pulinenoList.append(curLine['PULINENO'])
        self._data.initializeVars(curLine, 'PULINENO')

        # breaks out of the while loop to get the next available master key
        break

      try:
        curLine = next(self._csvReader)
        csvKey = curLine['CTRLNUM']
      except StopIteration:
        yield copy.deepcopy(self._data)

        # after returns from the edit, break out of the "while-loop" and get
        # the next key
        break
    else:
      # the eof has reached; if there is anything in the buffer, send them to
      # edit
      if len(self._data.pulinenoList) != 0:
        yield copy.deepcopy(self._data)


  def openDataset(self):
    return self._openDataset


  def closeDataset(self):
    self._openDataset.close()







if __name__ == '__main__':
  pers=Pers()
  heros=Heros()

  keys = ['333Z333','999K999','111A111','222B222']
  
  print(platform)

  if platform == "linux" or platform == "linux2":
    inputHero = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/heros.csv"
    inputPer = "/home/woof/PycharmProjects/gitRepo/pydmedit-repos/data/pers.csv"
  elif platform == "win32":
    inputHero = "d:/compilers/githubRepos/pydmedit-repos/data/heros.csv"
    inputPer = "d:/compilers/githubRepos/pydmedit-repos/data/pers.csv"
  else:
    inputHero = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/heros.csv"
    inputPer = "/Volumes/macExFat/compilers/gitRepo/pydmedit-repos/data/pers.csv"

  keyMonitor = KeyMonitor(keys)
  heroDS = Dataset(heros, keyMonitor, inputHero)
  perDS = Dataset(pers, keyMonitor, inputPer)

  for key in keyMonitor:
    for hero in heroDS.getRecords(key):
      print(f"...I am adding repo found hero... -> {hero.pulinenoList}")
      print(f"...found heros... -> {heros.pulinenoList}")

    for persons in perDS.getRecords(key):
      print(f"...another I am repo found persons... -> {persons.pulinenoList}")
      print(f"...check found pers... -> {pers.pulinenoList}")


    print(f" ---- editing -> key: {key} -- hero: {hero.pulinenoList}")
    print(f" ---- reverse repo editing -> key: {key} -- persons: {persons.pulinenoList}")

    for i in hero.pulinenoList:
      heroName = hero.prheroname[i]
      heroRealName = persons.pufname[i]
      print(f"prheroname: {heroName} -- real name: {heroRealName}")


  # updating a csv file
  # https://codereview.stackexchange.com/questions/98627/updating-a-csv-file
  perDS.closeDataset()
  heroDS.closeDataset()
