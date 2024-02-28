# Graph:
# consists of nodes and edges
# utilises hash table to create the graph
# map a node (key) to its neighbours (values)

# Breadth-first search:
# runs on graph
# use to solve questions:
# - is there a path from node A to node B?
# - what is the shortest path from node A to node B?
# use queue (first-in-first-out) to store all the nodes
# check from first degree connection to second degree connection to ....
# run time:
# O(V + E)
# where V = number of vertices/nodes, E = number of edges
# only suitable for unweighted graph
