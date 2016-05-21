"""
File: degree_distribution_stats.py
-------------------
@author jmwebb
@date 2016-05-19

Function to evaluate which node attribute is
the best predictor of a match.
"""

import networkx as nx
import collections # counter

def in_degree_distribution(graph):
	in_degrees = collections.Counter()
	high_degree = []
	for node in graph.nodes(data=True):
		in_degrees[graph.in_degree(node[0])] += 1
		if graph.in_degree(node[0]) > 10:
			high_degree.append((node[1]['gender'], graph.in_degree(node[0]), node[1]))

	high_degree = sorted(high_degree, key=lambda x:x[1])
	print(high_degree)

	print(in_degrees)