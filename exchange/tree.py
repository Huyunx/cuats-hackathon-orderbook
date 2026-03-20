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

    def __init__(self, order: Order, parent: Optional[Self] = None):
        self.order = order
        self.left = None
        self.right = None
        self.parent = parent
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
                self.left = TreeNode(neworder, self)
        if neworder > self.order:
            if self.right is not None:
                self.right.insert(neworder)
            else:
                self.right = TreeNode(neworder, self)

        if TreeNode.depth(self.right) - TreeNode.depth(self.left) >= 2:
            self.rotate_left()
        elif TreeNode.depth(self.left) - TreeNode.depth(self.right) >= 2:
            self.rotate_right()
        self.update_depth()

    def find_largest(self) -> TreeNode:
        if self.right is not None:
            return self.right.find_largest()
        return self

    def find_smallest(self) -> TreeNode:
        if self.left is not None:
            return self.left.find_smallest()
        return self

    def remove(self) -> Optional[TreeNode]:
        """Remove self from the tree. Returns the new root of the tree."""
        if self.left is None and self.right is None:
            to_remove = self
        elif TreeNode.depth(self.right) > TreeNode.depth(self.left):
            smallest = self.right.find_smallest()
            smallest.rotate_left()
            self.order = smallest.order
            to_remove = smallest
        else:
            largest = self.left.find_largest()
            largest.rotate_right()
            self.order = largest.order
            to_remove = largest
        p = to_remove.parent
        q = p
        if p is not None:
            if to_remove == p.left:
                p.left = None
            else:
                p.right = None
            while p is not None:
                q = p
                if TreeNode.depth(p.right) - TreeNode.depth(p.left) >= 2:
                    p.rotate_left()
                elif TreeNode.depth(p.left) - TreeNode.depth(p.right) >= 2:
                    p.rotate_right()
                p.update_depth()
                p = p.parent
        return q

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
        if b is None:
            return
        b.parent = self.parent
        if b.left is not None:
            b.left.parent = self
        self.right = b.left
        b.left = self
        if self.parent is None:
            pass
        elif self is self.parent.left:
            self.parent.left = b
        elif self is self.parent.right:
            self.parent.right = b
        self.parent = b
        self.update_depth()
        b.update_depth()

    def rotate_right(self):
        b = self.left
        if b is None:
            return
        b.parent = self.parent
        self.left = b.right
        if b.right is not None:
            b.right.parent = self
        b.right = self
        if self.parent is None:
            pass
        elif self is self.parent.left:
            self.parent.left = b
        elif self is self.parent.right:
            self.parent.right = b
        self.parent = b
        self.update_depth()
        b.update_depth()