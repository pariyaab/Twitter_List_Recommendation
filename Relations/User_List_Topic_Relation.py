import pandas as pd
import ast


def average(lst):
    return sum(lst) / len(lst)


def find_main_topics(topics):
    main_topics = []
    topics_without_zeros = [x for x in topics if float(x) != 0.0]
    average_topics = average(topics_without_zeros)
    index = 0
    for item in topics:
        if float(item) > average_topics:
            main_topics.append(topics.index(item, index, len(topics)))
            index = topics.index(item)
    return main_topics


df_lists = pd.read_csv('../Dataset/lists.csv')
lists_ids = list(df_lists['id'])
index = 0
entity_2_vec = {}
with open("../Dataset/entity2vec_normal.txt") as myfile:
    for line in myfile:
        entity_id, topic_list = line.split(":")
        entity_2_vec[entity_id] = ast.literal_eval(topic_list)
    myfile.close()

for key, value in entity_2_vec.items():
    if int(key) in lists_ids:
        main_topics_list = find_main_topics(value)
        for item in main_topics_list:
            df_new_row = pd.DataFrame({"source": item, "target": key, "weight": value[item], "relation": "T_L"},
                                      index=[index])
            index += 1
            df_new_row.to_csv('Dataset/l_t.csv', mode='a',
                              index=False, header=False)

df_users = pd.read_csv('../Dataset/users.csv')
user_ids = list(df_users['user_id'])

for key, value in entity_2_vec.items():
    if int(key) in user_ids:
        main_topics_list = find_main_topics(value)
        for item in main_topics_list:
            df_new_row = pd.DataFrame({"source": item, "target": key, "weight": value[item], "relation": "T_U"},
                                      index=[index])
            index += 1
            df_new_row.to_csv('Dataset/u_t.csv', mode='a', index=False, header=False)


