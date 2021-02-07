# Combine all three lists together
# The secondary_types list contains the corresponding secondary type of each Pokémon (nan if the Pokémon has only one type).
names = ['Abomasnow', 'Abra']
primary_types = ['Grass', 'Psychic']
secondary_types = ['Ice', 'nan']


names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')

# Combine five items from names and three items from primary_types
# Note that if you provide zip() with objects of differing lengths, it will only combine until the smallest lengthed object is exhausted?
differing_lengths = [*zip(names[:5], primary_types[:3])]

print(*differing_lengths, sep='\n')
