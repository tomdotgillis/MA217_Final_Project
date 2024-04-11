# source .env/bin/activate

import networkx as nx
import json


# Load the JSON data from file
with open('/Users/tomgillis/Desktop/SMC/Y4/S2/Classes/MA-217/Final Project/starwars-full-interactions-allCharacters-merged.json', 'r') as f:
    data = json.load(f)
    
# Create a new graph
G = nx.Graph()
'''
node_name = str(input("Key for Nodes: "))
node_sub = str(input("Subkey for Nodes: "))
edge_name = str(input("Key for Edges: "))
'''
node_name = 'nodes'
node_sub = 'name'
edge_name = 'links'
# Add nodes
for node_data in data[node_name]:
    G.add_node(node_data[node_sub], **node_data)

# Add edges
for edge_data in data[edge_name]:
    G.add_edge(edge_data['source'], edge_data['target'], **edge_data)

# Write the graph to a GraphML file
g_name = str(input('\nName the file: '))+'.graphml'
try:
    print("nx.write_graphml(G, g_name)")
except:
    print("Something Went Wrong")
else:
    print(f"\n\n%s, saved in project dir.\n\n" % g_name)
