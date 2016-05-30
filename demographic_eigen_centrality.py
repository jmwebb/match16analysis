"""
File: demographic_eigen_centrality.py
-------------------
@author jmwebb
@date 2016-05-19

Experiment to determine which demographic groups have the
highest average/median eigenvector centrality.
"""

import networkx as nx
import math


def _map_print(key, value):
    """
    Pretty print feature for key-value pairs
    """
    print(
        '\t{0:11.11}:\t{1}\t'.format(
            key, value))


def _print_average_demo(eigenvec_centrality_totals):
    """
    Calculates and prints the average eigenvector centrality
    for a given demographic group.

    @param eigenvec_centrality_totals: a dict mapping a demographic to
        a list of the eigenvector centrality for all nodes in that demographic
    """
    averages = {}
    print('-' * 60)
    for attribute in eigenvec_centrality_totals:
        averages[attribute] = sum(eigenvec_centrality_totals[
                                  attribute]) / len(eigenvec_centrality_totals[attribute])

    for attribute, average in sorted(
            averages.items(), key=lambda x: -x[1]):
        _map_print(attribute, average)


def _print_median_demo(eigenvec_centrality_totals):
    """
    Calculates and prints the average eigenvector centrality
    for a given demographic group.

    @param eigenvec_centrality_totals: a dict mapping a demographic to
        a list of the eigenvector centrality for all nodes in that demographic
    """
    medians = {}
    print('-' * 60)
    for attribute in eigenvec_centrality_totals:
        sort = sorted(eigenvec_centrality_totals[attribute])
        medians[attribute] = sort[math.floor(len(sort) / 2)]

    for attribute, median in sorted(medians.items(), key=lambda x: -x[1]):
        _map_print(attribute, median)


def _calc_centrality_totals(graph):
    """
    Calculates the eigenvector centrality for every node in
    a graph, then assigns those centralities to different
    demographic groups.

    @param graph: the graph to calculate centrality for
    @return a dict mapping gender string to list of centralities
    @return a dict mapping major name to list of centralities
    @return a dict mapping activity name to list of centralities
    """
    eigen_centralities = nx.eigenvector_centrality(graph)
    gender_eigen_totals = {}
    major_eigen_totals = {}
    ec_eigen_totals = {}
    for node in graph.nodes(data=True):
        gender = node[1]['gender']
        major = node[1]['area_of_study']
        extra_currics = node[1]['extra_curricular']
        if gender in gender_eigen_totals:
            gender_eigen_totals[gender].append(eigen_centralities[node[0]])
        else:
            gender_eigen_totals[gender] = []
        if major in major_eigen_totals:
            major_eigen_totals[major].append(eigen_centralities[node[0]])
        else:
            major_eigen_totals[major] = []
        for ec in extra_currics:
            if ec in ec_eigen_totals:
                ec_eigen_totals[ec].append(eigen_centralities[node[0]])
            else:
                ec_eigen_totals[ec] = []

    return gender_eigen_totals, major_eigen_totals, ec_eigen_totals


def average_centralities(graph):
    """
    Finds the average eigenvector centrality across all demographic groups
    in the provided graph.
    """
    gender_eigen_totals, major_eigen_totals, ec_eigen_totals = _calc_centrality_totals(
        graph)

    print('Average Eigenvector Centrality by Demographic:')
    print('-' * 60)
    print('Gender stats:')
    _print_average_demo(gender_eigen_totals)
    print('Major stats:')
    _print_average_demo(major_eigen_totals)
    print('Extracurricular stats:')
    _print_average_demo(ec_eigen_totals)


def median_centralities(graph):
    """
    Finds the median eigenvector centrality across all demographic groups
    in the provided graph.
    """
    gender_eigen_totals, major_eigen_totals, ec_eigen_totals = _calc_centrality_totals(
        graph)

    print('Median Eigenvector Centrality by Demographic:')
    print('-' * 60)
    print('Gender stats:')
    _print_median_demo(gender_eigen_totals)
    print('Major stats:')
    _print_median_demo(major_eigen_totals)
    print('Extracurricular stats:')
    _print_median_demo(ec_eigen_totals)
