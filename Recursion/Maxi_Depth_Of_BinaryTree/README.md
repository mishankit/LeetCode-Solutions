Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

The height of a tree can be found recursively by calculating the height of the left and right subtrees.
The height of the tree is the maximum of the heights of the left and right subtrees plus one (for the current node).
Base case: If the node is None, return -1 (or 0 if you're counting nodes instead of edges).