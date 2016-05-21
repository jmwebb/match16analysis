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
	for node in graph.nodes(data=True):
		in_degrees[graph.in_degree(node[0])] += 1

	in_degrees = sorted(in_degrees.items(), key=lambda x:x[0])

	print(in_degrees)

def in_degree_distribution_females(graph):
	in_degrees = collections.Counter()
	for node in graph.nodes(data=True):
		if node[1]['gender'] == 'Female':
			in_degrees[graph.in_degree(node[0])] += 1

	in_degrees = sorted(in_degrees.items(), key=lambda x:x[0])

	print(in_degrees)