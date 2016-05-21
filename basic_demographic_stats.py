"""
File: basic_demographic_stats.py
-------------------
@author jmwebb
@date 2016-05-21

Function to calculate basic stats
about the demographics of the graph nodes.
"""

import collections

def _percent_print(demographic_string, total_nodes, attribute_counts):
	print('\t{0} nodes: {1}\t{2}%'.format(demographic_string, attribute_counts[demographic_string],attribute_counts[demographic_string]/total_nodes))

def calculate_node_percentages(graph):
	total_nodes = graph.number_of_nodes()
	attribute_counts = collections.Counter()
	for node in graph.nodes(data=True):
		gender = node[1]['gender']
		major = node[1]['area_of_study']
		extra_currics = node[1]['extra_curricular']
		attribute_counts[gender] += 1
		attribute_counts[major] += 1
		for ec in extra_currics:
			attribute_counts[ec] += 1

	print('Basic Demographic Stats:')
	print('\tTotal nodes: {}'.format(total_nodes))
	for attribute in attribute_counts.keys()
		_percent_print('Male', total_nodes, attribute_counts)	
	