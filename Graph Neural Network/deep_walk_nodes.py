import networkx as nx
import pandas as pd
import ast


def read_files(file_name):
    path_instance = []
    with open(file_name) as myfile:
        for line in myfile:
            path_instance.append(ast.literal_eval(line))
        myfile.close()
    return path_instance


def calculate_path_representation(heaviest_path):
    sum_embedding = [0] * 64
    for item in heaviest_path:
        sum_embedding = sum_embedding + embedding[nodes[item]]
    return sum_embedding / len(heaviest_path)


df_result = pd.read_csv("../final_result_4.csv")
df_result.columns = ['source', 'target', 'weight', 'relation']
print(len(df_result))

G = nx.from_pandas_edgelist(df_result, source="source", target="target", edge_attr=["weight", "relation"],
                            create_using=nx.Graph)
reindexed_graph = nx.relabel.convert_node_labels_to_integers(G, first_label=0, ordering='default')
# train model and generate embedding
model = DeepWalk(walk_length=100, dimensions=64, window_size=5)
model.fit(reindexed_graph)
embedding = model.get_embedding()
nodes = G.nodes()
nodes = dict(zip(nodes, range(len(nodes))))

source_user = 830014045658812417
file_name = "../Final_Paths/" + str(source_user) + ".txt"
all_list_together = read_files(file_name)

for path in all_list_together:
    with open("embedding_830014045658812417.txt", 'a') as convert_file:
        heaviest_path = path['source']
        convert_file.write("%s\n" % calculate_path_representation(heaviest_path))
    convert_file.close()
