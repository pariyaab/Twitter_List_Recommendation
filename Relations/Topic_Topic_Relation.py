import pandas as pd
import numpy as np

df_topic_similarities = pd.read_csv('.././Dataset/topics_similarites.csv')
df_topic_similarities.columns = ['source', 'target', 'weight']
print(len(df_topic_similarities))

topics_similarities = {}
df_filterd_topics = df_topic_similarities.loc[(df_topic_similarities['weight'] > 0.05)]

print(len(df_filterd_topics))
for i in range(0, 529):
    df_topic_number_similarities = df_filterd_topics.loc[(df_filterd_topics['source'] == i)]
    topics_similarities[i] = len(df_topic_number_similarities)

print(len(df_filterd_topics['weight']), df_filterd_topics['weight'].mean())
df_filterd_topics["relation"] = "T_T"
new_cols = ["target", "source", "weight", "relation"]
# or
df_filterd_topics = df_filterd_topics.reindex(columns=new_cols)
df_filterd_topics.to_csv('Dataset/t_t.csv', mode='a', index=False, header=False)
