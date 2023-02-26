import random

import pandas as pd

# rating dataset
df_user_list_subscribe = pd.read_csv('.././Dataset/ratings.csv')
df_user_list_subscribe.columns = ['source', 'target', 'weight']
df_user_list_subscribe.drop('weight', inplace=True, axis=1)
df_user_list_subscribe['weight'] = 0.5
new_cols = ["target", "source", "weight"]

df_user_list_subscribe = df_user_list_subscribe.reindex(columns=new_cols)
df_user_list_subscribe['relation'] = "U_L"
df_user_list_subscribe.to_csv('Dataset/u_L.csv', mode='a', index=False, header=False)


# df_new_row_2 = pd.DataFrame({"source": key, "target": item, "weight": 0.5, "relation": "U_L"}, index=[index_2])
# index_2 += 1
# df_new_row_2.to_csv('Dataset/train_kgat.csv', mode='a', index=False, header=False)

# train_set = pd.read_csv("Dataset/bidirectional_train_3_u_l.csv")
# train_set.columns = ['source', 'target', 'weight', 'relation']
# train_set.drop('weight', inplace=True, axis=1)
# train_set.drop('relation', inplace=True, axis=1)
# new_cols = ["target", "source"]
#
# train_set = train_set.reindex(columns=new_cols)
# train_set["weight"] = 0.5
# train_set["relation"] = "L_U"
# train_set.to_csv('Dataset/bidirectional_train_3_u_l.csv', mode='a', index=False, header=False)

# df = pd.merge(df_user_list_subscribe, test_set, how='outer', indicator=True)
# df_train = df.loc[df._merge == 'left_only']
# df_train.drop('_merge', inplace=True, axis=1)
#
# new_cols = ["target", "source"]
# df_train = df_train.reindex(columns=new_cols)
# df_train["weight"] = 0.5
# df_train["relation"] = "L_U"
# df_train.to_csv('Dataset/bidirectional_train_u_l.csv', mode='a', index=False, header=False)

# print(user_list_count_dict)
# # number of subscribed list
# df_user_list_count = pd.read_csv('.././Dataset/users_lists_count.csv', index_col=False)
# df_user_list_count.loc[(df_user_list_count['subscribe_count'] > 10), 'subscribe_count'] = 10
# print(df_user_list_count)
# # user ids
# user_ids = set(list(df_user_list_subscribe['source']))
#
# index = 0
# for user in user_ids:
#     weight = df_user_list_count.loc[(df_user_list_count['user_id'] == user)]['subscribe_count'].to_list()
#     weight = max(weight[0], user_list_count_dict[user])
#     target_list = (df_user_list_subscribe.loc[(df_user_list_subscribe['source'] == user)]['target']).to_list()
#     for lists in target_list:
#         df_new_row = pd.DataFrame({"source": user, "target": lists, "weight": 1 / weight, "relation": "U_L"},
#                                   index=[index])
#         index += 1
#         df_new_row.to_csv('Dataset/u_l.csv', mode='a', index=False, header=False)
#
# df = pd.read_csv('Dataset/u_l.csv', index_col=False)
# df.columns = ['source', 'target', 'weight', 'relation']
# print(df['weight'].median(), df['weight'].mean(), len(df))
