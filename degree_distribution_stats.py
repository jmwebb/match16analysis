"""
File: degree_distribution_stats.py
-------------------
@author jmwebb
@date 2016-05-19

A function to determine the degree distribution in the graph.
This gives us a sense of whether or not there exist people
in the graph who own a large percentage of the "preferences"
or in-links.
"""

import networkx as nx
import collections  # counter


def in_degree_distribution(graph):
    """
    Simple function that determines degree distribution.

    @param graph: the distribution will be found for this networkx graph
    """
    in_degrees = collections.Counter()
    for node in graph.nodes(data=True):
        in_degrees[graph.in_degree(node[0])] += 1

    in_degrees = sorted(in_degrees.items(), key=lambda x: x[0])

    print(in_degrees)
