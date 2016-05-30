"""
File: graphutils.py
-------------------
@author jmwebb
@date 2016-05-19

Lightweight utility library to work with Match16 data.
"""

import json
import networkx as nx


def load_nodes_and_edges(json_filename, json_attribute_filename):
    """
    Easy to use wrapper for two json loading functions. Produces
    a networkx graph with detailed nodes.

    @param json_filename: json file containing edge list
    @param json_attribute_filename: json file containing node attributes
    @return networkx graph
    """
    g = json_to_graph(json_filename)
    add_node_attributes(json_attribute_filename, g)
    return g


def json_to_graph(json_filename):
    """
    Converts a json file of edges into a networkx directed graph.
    Edge file must be formatted to include a 'recipient_id', 'creator_id',
    as well as a 'purpose' attribute.

    @param json_filename: json file containing edge list
    @return networkx graph
    """
    directed_graph = nx.DiGraph()
    with open(json_filename) as f:
        edge_list = json.load(f)

    for edge in edge_list:
        directed_graph.add_edge(
            edge['creator_id'],
            edge['recipient_id'],
            purpose=edge['purpose'])

    return directed_graph


def add_node_attributes(json_attribute_filename, graph):
    """
    Adds attributes from provided json file to nodes in provided graph.
    Attribute file must be formatted to include 'gender', 'area_of_study',
    and 'extra_curricular' attributes.
    'extra_curricular' should be a semi-colon separated list.

    @param json_attribute_filename: json file containing node attributes
    @param graph: networkx graph containing nodes to be modified
    """
    with open(json_attribute_filename) as f:
        node_list = json.load(f)

    for node in node_list:
        # Ignores nodes in attribute list that don't exist in graph
        if node['anon_id'] in graph.nodes():
            graph.node[node['anon_id']]['gender'] = node['gender']
            # Blank fields are replaced with "No Data" for consistency
            if node['area_of_study'] == '':
                node['area_of_study'] = 'No Data'
            graph.node[node['anon_id']][
                'area_of_study'] = node['area_of_study']
            if node['extra_curricular'] == '':
                node['extra_curricular'] = 'No Data'
            graph.node[node['anon_id']]['extra_curricular'] = node[
                'extra_curricular'].split(';')


def print_graph(graph):
    """
    Pretty print feature for provided graph. Displays attributes
    and edges for each node.

    @param graph: networkx graph to be printed
    """
    for node in graph.nodes_iter(data=True):
        print('-' * 60)
        print(
            'Node ID: {node_id}\n\tGender:\t{gender}\n\tMajor:\t{major}\n\tActivities:\t{ec_list}'.format(
                node_id=node[0],
                gender=node[1]['gender'],
                major=node[1]['area_of_study'],
                ec_list=', '.join(
                    node[1]['extra_curricular'])))
        for idx, predecessor_id in enumerate(graph.predecessors_iter(node[0])):
            purpose = graph.edge[predecessor_id][node[0]]['purpose']
            if idx == 0:
                print(
                    '\tIn-links from:\t{node_id}\t{purpose}'.format(
                        node_id=predecessor_id,
                        purpose=purpose))
            else:
                print(
                    '\t\t\t{node_id}\t{purpose}'.format(
                        node_id=predecessor_id,
                        purpose=purpose))
        print()
        for idx, successor_id in enumerate(graph.successors_iter(node[0])):
            purpose = graph.edge[node[0]][successor_id]['purpose']
            if idx == 0:
                print(
                    '\tOut-links to:\t{node_id}\t{purpose}'.format(node_id=successor_id, purpose=purpose))
            else:
                print(
                    '\t\t\t{node_id}\t{purpose}'.format(
                        node_id=successor_id,
                        purpose=purpose))
    print('-' * 60)


def filter(graph, node_filters=[], edge_filters=[]):
    """
    Creates a new graph representing only the nodes and
    edges that passed the given filter functions.

    @param graph: graph to filter
    @param node_filters: filters to be applied to the graph nodes
    @param edge_filters: filters to be applies to the graph edges
    @return the filtered graph
    """
    filtered_graph = nx.DiGraph(graph)
    for predicate in node_filters:
        for node in filtered_graph.nodes(data=True)[:]:
            if not predicate(graph, *node):
                filtered_graph.remove_node(node[0])
    for predicate in edge_filters:
        for edge in filtered_graph.edges(data=True)[:]:
            if not predicate(graph, *edge):
                filtered_graph.remove_edge(edge[0], edge[1])
    for node in filtered_graph.nodes()[:]:
        if filtered_graph.in_degree(
                node) == 0 and filtered_graph.out_degree(node) == 0:
            filtered_graph.remove_node(node)
    return filtered_graph


def count_shared_activities(graph, creator_id, recipient_id, attributes):
    """
    Counts the activities shared by the two nodes of an edge.

    @param graph: the graph the edge belongs to
    @param creator_id: the id of the first node of the edge
    @param recipient_id: the id of the second node of the edge
    @param attributes: dictionary of edge attributes
    return the number of activities in common
    """
    return len(set(graph.node[creator_id]['extra_curricular']).intersection(
        set(graph.node[recipient_id]['extra_curricular'])))


#####################################################
#                                                   #
#         Useful filters for edges/nodes            #
#                                                   #
#####################################################

def is_male(graph, node_id, attributes):
    return attributes['gender'] == 'Male'


def is_female(graph, node_id, attributes):
    return attributes['gender'] == 'Female'


def is_romantic(graph, creator_id, recipient_id, attributes):
    return attributes['purpose'] == 'Romance'


def did_participate(graph, node_id, attributes):
    return attributes['gender'] != 'No Data'


def is_reciprocated(graph, creator_id, recipient_id, attributes):
    return creator_id in graph.successors(recipient_id)


def is_same_gender(graph, creator_id, recipient_id, attributes):
    return graph.node[creator_id][
        'gender'] == graph.node[recipient_id]['gender']


def is_same_major(graph, creator_id, recipient_id, attributes):
    return graph.node[creator_id]['area_of_study'] == graph.node[
        recipient_id]['area_of_study']
