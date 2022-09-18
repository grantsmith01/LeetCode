#Coded on AlgoMonster

'''
INSTRUCTIONS
In a binary tree, we define a node "visible" when no node on the root-to-itself path (inclusive) has a greater value. 
The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.

NOTES
- RETURN VALUE: The number of visible nodes on current node's subtrees, potentially plus itself if it's visible
- STATES: We must track the current maximum value of the current node's ancestors. Use a parameter to do this, updating max val as you go in the param
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node, maxVal: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    if root is None:
        return 0
    left_visible = visible_tree_node(root.left, max(root.val, maxVal))
    right_visible = visible_tree_node(root.right, max(root.val, maxVal))
    if root.val >= maxVal:
        return 1 + left_visible + right_visible
    return 0 + left_visible + right_visible

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
    res = visible_tree_node(root, -float('inf'))
    print(res)
