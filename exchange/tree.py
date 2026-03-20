from __future__ import annotations
from typing import Optional, Self

from .types import Order

class TreeNode:
    order: Order
    left: Optional[Self]
    right: Optional[Self]
    parent: Optional[Self]
    depth: int

    def __str__(self):
        return f"TreeNode(order={self.order}, depth={self.depth})"

    def __init__(self, order: Order):
        self.order = order
        self.left = None
        self.right = None
        self.parent = None
        self.depth = 1

    @staticmethod
    def depth(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        return node.depth

    def update_depth(self):
        left_depth = TreeNode.depth(self.left)
        right_depth = TreeNode.depth(self.right)
        self.depth = 1 + max(left_depth, right_depth)

    def insert(self, neworder: Order):
        if not (self.order < neworder):
            if self.left is not None:
                self.left.insert(neworder)
            else:
                self.left = TreeNode(neworder)
        if neworder > self.order:
            if self.right is not None:
                self.right.insert(neworder)
            else:
                self.right = TreeNode(neworder)

        if TreeNode.depth(self.right) - TreeNode.depth(self.left) >= 2:
            self.rotate_left()
        elif TreeNode.depth(self.left) - TreeNode.depth(self.right) >= 2:
            self.rotate_right()
        self.update_depth()

    def get_all_nodes(self) -> list[Self]:
        ans = []
        if self.left is not None:
            ans = self.left.get_all_nodes()
        ans.append(self)
        if self.right is not None:
            ans.extend(self.right.get_all_nodes())
        return ans

    def get_all_orders(self) -> list[Order]:
        ans = []
        if self.left is not None:
            ans = self.left.get_all_orders()
        ans.append(self.order)
        if self.right is not None:
            ans.extend(self.right.get_all_orders())
        return ans

    def rotate_left(self):
        b = self.right
        b.parent = self.parent
        if b.left is not None:
            b.left.parent = self
        self.right = b.left
        b.left = self
        if self.parent is None:
            pass
        elif self is self.parent.left:
            self.parent.left = b
            self.parent = b
        elif self is self.parent.right:
            self.parent.right = b
            self.parent = b
        self.update_depth()
        b.update_depth()

    def rotate_right(self):
        b = self.left
        b.parent = self.parent
        self.left = b.right
        if b.right is not None:
            b.right.parent = self
        b.right = self
        if self.parent is None:
            pass
        elif self is self.parent.left:
            self.parent.left = b
            self.parent = b
        elif self is self.parent.right:
            self.parent.right = b
            self.parent = b
        self.update_depth()
        b.update_depth()