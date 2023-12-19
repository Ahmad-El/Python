from py2neo import Graph, Node, Relationship
from neo4j import GraphDatabase
import json

# Connect to your Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "12345678"))

neo4j_url = "bolt://localhost:7687"  # Make sure to use the correct port
neo4j_username = "neo4j"
neo4j_password = "12345678"

# json_data = {
#     "nodes": [
#         {"id": 1, "label": "Person", "name": "Alice"},
#         {"id": 2, "label": "Person", "name": "Bob"},
#         # Add more nodes as needed
#     ],
#     "relationships": [
#         {"start_node": 1, "end_node": 2, "type": "KNOWS"},
#         # Add more relationships as needed
#     ]
# }
# for node_data in json_data.get("nodes", []):
#     # node = Node(node_data["label"], **node_data)
#     # graph.create(node)
#     print(node_data['label'])
#     print(node_data)




           
def import_json_data(json_data):
    for node_data in json_data.get("nodes", []):
        node = Node(node_data["label"], **node_data)
        graph.create(node)

    for rel_data in json_data.get("relationships", []):
        start_node = graph.nodes[rel_data["start_node"]]
        end_node = graph.nodes[rel_data["end_node"]]
        rel_type = rel_data["type"]

        # Use the Relationship class to create a relationship
        relationship = Relationship(start_node, rel_type, end_node)
        graph.create(relationship)


def import_json_data(json_data):
    for node_data in json_data.get("nodes", []):
        node = Node(node_data["label"], **node_data)
        graph.create(node)

    for rel_data in json_data.get("relationships", []):
        start_node = graph.nodes[rel_data["start_node"]]
        end_node = graph.nodes[rel_data["end_node"]]
        rel_type = rel_data["type"]

        # Use the Relationship class to create a relationship
        relationship = Relationship(start_node, rel_type, end_node)
        graph.create(relationship)


with open("output.json", "r") as file:
    json_data = json.load(file)
def get_data(json_data):
    for key in json_data:
        node = key
        values = list(json_data[key])
        for value in values:
            node = Node(value)
            graph.create(node)
        # for 
        # print(node)
        # print(values)
        
        # self.get_data(json_data[key])
    

# Import JSON data into Neo4j
# import_json_data(json_data)


# Function to import JSON data into Neo4j
def import_json_data(data, parent_node=None):
    for key, value in data.items():
        # Create a node for the current key
        current_node = Node("Page", url=key)
        graph.create(current_node)

        # Create a relationship between the current node and its parent node (if exists)
        if parent_node is not None:
            relationship = Relationship(parent_node, "HAS_LINK", current_node)
            graph.create(relationship)

        # Recursively call the function for the child nodes
        import_json_data(value, parent_node=current_node)

import_json_data(json_data)