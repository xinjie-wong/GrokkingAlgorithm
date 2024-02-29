# Dijsktra's algorithm:
# suitable for weighted graph
# find the fastest path between two nodes
# not suitable for negative-weight edges

# create a graph
# using nested hash table
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}

# to represent infinity
infinity = float('inf')

# create a hash table to record the cost from the start to the current node
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# create another hash table to store the parents
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# create an array to keep track of all the processed nodes
processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors:
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

start = processed[len(processed) - 1]
while start is not None:
    print(start)
    if start in parents:
        start = parents[start]
    else:
        break

