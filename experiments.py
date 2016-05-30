"""
File: experiments.py
-------------------
@author jmwebb
@date 2016-05-19

Primary file that will run all experiments on Match16 data and print results.
"""

import graphutils as gu
import networkx as nx

EDGE_FILE = 'final_match16_matches.json'
NODE_FILE = 'all_nodes_final.json'


def basic_stats(graph):
    """
    Reports basic demographic statistics about the match graph.
    """
    import basic_demographic_stats as exp
    exp.calculate_node_percentages(graph)


def degree_distribution_experiments(graph):
    """
    Reports the distribution of in-links
    """
    import degree_distribution_stats as exp
    exp.in_degree_distribution(graph)


def eigenvector_demographic_popularity(graph):
    """
    Reports stats on the eigenvector centrality for
    different demographic groups.
    """
    import demographic_eigen_centrality as exp
    # We thought edges marked as 'romantic' were more interesting
    romantic_players = gu.filter(
        graph, node_filters=[
            gu.did_participate], edge_filters=[
            gu.is_romantic])
    exp.average_centralities(romantic_players)
    exp.median_centralities(romantic_players)


def match_logistic_regression(graph):
    """
    Reports results from regression run on the edgeset.
    """
    import match_logit as ml
    romanctic_players = gu.filter(
        graph, node_filters=[
            gu.did_participate], edge_filters=[
            gu.is_romantic])
    y, X = ml.create_data_matrix(romanctic_players)
    ml.cross_validation_test(X, y)
    ml.report_metics(X, y)


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
    eigenvector_demographic_popularity(match16_graph)
    match_logistic_regression(match16_graph)
