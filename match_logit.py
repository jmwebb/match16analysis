"""
File: match_logit.py
-------------------
@author jmwebb
@date 2016-05-28

Logistic regression model to predict if an edge
will be reciprocated. Uses sklearn's logistic
regression module as well as some validation
modules. Also will be used to demonstrate the
correspondence of various features with the
likelihood to match.

Features for each edge include:
- are the two nodes of the edge the same gender
- are they the same major
- the count of activities they have in common
- the ratio of their eigenvector centralities
"""

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn.cross_validation import cross_val_score
import numpy as np
import graphutils as gu
import networkx as nx


column_names = [
    'same_gender',
    'same_major',
    'shared_activities',
    'eigenvec_ratio',
    'is_reciprocated']


def _create_row(graph, edge, eigen_centralities):
    """
    Creates a feature vector for a given edge.

    @param graph: the graph the edge belongs to
    @param edge: the edge being featurized
    @param eigen_centralities: a map of eigenvector centralities for all nodes
    return a feature array for the given edge
    """
    same_gender_indicator = int(gu.is_same_gender(graph, *edge))
    same_major_indicator = int(gu.is_same_major(graph, *edge))
    num_shared_activities = gu.count_shared_activities(graph, *edge)
    if eigen_centralities[edge[1]] != 0:
        eigenvec_ratio = eigen_centralities[
            edge[0]] / eigen_centralities[edge[1]]
    else:
        eigenvec_ratio = 0
    match_indicator = int(gu.is_reciprocated(graph, *edge))
    return [
        same_gender_indicator,
        same_major_indicator,
        num_shared_activities,
        eigenvec_ratio,
        match_indicator]


def create_data_matrix(graph):
    """
    Creates a matrix from the given graph where each row is
    the feature vector for a given edge, and the output is
    whether or not that edge is reciprocated (i.e. a match).
    @param graph: the graph to turn into a matrix
    return a tuple of the outputs and data matrix
    """
    # Getting all eigen centralities here to avoid recalculation
    eigen_centralities = nx.eigenvector_centrality(graph)
    all_data = np.array([_create_row(graph, edge, eigen_centralities)
                         for edge in graph.edges(data=True)])
    return all_data[:, -1], all_data[:, :-1]


def cross_validation_test(X, y):
    """
    Reports the accuracy of the logistic regression use
    10-fold cross-validation.

    @param X: the data matrix
    @param y: the outputs
    """
    scores = cross_val_score(
        LogisticRegression(),
        X,
        y,
        scoring='accuracy',
        cv=10)
    print('Logistic Regression Cross-validation accuracy: {}'.format(scores.mean()))


def report_metics(X, y):
    """
    Reports the classification stats (accuracy, precision, recall, f1)
    using a 30-70 split on the data matrix. Also reports the weight vector
    of the regressor so we can see how different features correlated with the likelihood
    of a match.

    @param X: the data matrix
    @param y: the outputs
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=0)
    model = LogisticRegression()
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    print(metrics.classification_report(y_test, predicted))
    print('Weight vector for model:')
    print(list(zip(column_names[:-1], np.transpose(model.coef_))))
