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
  def __init__(self, kM, fn, mxsz):
    self._keyMonitor = kM
    self._inputPer = fn
    self._key = ""
    self._buffer = []
    self._MAXSIZE = mxsz
    self._openDataset = open(fn, 'r')


  def getRecords(self, key):
    self._key = key
    csvKey = None

    print(f'\n*** searching for self._key: {self._key}')
    
    # this try except is needed to handle the last group of records with same
    # csvKey
    try:
      line = next(self._openDataset)
      csvKey = line.strip()
    except StopIteration:
      yield self._buffer
      self._buffer = []

    while csvKey:
      if self._key == csvKey:
        print(f"self._key: {self._key} -- csvKey: {csvKey}")
        self._buffer.append(csvKey)
        print(f"current buffer: {self._buffer}")
      else:
        yield self._buffer

        # returns from the edit
        self._buffer = []
        self._buffer.append(csvKey)
        print(f"??? what's left ??? {self._buffer}")

        # breaks out of the while loop to get the next avaialble new key
        break

      try:
        line = next(self._openDataset)
        csvKey = line.strip()
      except StopIteration:
        yield self._buffer

        # after returns from the edit, break out of the "while-loop"
        break
    else:
      # the eof has reached; if there is anything in the buffer, send them to
      # edit
      if len(self._buffer) != 0:
        yield self._buffer


  def openDataset(self):
    return self._openDataset


  def closeDataset(self):
    self._openDataset.close()






if __name__ == '__main__':
  keys = ['1','2','3','4','5','6','7','8','9','10']
  inputFam = "PyTransPrjs\\data\\largeFam.txt"
  inputPer = "PyTransPrjs\\data\\largePer.txt"
  maxsize = 10
  keyMonitor = KeyMonitor(keys)
  famDataset = Dataset(keyMonitor, inputFam, maxsize)
  perDataset = Dataset(keyMonitor, inputPer, maxsize)

  for key in keyMonitor:
    for family in famDataset.getRecords(key):
      print(f"...found family... -> {family}")

    for persons in perDataset.getRecords(key):
      print(f"...found persons... -> {persons}")


    print(f" --------------------------- editing -> key: {key} -- family: {family}")
    print(f" --------------------------- editing -> key: {key} -- persons: {persons}")


  perDataset.closeDataset()
  famDataset.closeDataset()