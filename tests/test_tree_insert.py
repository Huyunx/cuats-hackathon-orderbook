import datetime
import random

from exchange import TreeNode, Order

if __name__ == "__main__":
    tree = TreeNode(Order(id=0, owner="", price=0, volume=1))
    for i in range(1, 3):
        tree.insert(Order(id=0, owner="", price=i, volume=1))
        while tree.parent is not None:
            tree = tree.parent
    print(len(tree.get_all_nodes()))
    # print("\n".join(map(str, tree.get_all_nodes())))
