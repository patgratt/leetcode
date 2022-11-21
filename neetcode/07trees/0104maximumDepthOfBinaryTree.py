# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# testcase
testcase = TreeNode(val=3)

testcase.left = TreeNode(val=9)
testcase.right = TreeNode(val=20)

testcase.right.left = TreeNode(val=15)
testcase.right.right = TreeNode(val=7)

# solution 1 - recursive DFS (inorder) - all these algos are O(n)
def maxDepth1(root):
    # base case = empty tree
    if not root:
        return 0

    return 1 + max(maxDepth1(root.left), maxDepth1(root.right))

print(maxDepth1(testcase))


# solution 2 - iterative BFS
from collections import deque
def maxDepth2(root):
    if not root:
        return 0

    level = 0
    q = deque([root])
    while q:

        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1

    return level

print(maxDepth2(testcase))


# solution 3 - iterative DFS (preorder)
def maxDepth3(root):
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res

        

