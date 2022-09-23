#Coded on AlgoMonster

'''
INSTRUCTIONS
- A balanced binary tree is defined as a tree such that either it is an empty tree, or both its 
  subtree are balanced and !has a height difference of at most 1!
- In that case, given a binary tree, determine if it's balanced.

NOTES
- Return Value: height of longest subtree
- States being passed down: None!
- Look on the lowest-level: the node! If we start from the very bottom, leaf node, as we always should, then
  we can see that we have to start counting height from the leaves, not from the top. Count subtree length 
  from bottom up: return longest subtree + 1, creating tree height going all the way back to the root.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(tree: Node) -> int:   
    if tree is None:
        return 0
    leftHeight = tree_height(tree.left)
    rightHeight = tree_height(tree.right)
    if leftHeight == -1 or rightHeight == -1:
        return -1
    elif abs(rightHeight - leftHeight) > 1:
        return -1
    else:
        return 1 + max(leftHeight, rightHeight)
        
def is_balanced(tree: Node) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    return tree_height(tree) != -1
    

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print('true' if res else 'false')
