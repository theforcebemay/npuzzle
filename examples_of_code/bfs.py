from implementation import *

def breadth_first_search_1(graph, start):
    frontier = []
    frontier.append(start)
    visited = {}
    visited[start] = True
    
    while frontier:
        print("Visited : %s" % visited)
        current = frontier.pop(0)
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.append(next)
                print("Appended {} to frontier".format(next))
                visited[next] = True

breadth_first_search_1(example_graph, 'A')
