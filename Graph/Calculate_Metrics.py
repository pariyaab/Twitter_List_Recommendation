import pandas as pd
from operator import itemgetter
import ast
import json

df_users = pd.read_csv('../Dataset/users.csv', index_col=False)
df_user_list_subscribe = pd.read_csv('../Dataset/ratings.csv', index_col=False, header=None)
df_user_list_subscribe.columns = ['source', 'target', 'weight']
user_ids = df_users['user_id'].to_list()

def read_files(file_name):
    path_instance = []
    with open(file_name) as myfile:
        for line in myfile:
            path_instance.append(line)
        myfile.close()
    return path_instance


def find_top_k_weights(path_instances, k):
    path_instance_changed = []
    for item in path_instances:
        path_instance_changed.append(ast.literal_eval(item))

    newlist = sorted(path_instance_changed, key=itemgetter('similarities'), reverse=True)
    return newlist[:k]


def find_recommend_lists_ids(path_instance):
    all_lists = []
    for item in path_instance:
        # all_lists.append(item["source"][-1])
        all_lists.append(item['target'])
    return all_lists


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def calculate_precision(list_subscribed, recommendation_list_ids, k):
    return len(intersection(list_subscribed, recommendation_list_ids)) / k


def calculate_recall(list_subscribed, recommendation_list_ids, k):
    return len(intersection(list_subscribed, recommendation_list_ids)) / len(list_subscribed)


def calculate_metrics(k):
    sum_precision = 0.0
    sum_recall = 0.0
    for source_user in user_ids:
        # print(source_user)
        file_name = "KGAT_paths/" + str(source_user) + ".txt"
        all_list_together = read_files(file_name)
        recommend_list = find_top_k_weights(all_list_together, k)
        list_subscribed = df_user_list_subscribe.loc[(df_user_list_subscribe['source'] == source_user)]
        recommendation_list_ids = find_recommend_lists_ids(recommend_list)
        sum_precision = sum_precision + calculate_precision(list_subscribed['target'].to_list(),
                                                            recommendation_list_ids,
                                                            k)
        sum_recall = sum_recall + calculate_recall(list_subscribed['target'].to_list(), recommendation_list_ids,
                                                   k)
    return sum_recall, sum_precision


recall, precision = calculate_metrics(10)
print("avg_recall_10: ", recall / 1284, " avg_precision_10: ", precision / 1284)

recall, precision = calculate_metrics(50)
print("avg_recall_50: ", recall / 1284, " avg_precision_50: ", precision / 1284)

recall, precision = calculate_metrics(100)
print("avg_recall_100: ", recall / 1284, " avg_precision_100: ", precision / 1284)

recall, precision = calculate_metrics(500)
print("avg_recall_500: ", recall / 1284, " avg_precision_500: ", precision / 1284)
