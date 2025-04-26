# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder_lst = []
        def inorder(root):
            if root:
                inorder(root.left)
                inorder_lst.append(root.val)
                inorder(root.right)

            return root
        
        inorder(root)
        return inorder_lst[k - 1] 