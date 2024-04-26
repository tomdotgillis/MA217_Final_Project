import networkx as nx
import json

# Load the JSON data from file
with open('/Users/tomgillis/Desktop/SMC/Y4/S2/Classes/MA-217/Final Project/starwars-full-interactions-allCharacters-merged.json', 'r') as f:
    data = json.load(f)
    
# Create a new graph
G = nx.Graph()

# Add nodes with numerical IDs
for idx, node_data in enumerate(data['nodes']):
    G.add_node(idx, **node_data)

# Add edges
for edge_data in data['links']:
    G.add_edge(edge_data['source'], edge_data['target'], **edge_data)

# Write the graph to a GraphML file
g_name = input('\nName the file: ') + '.graphml'
try:
    nx.write_graphml(G, g_name)
except Exception as e:
    print("Something Went Wrong:", e)
else:
    print(f"\n\n{g_name}, saved in project dir.\n\n")
