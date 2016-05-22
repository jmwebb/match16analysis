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
	print('\t{0:11.11}:\t{1}\t{2:5.5}%'.format(demographic_string, attribute_counts[demographic_string],attribute_counts[demographic_string]/total_nodes))

def _print_demo_sector(total_nodes, attribute_counts):
	print('-' * 60)	
	for attribute, count in sorted(attribute_counts.items(), key=lambda x: -x[1]):
		if attribute != 'No Data' and attribute != 'Prefer Not To Answer':
			_percent_print(attribute, total_nodes, attribute_counts)
	_percent_print('Prefer Not To Answer', total_nodes, attribute_counts)
	_percent_print('No Data', total_nodes, attribute_counts)	

def calculate_node_percentages(graph):
	total_nodes = graph.number_of_nodes()
	gender_counts = collections.Counter()
	major_counts = collections.Counter()
	ec_counts = collections.Counter()
	for node in graph.nodes(data=True):
		gender = node[1]['gender']
		major = node[1]['area_of_study']
		extra_currics = node[1]['extra_curricular']
		gender_counts[gender] += 1
		major_counts[major] += 1
		for ec in extra_currics:
			ec_counts[ec] += 1

	print('Basic Demographic Stats:')
	print('-' * 60)
	print('Total nodes: {}'.format(total_nodes))
	print('-' * 60)
	print('Gender stats:')
	_print_demo_sector(total_nodes, gender_counts)
	print('Major stats:')
	_print_demo_sector(total_nodes, major_counts)
	print('Extracurricular stats:')
	_print_demo_sector(total_nodes, ec_counts)
	
	