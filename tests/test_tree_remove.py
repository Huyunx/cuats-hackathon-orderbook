from exchange import TreeNode, Order

def get_prices(node: TreeNode) -> list[float]:
    return list(map(lambda x: x.price, node.get_all_orders()))

def test_tree_remove():
    tree = TreeNode(Order(id=0, owner="", price=0, volume=1))
    for i in range(1, 1000):
        tree = tree.insert(Order(id=i, owner="", price=i, volume=1))
    assert get_prices(tree) == list(range(1000)), f"Assertion failed: left = {get_prices(tree)}, right = {get_prices(tree)}"
    for i in range(1000):
        all_nodes = tree.get_all_nodes()
        tree = all_nodes[i].remove()
        assert get_prices(tree) == list(filter(lambda x: x != i, range(1000)))
        tree.insert(Order(id=i, owner="", price=i, volume=1))
        while tree.parent is not None:
            tree = tree.parent
        assert get_prices(tree) == list(range(1000))
    print("All tests passed")

if __name__ == "__main__":
    test_tree_remove()