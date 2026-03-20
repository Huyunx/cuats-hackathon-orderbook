import datetime
import random

from exchange import TreeNode, Order

if __name__ == "__main__":
    tree = TreeNode(Order(id=0, owner="", price=0, volume=1))
    N = 100000
    for i in range(1, N):
        tree.insert(Order(id=0, owner="", price=i, volume=1))
        while tree.parent is not None:
            tree = tree.parent
        # print("\n".join(map(str, tree.get_all_nodes())))
        # print("\n")
    tree_len = len(tree.get_all_nodes())
    print(tree_len)
    print(tree.depth)

    assert tree_len == N
    assert 2 ** (tree.depth - 1) <= tree_len <= 2 ** tree.depth
    print("All tests passed")
