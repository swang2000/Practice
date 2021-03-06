import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findDuplicateSubtrees(root):
    count = collections.Counter()
    ans = []

    def collect(node):
        if not node: return "#"
        serial = "{},{},{}".format(node.val, collect(node.left), collect(node.right))
        count[serial] += 1
        if count[serial] == 2:
            ans.append(node)
        return serial

    collect(root)
    return ans


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)

findDuplicateSubtrees(root)
