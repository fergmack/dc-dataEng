# Combine all three lists together
# The secondary_types list contains the corresponding secondary type of each Pokémon (nan if the Pokémon has only one type).
names = ['Abomasnow', 'Abra']
primary_types = ['Grass', 'Psychic']
secondary_types = ['Ice', 'nan']


names_types = [*zip(names, primary_types, secondary_types)]

print(*names_types[:5], sep='\n')
