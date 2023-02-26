import pandas as pd

user_list = pd.read_csv('../Relations/Dataset/OpenHE/bidirectional_u_L.csv', error_bad_lines=False)
user_list.columns = ["source", "target", "weight", "relation"]
user_list.to_csv('final_result.csv', mode='a', index=False, header=False)


list_topic = pd.read_csv('../Relations/Dataset/OpenHE/new_l_t.csv')
list_topic.columns = ["source", "target", "weight", "relation"]
list_topic = list_topic.loc[(list_topic['weight'] != 0.0)]
list_topic.to_csv('final_result.csv', mode='a', index=False, header=False)

user_topic = pd.read_csv('../Relations/Dataset/OpenHE/new_u_t.csv')
user_topic.columns = ["source", "target", "weight", "relation"]
user_topic = user_topic.loc[(user_topic['weight'] != 0.0)]
user_topic.to_csv('final_result.csv', mode='a', index=False, header=False)

topic_topic = pd.read_csv('../Relations/Dataset/OpenHE/new_t_t.csv')
topic_topic.columns = ["source", "target", "weight", "relation"]
topic_topic = topic_topic.loc[(topic_topic['weight'] != 0.0)]
topic_topic.to_csv('final_result.csv', mode='a', index=False, header=False)

user_user = pd.read_csv('../Relations/Dataset/OpenHE/new_u_u.csv')
user_user.columns = ["source", "target", "weight", "relation"]
user_user = user_user.loc[(user_user['weight'] != 0.0)]
user_user.to_csv('final_result.csv', mode='a', index=False, header=False)

