# Get combindations of poke_types - note, if we have Bug, Fire, then we don't want to include Fire, Bug
poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
combos = [] 

for x in poke_types:
  for y in poke_types:
    if x == y:
      continue
    # makes sure, for example, that if bug, fire is in the list, it doesn't include fire, bug in the list
    if ((x, y) not in combos) & ((y, x) not in combos):
      combos.append((x, y))

print(combos)

# a faster way of doing the above
from itertools import combinations 
combos_obj = combinations(poke_types, 2)
print(type(combos_obj))

combos = [*combos_obj]
print(combos)
