"""
File: match_version_splitter.py
-------------------
@author jmwebb
@date 2016-05-19

Simple function to divide data dump into 2 files,
one for match8 and one for match16.
"""
import json

UNSPLIT_FILE = 'all_matches_final.json'

if __name__ == '__main__':
    with open(UNSPLIT_FILE) as f:
        edge_list = json.load(f)

    edges16 = [edge for edge in edge_list if edge[
        'match_session'] == 'Match16']
    edges8 = [edge for edge in edge_list if edge['match_session'] == 'Match8']

    with open('final_match16_matches.json', 'w') as f:
        f.write(json.dumps(edges16))
    with open('final_match8_matches.json', 'w') as f:
        f.write(json.dumps(edges8))
