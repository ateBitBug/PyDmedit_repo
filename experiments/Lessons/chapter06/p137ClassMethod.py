class A():
  count = 0

  def __init__(self):
    A.count += 1

  def exclaim(self):
    print("i am an A")

  @classmethod
  def kids(cls):
    print("A has", cls.count, "little object")
    print("A has", A.count, "little object")



easyA = A()
breezyA = A()
wheezyA = A()
A.kids()