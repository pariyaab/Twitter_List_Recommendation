import pandas as pd
from operator import itemgetter
import ast
import json

df_users = pd.read_csv('../Dataset/users.csv', index_col=False)
test_dataset = pd.read_csv('../Relations/Dataset/OpenHE/test_set_3.csv', index_col=False, header=None)
test_dataset.columns = ['source', 'target']
user_ids = df_users['user_id'].to_list()


def read_files(file_name):
    path_instance = []
    with open(file_name) as myfile:
        for line in myfile:
            path_instance.append(line)
        myfile.close()
    return path_instance


def sort_target_nodes_based_on_similarities(path_instances):
    path_instance_changed = []
    for item in path_instances:
        path_instance_changed.append(ast.literal_eval(item))

    newlist = sorted(path_instance_changed, key=itemgetter('similarities'), reverse=True)
    return newlist


def find_recommend_lists_ids(path_instance):
    all_lists = []
    for item in path_instance:
        all_lists.append(item["target"])
    return all_lists


sum_of_mpr = 0.0


def calculate_mpr(all_list, target_id):
    global sum_of_mpr
    index_of_test_list = all_list.index(target_id[0])
    sum_of_mpr = sum_of_mpr + (index_of_test_list / 1534)


def calculate_metrics():
    for source_user in user_ids[:5]:
        print(source_user)
        # file_name = "KGAT_paths/" + str(source_user) + ".txt"
        file_name = "KGAT_Paths_all_relations/" + str(source_user) + ".txt"
        all_list_together = read_files(file_name)
        recommend_list = sort_target_nodes_based_on_similarities(all_list_together)
        recommendation_list_ids = find_recommend_lists_ids(recommend_list)
        test_target_id = (test_dataset.loc[(test_dataset['source'] == source_user)])['target'].to_list()
        calculate_mpr(recommendation_list_ids, test_target_id)


calculate_metrics()
print(sum_of_mpr / 1284)
