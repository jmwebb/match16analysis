"""
File: experiments.py
-------------------
@author jmwebb
@date 2016-05-19

Primary file that will run all experiments on Match16 data and print results.
"""

import graphutils as gu
import networkx as nx
import matplotlib.pyplot as plt

EDGE_FILE = 'final_match16_matches.json'
NODE_FILE = 'all_nodes_final.json'

def is_athlete(graph, node_id, attributes):
    return 'Varsity Athletics' in attributes['extra_curricular']

def is_romantic(graph, creator_id, recipient_id, attributes):
    return attributes['purpose'] == 'Romance'

def is_friendship(graph, creator_id, recipient_id, attributes):
    return attributes['purpose'] == 'Friend'

def is_romantic(graph, creator_id, recipient_id, attributes):
    return attributes['purpose'] == 'Romance'

def is_reciprocal(graph, creator_id, recipient_id, attributes):
    return (recipient_id, creator_id) in graph.edges()

def played_game(graph, node_id, attributes):
    return graph.out_degree(node_id) > 0

def has_matches(graph, node_id, attributes):
    return len(set(graph.successors(node_id)) & set(graph.predecessors(node_id))) >= 1

def is_female(graph, node_id, attributes):
    return attributes['gender'] == 'Female'

def degree_distribution_experiments(graph):
    import degree_distribution_stats as dds
    dds.in_degree_distribution(graph)


if __name__ == "__main__":
    print('Reading edge data from {}...'.format(EDGE_FILE))
    match16_graph = gu.json_to_graph(EDGE_FILE)
    print('Generated graph with {0} nodes and {1} edges!'.format(match16_graph.number_of_nodes(), match16_graph.number_of_edges()))
    print('Adding attributes to nodes...')
    gu.add_node_attributes(NODE_FILE, match16_graph)
    print('Node attributes added!')
    degree_distribution_experiments(match16_graph)
