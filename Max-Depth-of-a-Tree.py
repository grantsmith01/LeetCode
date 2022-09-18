#Coded on AlgoMonster

'''
INSTRUCTIONS
Max depth of a binary tree is the longest root-to-leaf path. Given a binary tree, find its max depth.

NOTES
- Root alone is depth 1
- From the perspective of each node: return 1 + greatest depth of either child, 1 accounting for my depth + my longest child's.
- Null nodes return 0 since they aren't a node at all, therefore add no depth.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if root is None:
        return 0
    left_path = tree_max_depth(root.left)
    right_path = tree_max_depth(root.right)
    return 1 + max(left_path, right_path)

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = tree_max_depth(root)
    print(res)
