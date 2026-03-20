from exchange import TreeNode, Order
import random

def get_prices(node: TreeNode) -> list[float]:
    return list(map(lambda x: x.price, node.get_all_orders()))

def test_split():
    tree = TreeNode(Order(id=0, owner="", price=0, volume=1))
    for i in range(1, 1000):
        tree = tree.insert(Order(id=i, owner="", price=i, volume=1))
    left, right = tree.split(100)
    assert len(left.get_all_nodes()) == 101
    assert len(right.get_all_nodes()) == 899
    assert all(price <= 100 for price in get_prices(left))
    assert all(price > 100 for price in get_prices(right))

def test_split_and_remove():
    tree = TreeNode(Order(id=0, owner="", price=0, volume=1))
    for i in range(1, 1000):
        tree = tree.insert(Order(id=i, owner="", price=i, volume=1))
    left, right = tree.split(100)
    right = right.get_all_nodes()[0].remove()
    assert len(right.get_all_nodes()) == 898
    assert all(price > 101 for price in get_prices(right))
    for i in range(1000):
        length = len(right.get_all_nodes())
        node_to_remove = right.get_all_nodes()[random.randint(0, length - 1)]
        right = node_to_remove.remove()
        assert right.parent is None
        assert len(right.get_all_nodes()) == 897
        right = right.insert(node_to_remove.order)
        assert right.parent is None
        assert len(right.get_all_nodes()) == 898

if __name__ == "__main__":
    test_split()