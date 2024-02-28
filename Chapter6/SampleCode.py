# Breadth-first search
# seeking for a mango seller from my network

# create a graph using dictionary
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

# create the breadth-first search algorithm:
from collections import deque   # import queue
def search(name):
    search_queue = deque()  # queue of names to be checked
    searched = []   # list of checked names
    search_queue += graph[name]     # add neighbours of the starting point into the queue
    while search_queue:
        person = search_queue.popleft()     # pick the first neighbour in the queue
        if person not in searched:
            if person_is_seller(person):
                print(person, 'is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    print('No mango seller in your network!')
    return False

def person_is_seller(name):
    return name[-1] == 'm'

search('jonny')
