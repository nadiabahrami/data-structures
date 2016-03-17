# -*- coding: utf-8 -*-
"""Simple grpah construction.
Once you have a grasp of the basic idea, implement a simple graph (unweighted, directed) in Python. You may use any of the Python primitive data types that are available without importing any additional libraries (str, unicode, dict, list, tuple).

Your graph should support the following operations:

g.nodes(): return a list of all nodes in the graph
g.edges(): return a list of all edges in the graph
g.add_node(n): adds a new node ‘n’ to the graph
g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
g.del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
Begin by creating a new branch “simple_graph” in your data-structures repository. For each method of your graph class (including the constructor), write tests first that demonstrates the functionality of that method, then implement the method to make the tests pass.

Focus on making small, atomic commits to git with well-written and meaningful commit messages.

Remember to update your README file with a description of this new data type as well as any additional sources, references or collaborations you may have used in completing the work.

"""


class Node(object):
    """Initializes a node"""

    def __init__(self, value=None):
        self.value = value

class SimpleGraph(object)
