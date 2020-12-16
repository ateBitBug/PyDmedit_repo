class Duck():
  def __init__(self, inputName):
    self.hiddenName = inputName

  @property
  def hName(self):
    print("inside the getter")
    return self.hiddenName

  @hName.setter
  def hName(self, inputName):
    print("inside the setter")
    self.hiddenName = inputName

fowl = Duck("howard")
print(fowl.hName)

fowl.hName = "daffy duck"
print(fowl.hName)

'''*
  accessing self.hiddenName -> cause no error
*'''
fowl.hiddenName = "donald duck"