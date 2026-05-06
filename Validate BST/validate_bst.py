""" Validate BST """

class TreeNode:
    """
    Tree Node class
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Check is bst is valid
    """
    if not root:
        return True
    if not min_val < root.val < max_val:
        return False
    return (is_valid_bst(root.left, min_val, root.val)
            and is_valid_bst(root.right, root.val, max_val))
