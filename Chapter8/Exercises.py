# Exercise 8.1
"""
You work for a furniture company, and you have to ship furniture all over the country.
You need to pack your truck with boxes.
All the boxes are of different sizes, and you're trying to maximize the space you use in each truck.
How would you pick boxes to maximize space?
Come up with a greedy strategy. Will that give you the optimal solution?
"""
# Answer: 
# A greedy strategy is to pick the largest box that can fit in the remaining space, and repeat it until no boxes can fit in anymore.
# This might not give us an optimal solution.

# Exercise 8.2
"""
You're going to Europe, and you have seven days to see everything you can.
You assign a point value to each item (how much you want to see it) and estimate how long it takes.
How can you maximize the point total (seeing all the things you really want to see) during your stay?
Come up with a greedy strategy. Will that give you the optimal solution?
"""
# Answer:
# A greedy strategy is to pick the item with the highest point value, and repeat it until you have no time left.
# This might not give us an optimal solution.

# For each of these algorithms, say whether it's a greedy algorithm or not.
# Exercise 8.3
# Quicksort
# Asnwer: No

# Exercise 8.4
# Breadth-first search
# Answer: Yes
# Reason: it make locally optimal choices at each step by explores all the neighbor nodes before moving on to the next level of nodes

# Exercise 8.5 
# Dijkstra's algorithm
# Answer: Yes
# Reason: it make locally optimal choices at each step by explores all the neighbor nodes before moving on to the next level of nodes

# Exercise 8.6
"""
A postman needs to deliver to 20 homes. 
He needs to find the shortest route that goes to all 20 homes.
Is this an NP-complete problem?
"""
# Answer: Yes


# Exercise 8.7
"""
Finding the largest clique in a set of people (a clique is a set of people who all know each other).
Is this an NP-complete problem?
"""
# Answer: Yes


# Exercise 8.8
"""
You're making a map of the USA, and you need to color adjacent states with different coluors.
You have to find the minimum number of colours you need so that no two adjacent states are the same colour.
Is this an NP-complete problem?
"""
# Answer: Yes