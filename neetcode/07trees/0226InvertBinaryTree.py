# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# solution
def invertTree(root: TreeNode) -> TreeNode:
    # base case
    if not root:
        return None

    # swap the children of the root
    tmp = root.left
    root.left = root.right
    root.right = tmp

    # recursively swap the children of what we just swapped
    invertTree(root=root.left)
    invertTree(root=root.right)

    return root


# function to recursively print tree
def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)


# build test case input tree
testcase = TreeNode(val=4)

testcase.left = TreeNode(val=2)
testcase.right = TreeNode(val=7)

testcase.left.left = TreeNode(val=1)
testcase.left.right = TreeNode(val=3)
testcase.right.left = TreeNode(val=6)
testcase.right.right = TreeNode(val=9)

printTree(testcase)

# run testcase
invertTree(testcase)
printTree(testcase)

# my solution months later

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        # DFS
        # base case
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            tmp = node.left
            node.left = node.right
            node.right = tmp

        dfs(root)
        return root