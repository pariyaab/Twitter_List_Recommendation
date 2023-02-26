# Twitter_List_Recommendation

This project builds an explainable list recommendation system for Twitter users using a knowledge graph. The recommendation process involves four main steps:

## Defining our relations for building a knowledge graph

To build our knowledge graph, we define the following relations:

* **user_user relation:** We calculate the number of tweets that have been retweeted between two users, remove the ones with a count of 0, and normalize the remaining ones.
* **user_topic relation:** We identify the most interesting topics for each user based on their tweets and consider those topics as their interests.
* **user_list relation:** We find the lists that each user has already subscribed to.
* **list_topic relation:** We determine the most relevant topic(s) for each list.
* **topic_topic relation:** We calculate the similarity between two topics.

This is a schema of our graph:
![img.png](img.png)

## Building a knowledge graph

We use the `networkx` library to build a weighted, indirect knowledge graph. The statistics of our graph are shown below:

| # U_U relation | # U_T relation | # U_L relation | # T_T relation | # L_T relation |
| --------------| -------------- | -------------- | -------------- | -------------- |
| 3058           | 19679          | 6058           | 7317           | 19161          |




