"""
Description: https://code.google.com/codejam/contest/dashboard?c=6234486#s=p0

Solution: construct an undirected graph where the nodes are villains' names,
and edges indicate the fact that the villains don't like each other.

Then check if graph is bipartite by finding a 2-coloring of the graph.
"""

from collections import defaultdict
import sys

def build_graph(edges, unordered=False):
    """Takes some edges and constructs a graph in its adjacency list
    representation.

    edges -- an iterable of pairs of nodes
    unordered -- if `True`, will construct an unordered graph
    """

    edges = iter(edges)
    graph = defaultdict(list)

    for _ in range(num_pairs):
        a, b = next(edges)

        graph[a].append(b)
        if unordered:
            graph[b].append(a)

    return graph

def check_bipartite(graph):
    """Checks if a given graph is bipartite, that is, if it can be partitioned
    into two sets of nodes, such that there are no edges between nodes within
    each set, only edges between nodes on different sides.

    graph -- adjacency list representation of the graph
    """

    colors = {}

    def bfs(node):
        if node in colors:
            return True

        colors[node] = 1

        queue = [node]
        while queue:
            node = queue.pop()

            color = colors[node]
            neighbor_color = -1 * color

            for neighbor in graph[node]:
                if neighbor in colors:
                    if colors[neighbor] != neighbor_color:
                        return False
                else:
                    colors[neighbor] = neighbor_color
                    queue.insert(0, neighbor)

        return True

    for node in graph.keys():
        if not bfs(node):
            return False

    return True

fin = sys.stdin
fout = sys.stdout

test_cases = int(next(fin))

for case in range(test_cases):
    num_pairs = int(next(fin))

    stripped_lines = map(str.strip, fin)
    edges = map(str.split, stripped_lines)
    graph = build_graph(edges, unordered=True)

    answer = 'Yes' if check_bipartite(graph) else 'No'
    print(f'Case #{case + 1}: {answer}', file=fout)
