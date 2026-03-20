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
    
    def rotate_to_balance(self) -> TreeNode:
        """Rotate the current node such that it maintains the balaning property.
        
        When the depth of the left tree and the right tree are differed by at most 1, the node
        is said to be "balanced".

        This function returns the new root node.
        """
        if TreeNode.depth(self.right) - TreeNode.depth(self.left) >= 2:
            if self.right is not None and TreeNode.depth(self.right.left) - TreeNode.depth(self.right.right) == 1:
                self.right.rotate_right()
            self.rotate_left()
            return self.parent
        elif TreeNode.depth(self.left) - TreeNode.depth(self.right) >= 2:
            if self.left is not None and TreeNode.depth(self.left.right) - TreeNode.depth(self.left.left) == 1:
                self.left.rotate_left()
            self.rotate_right()
            return self.parent
        return self

    def insert(self, neworder: Order) -> TreeNode:
        if not (self.order < neworder):
            if self.left is not None:
                self.left.insert(neworder)
            else:
                self.left = TreeNode(neworder, self)
        else:
            if self.right is not None:
                self.right.insert(neworder)
            else:
                self.right = TreeNode(neworder, self)
        self.update_depth()
        return self.rotate_to_balance()

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
        while self.left is not None or self.right is not None:
            if TreeNode.depth(self.left) < TreeNode.depth(self.right):
                self.rotate_left()
            else:
                self.rotate_right()
        p = self.parent
        if p is not None:
            if self is p.left:
                p.left = None
            else:
                p.right = None
        else:
            return None
        p.update_depth()
        while p.parent is not None:
            p.rotate_to_balance()
            p = p.parent
        return p

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

    def split(self, target_price: float) -> tuple[Optional[TreeNode], Optional[TreeNode]]:
        """
        Split the current tree to two trees, with all values in the left tree smaller than or equal
        to the given value, and the right tree larger than the given value.
        """
        if self.order.price <= target_price:
            if self.right is not None:
                rl, rr = self.right.split(target_price)
                self.right = rl
                if rl is not None:
                    rl.parent = self
                self.update_depth()
                return (self, rr)
            else:
                return (self, None)
        else:
            if self.left is not None:
                ll, lr = self.left.split(target_price)
                self.left = lr
                if lr is not None:
                    lr.parent = self
                self.update_depth()
                return (ll, self)
            else:
                return (None, self)