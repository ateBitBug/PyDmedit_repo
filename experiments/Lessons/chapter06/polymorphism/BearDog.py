class Bear(object):
  def sound(self):
    print("Groarrrr")

class Dog(object):
  def sound(self):
    print("woof woof")


def makeSound(animalType):
  animalType.sound()


bear = Bear()
dog = Dog()

makeSound(bear)
makeSound(dog)