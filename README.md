# match16analysis

## Project overview

This project is a suite of experiments to help better understand the data collected from Match16, a web-based dating/crushes application for Stanford c/o 2016. All seniors who participated were asked to fill out a survey detailing some basic demographic information about themselves (gender, area of study, and extracurricular activities). Participants then were asked to fill out a form where they could list up 16 other seniors that they either wanted to date or get to know better. Participants had the option of marking the other senior as a romantic or plutonic preference. Roughly 700 seniors participated. Here are some preliminary findings from the experiments included in this iteration:

* There was some wild variance in the number of in-links between nodes. We found that one female participant was written down as a preference by 66 other people. This was the highest in-degree we saw. The highest in-degree for a male participant was 45.
* Engineers and seniors involved with Greek life played the game most, constituting 22 and 13 percent of the participants, respectively.
* Through several experiments assessing the "desirability" of certain demographics, we determined females are more desired than males. The most desired areas of study were Performing Arts and the Humanities; much to our chagrin, the least were Physical and Mathematical Science and Engineering. The most desired extracurricular activities were, unsurprisingly, varsity athletics and Greek life; the least were religious life clubs and research groups. We leave a determination of our society's priorities as an exercise to the reader.
* Through several experiments we attempted to discern what attributes of a pairing corresponded with a likelihood to match. In layman's terms, if you wanted to match with someone, your best shot for a match was to choose someone who is outside your area of study, who shares extracurriculars with you, and who is "less popular" than you.

## Set-up and execution instructions

### System requirements

This codebase/instructions have only been tested with the following setup:
* Mac running OSX El Capitan
* Python3
* A working version of `pip` installed

### Set-up

Getting things up and running is very easy. After downloaing the codebase, we first have to set-up a virtual environment. If you do not already have `virtualenv` installed on your machine, run the following line on your terminal:

```
$ pip install virtualenv
```

Next to get the virtual environment running on your terminal, run the following command:

```
$ source venv/bin/activate
```

Once the virtual environment is running (you will be able to tell because `(venv)` will be added to your bash shell), you will need to install the required libraries. Do so by running:

```
$ pip install -r requirements.txt
```

### Execution

Execution simply requires the following line be ran:

```
$ python experiments.py
```

This will launch the experiments and start printing results to the console.

## Technical overview

### experiments.py
This file contains the "main" function necessary for running this entrie suite. The code is laid out in a functional programming paradigm. There are no objects except those provided by third parties. This decision was made because each module contains a single experiment, which is run once and never called again. Thus, we felt we did not need the data storage and attributes enabled by an object-oriented design. The experiments.py file works as a controller, importing and executing the public API for each experiment.

### graphutils.py
This is our lightweight utility library to work with Match16 data. It comes with several functions for loading and filtering networkx graphs as well as a suite of filters that can easily be applied to the graph.

**Public API:**
* **load_nodes_and_edges:** Easy to use wrapper for two json loading functions. Produces a networkx graph with detailed nodes.
* **json_to_graph:** Converts a json file of edges into a networkx directed graph. Edge file must be formatted to include a 'recipient_id', 'creator_id', as well as a 'purpose' attribute.
* **add_node_attributes:** Adds attributes from provided json file to nodes in provided graph. Attribute file must be formatted to include 'gender', 'area_of_study', and 'extra_curricular' attributes. 'extra_curricular' should be a semi-colon separated list.
* **print_graph:** Pretty print feature for provided graph. Displays attributes and edges for each node.
* **filter:** Creates a new graph representing only the nodes and edges that passed the given filter functions.

### basic_demographic_stats.py
This experiment calculates basic stats about the demographics of the graph nodes.

**Public API:**
* **calculate_node_percentages:** Calculates the demographic make-up of the graph and reports.

### degree_distribution_stats.py
This experiment determines the degree distribution in the graph. This gives us a sense of whether or not there exist people in the graph who own a large percentage of the "preferences" or in-links.

**Public API:**
* **in_degree_distribution:** determines in-link distribution

### demographic_eigen_centrality.py
This experiment determines which demographic groups have the highest average/median eigenvector centrality.

**Public API:**
* **average_centralities:** Finds the average eigenvector centrality across all demographic groups in the provided graph.
* **median_centralities:** Finds the median eigenvector centrality across all demographic groups in the provided graph.

### match_logit.py
Logistic regression model to predict if an edge will be reciprocated. Uses sklearn's logistic regression module as well as some validation modules. Also will be used to demonstrate the correspondence of various features with the likelihood to match.

**Public API:**
* **create_data_matrix:** Creates a matrix from the given graph where each row is the feature vector for a given edge, and the output is whether or not that edge is reciprocated (i.e. a match).
* **cross_validation_test:** Reports the accuracy of the logistic regression use 10-fold cross-validation.
* **report_metics:** Reports the classification stats (accuracy, precision, recall, f1) using a 30-70 split on the data matrix. Also reports the weight vector of the regressor so we can see how different features correlated with the likelihood of a match.

## Acknowledgements

We would like to thank Dr. Dan McFarland at Stanford University for his indispensible advice and guidance in this project. Also thank you to the Senior Class Presidents for allowing us to have some fun with the data. Finally, thank you to the rest of the Match16 team: John and Peter, you guys rock.

> written by @jmwebb