import numpy as np
from collections import defaultdict



# Define the entropy function
def entropy(y):
    unique, count = np.unique(y, return_counts=True)
    p = count / np.sum(count)
    return -np.sum(p * np.log2(p))




# Define the function to split a node
def split_node(X, attributes, C, t):
    best_c, best_a, best_info_gain = None, None, -1
    for a in attributes:
        for c in np.unique(C):
            mask = (C == c)
            info_gain = entropy(X[mask, -1]) - entropy(X[mask, a])
            if info_gain > best_info_gain:
                best_c, best_a, best_info_gain = c, a, info_gain
    if best_info_gain == 0:
        return None, None
    C_left, C_right = best_c, best_c
    X_left, X_right = X[X[:, best_a] == 0], X[X[:, best_a] == 1]
    return {"C": C_left, "X": X_left}, {"C": C_right, "X": X_right}




# Define the main function to build the decision tree
def build_tree(X, attributes, C, t):
    node_list = [{"C": C, "X": X, "depth": 0}]
    tree = defaultdict(list)
    while node_list:
        next_list = []
        for node in node_list:
            v1, v2 = split_node(node["X"], attributes, node["C"], t)
            if v1 is not None and v2 is not None and node["depth"] < t:
                tree[node["C"], t].append({"a": attributes[node["depth"]], "v": 0})
                tree[node["C"], t].append({"a": attributes[node["depth"]], "v": 1})
                next_list.append({"C": v1["C"], "X": v1["X"], "depth": node["depth"] + 1})
                next_list.append({"C": v2["C"], "X": v2["X"], "depth": node["depth"] + 1})
            else:
                tree[node["C"], t].append({"a": None, "v": None})
        node_list = next_list
    return dict(tree)