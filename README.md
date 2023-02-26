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

## Baseline Method

In this method, we find the heaviest path between each user and all of the lists using the A* algorithm.

In `Find_Heaviest_Paths.py`, the implemented algorithm works by maintaining two dictionaries, `g` and `path_length`. The `g` dictionary stores the current heaviest path weight from the source node to each visited node, and the `path_length` dictionary stores the length of the path from the source node to each visited node.

At each iteration, the algorithm selects the node with the highest `f = g + h` value, where `g` is the heaviest path weight from the source node to the current node, and `h` is an estimate of the remaining heaviest path weight from the current node to the target node. The estimate is computed using a heuristic function, which in this case is simply the weight of the edge connecting the current node to the target node.

If the length of the path from the source node to the current node is less than or equal to the `max_path_length` (if provided), the algorithm updates the `g` and `path_length` dictionaries with the heaviest path weight and path length to the current node, and adds the current node to the heap.

When the algorithm reaches the target node, it reconstructs the heaviest path from the source to the target by backtracking through the `path` dictionary, which stores the parent node for each visited node. Finally, it returns the reconstructed path and its weight.

By summing the weights of the edges in the reconstructed path, we get the heaviest path weight between the source and target nodes.

After finding the heaviest paths between each user and list, we sort them based on their weight and calculate Recall and Precision:

* **Recall:** How many lists that are in the first K sorted list that the user has already subscribed to, divided by the number of subscribed lists.
* **Precision:** How many lists that are in the first K sorted list that the user has already subscribed to, divided by K.

The results are as follows:

| K    | Precision | Recall |
| ---- | --------- | ------ |
| 10   | 0.06      | 0.13   |
| 50   | 0.02      | 0.31   |
| 100  | 0.02      | 0.43   |
| 500  | 0.007     | 0.81   |

# Graph Neural Network Method

In this method, we use Graph Neural Network to find the embedding of each entity and then use those embedding vectors to find the cosine similarity between each user and list, and do the same thing as the baseline method (sort based on similarity values and choose top K).

## Getting the Embeddings

To get the embeddings of our graph, we first split our dataset into train and test (80% train and 20% test - for each user, we choose 1 list as a test list) and use the OpenHINE repository (https://github.com/BUPT-GAMMA/OpenHINE) to find the embedding vectors using Graph Neural Network methods.

## Calculating Precision and Recall

After finding the similarities, we calculate the following metrics:

| K    | Precision | Recall |
| ---- | --------- | ------ |
| 10   | 0.27      | 0.58   |
| 50   | 0.07      | 0.79   |
| 100  | 0.04      | 0.87   |
| 500  | 0.09      | 0.98   |

We also calculate another metric, which is called MPR (Mean Percentile Rank). This is calculated as follows:
* **MPR:** Mean percentile ranking (MPR) is a metric commonly used to evaluate the performance of top-K recommendation algorithms. It measures the average position of a test item in the ranked list of recommended items. Specifically, for each test item, its percentile ranking is calculated as the position of the item in the ranked list divided by the total number of items, and then multiplied by 100 to get a percentage. The MPR is then calculated as the average of these percentile rankings across all test items and all users. A lower MPR value indicates better performance, as it means that the test items are ranked higher in the recommendation list.

1. Order all of the similarities.
2. Find the position of the test list and divide it by the total number of lists.
3. Sum all of the divided values and divide by the number of users.

The result for 3 consecutive runs is as follows:

| K    | MPR  | 
| ---- | ---- | 
| 1    | 0.35 | 
| 2    | 0.24 | 
| 3    | 0.24 | 

## Resources
*  Zhang, D., Yin, J., Zhu, X., & Zhang, C. (2018). Metagraph2vec: 
Complex semantic path augmented heterogeneous network 
embedding. In Advances in Knowledge Discovery and Data Mining: 
22nd Pacific-Asia Conference, PAKDD 2018, Melbourne, VIC, 
Australia, June 3-6, 2018, Proceedings, Part II 22 (pp. 196-208). 
Springer International Publishing.