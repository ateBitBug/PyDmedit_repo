class Duck():
  def __init__(self, inputName):
    self.hiddenName = inputName

  def getName(self):
    print("inside the getter")
    return self.hiddenName

  def setName(self, inputName):
    print("inside the setter")
    self.hiddenName = inputName

  name = property(getName, setName)



fowl = Duck("howard")
print(fowl.name)
fowl.name = "sammy"
print(fowl.name)