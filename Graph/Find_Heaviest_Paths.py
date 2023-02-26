import heapq
import json
import os

import networkx as nx

# build graph with networkx
import pandas as pd

df_result = pd.read_csv("final_result.csv")
df_result.columns = ['source', 'target', 'weight', 'relation']
G = nx.from_pandas_edgelist(df_result, source="source", target="target", edge_attr=["weight", "relation"],
                            create_using=nx.Graph)


def heuristic(G, node, goal):
    """
    A heuristic function for A* algorithm.
    It returns the weight of the heaviest edge
    between the current node and the goal node.
    """
    heaviest_edge = 0
    for neighbor in G.neighbors(node):
        if neighbor == goal:
            edge_weight = G[node][neighbor]['weight']
            if edge_weight > heaviest_edge:
                heaviest_edge = edge_weight
        else:
            for n in G.neighbors(neighbor):
                if n == goal:
                    edge_weight = G[node][neighbor]['weight'] + G[neighbor][n]['weight']
                    if edge_weight > heaviest_edge:
                        heaviest_edge = edge_weight
    return heaviest_edge


def astar_path(G, source, target, max_path_length=None):
    """
    A* algorithm to find the heaviest path between source and target nodes in G.
    """
    heap = [(0, source)]
    visited = set()
    path = {}
    g = {node: -float('inf') for node in G.nodes()}
    g[source] = 0
    path_length = {node: 0 for node in G.nodes()}
    path_length[source] = 1

    while heap:
        _, node = heapq.heappop(heap)

        if node == target:
            # Build the path from source to target
            full_path = [target]
            while full_path[-1] != source:
                full_path.append(path[full_path[-1]])
            full_path.reverse()
            weight = sum([G[full_path[i]][full_path[i + 1]]['weight'] for i in range(len(full_path) - 1)])
            return full_path, weight

        visited.add(node)

        for neighbor in G.neighbors(node):
            if neighbor in visited:
                continue

            tentative_g = g[node] + G[node][neighbor]['weight']
            if tentative_g > g[neighbor]:
                # Check if the length of the path is less than or equal to the max_path_length
                if max_path_length is None or path_length[node] + 1 <= max_path_length:
                    g[neighbor] = tentative_g
                    f = tentative_g + heuristic(G, neighbor, target)
                    heapq.heappush(heap, (f, neighbor))
                    path[neighbor] = node
                    path_length[neighbor] = path_length[node] + 1

    return None, None


col_list = ["id", "name"]
df_lists = pd.read_csv('../../Dataset/lists.csv', usecols=col_list, index_col=False)
target_nodes = list(df_lists['id'])
df_users = pd.read_csv('../../Dataset/users.csv', index_col=False)
user_ids = df_users['user_id'].to_list()

user_ids = user_ids[1036:1050]

for source_user in user_ids:
    print(source_user)
    file_name = "../path/" + str(source_user) + ".txt"
    with open(file_name, 'a') as convert_file:
        for item in target_nodes:
            try:
                heaviest_path, heaviest_weight = astar_path(G, source_user, item, max_path_length=6)
                if heaviest_path == None:
                    heaviest_path, heaviest_weight = astar_path(G, source_user, item, max_path_length=7)
                path_weights = {"source": heaviest_path, "weight": heaviest_weight / (len(heaviest_path) - 1)}
            except:
                heaviest_path, heaviest_weight = astar_path(G, source_user, item, max_path_length=8)
                if heaviest_path == None:
                    path_weights = {"source": [source_user, item], "weight": 0.0}
                else:
                    path_weights = {"source": heaviest_path, "weight": heaviest_weight / (len(heaviest_path) - 1)}
            convert_file.write(json.dumps(path_weights))
            convert_file.write("\n")
    convert_file.close()
