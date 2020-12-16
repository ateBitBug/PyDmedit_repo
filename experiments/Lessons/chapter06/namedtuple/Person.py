import collections

Person = collections.namedtuple('Person', 'name age gender')
print('type of person: ', type(Person))

p1 = Person(name='bob', age=30, gender='male')
print('representation: ', p1)

print("new p1 name: ", p1.name)