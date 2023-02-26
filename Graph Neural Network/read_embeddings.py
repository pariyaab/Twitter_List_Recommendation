import ast
import json
import pandas as pd
from scipy import spatial

with open('embeddings_3.txt', 'r') as fin:
    data = fin.read().splitlines(True)
with open('file.txt', 'w') as fout:
    fout.writelines(data[1:])

user_dict = {}
list_dict = {}
with open("file.txt") as myfile:
    for line in myfile:
        line_splitted = line.split(" ")
        if line_splitted[0].startswith("L"):
            list_id = line_splitted.pop(0)
            list_id = ast.literal_eval(list_id[1:])
            embedding_vector = list(map(lambda x: ast.literal_eval(x), line_splitted))
            list_dict[list_id] = embedding_vector
        elif line_splitted[0].startswith("U"):
            user_id = line_splitted.pop(0)
            user_id = ast.literal_eval(user_id[1:])
            embedding_vector = list(map(lambda x: ast.literal_eval(x), line_splitted))
            user_dict[user_id] = embedding_vector
    myfile.close()

col_list = ["id", "name"]
df_lists = pd.read_csv('../../Dataset/lists.csv', usecols=col_list, index_col=False)
list_ids = list(df_lists['id'])
df_users = pd.read_csv('../../Dataset/users.csv', index_col=False)
user_ids = df_users['user_id'].to_list()

for source_user in user_ids:
    user_embedding = user_dict[source_user]
    file_name = str(source_user) + ".txt"
    with open(file_name, 'a') as convert_file:
        for list_target in list_ids:
            list_embedding = list_dict[list_target]
            result = 1 - spatial.distance.cosine(user_embedding, list_embedding)
            path_weights = {"source": source_user, "target": list_target, "similarities": result}
            convert_file.write(json.dumps(path_weights))
            convert_file.write("\n")
    convert_file.close()
