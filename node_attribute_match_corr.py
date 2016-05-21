"""
File: node_attribute_match_corr.py
-------------------
@author jmwebb
@date 2016-05-19

Function to evaluate which node attribute is
the best predictor of a match.
"""

def node_attribute_matches(matches_graph):
	activity_matches = matches_for_attribute(graph, 'extra_curricular')
	study_matches = matches_for_attribute(graph, 'area_of_study')
	match_count = matches_graph.edges_in_graph()/2.0
	