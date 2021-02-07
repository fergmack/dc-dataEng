# Which function is faster?
def get_publisher_heroes(heroes, publishers, desired_publisher):

    desired_heroes = []

    for i,pub in enumerate(publishers):
        if pub == desired_publisher:
            desired_heroes.append(heroes[i])

    return desired_heroes
    
def get_publisher_heroes_np(heroes, publishers, desired_publisher):

heroes_np = np.array(heroes)
pubs_np = np.array(publishers)

desired_heroes = heroes_np[pubs_np == desired_publisher]

return desired_heroes

# test runtime 
%load_ext line_profiler
%lprun -f get_publisher_heroes get_publisher_heroes(heroes, publishers, 'George Lucas')

%lprun -f get_publisher_heroes_np get_publisher_heroe_nps(heroes, publishers, 'George Lucas')
