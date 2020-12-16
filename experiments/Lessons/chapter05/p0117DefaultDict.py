# https://stackoverflow.com/questions/9139897/how-to-set-default-value-to-all-keys-of-a-dict-object-in-python
from collections import defaultdict

animals = {"canine": 1, "feline": 2}
animals = defaultdict(lambda : -1, animals)
print(animals['canine'])
print(animals['ant'])