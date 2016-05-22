"""
File: experiments.py
-------------------
@author jmwebb
@date 2016-05-19

Primary file that will run all experiments on Match16 data and print results.
"""

import graphutils as gu
import networkx as nx
# import matplotlib.pyplot as plt

EDGE_FILE = 'final_match16_matches.json'
NODE_FILE = 'all_nodes_final.json'


def degree_distribution_experiments(graph):
    import degree_distribution_stats as exp
    exp.in_degree_distribution(graph)

def basic_stats(graph):
    import basic_demographic_stats as exp
    exp.calculate_node_percentages(graph)


if __name__ == "__main__":
    print('Reading edge data from {}...'.format(EDGE_FILE))
    match16_graph = gu.json_to_graph(EDGE_FILE)
    print('Generated graph with {0} nodes and {1} edges!'.format(
        match16_graph.number_of_nodes(), match16_graph.number_of_edges()))
    print('Adding attributes to nodes...')
    gu.add_node_attributes(NODE_FILE, match16_graph)
    print('Node attributes added!')
    degree_distribution_experiments(match16_graph)
    basic_stats(match16_graph)
