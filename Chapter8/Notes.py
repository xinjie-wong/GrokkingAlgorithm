# Greedy algorithm:
# at each step pick the locally optimal solution and in the end we will get a global optimal solution
# sometimes might not return the optimal solution, but a 'pretty close' solution
# easy to write and fast to run, making good approximation algorithms
# to determine if it's a NP-complete problem:
# - algorithm runs quickly with a handful of items but really slows down withh more items
# - 'all combinations of X'
# - involves a sequence/set and it is hard to solve
# - might need to calculate every possible solution when it is hard to break down into smaller sub-problems



# Example: Finding the smallest subset of radio stations that can cover the most states

# create a set of states
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# create a hash table to list the stations and the states they cover
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# create a set that will hold the final set of stations that we'll use
final_stations = set()

while states_needed:
    best_station = None     # will hold the station that covers the most uncovered stations
    states_covered = set()      # a set of all the states this station covers that haven't been covered yet
    for station, states_for_stations in stations.items():
        covered = states_needed & states_for_stations
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)



