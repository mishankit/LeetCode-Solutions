Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

A preorder traversal is a depth-first traversal method for trees where the nodes are visited in the following order:

Visit the root node.
    Traverse the left subtree in preorder.
    Traverse the right subtree in preorder.
    This traversal is commonly used to create a copy of the tree or to get a prefix expression (Polish notation) of an expression tree.

Approach
To perform a preorder traversal on a binary tree, we can use either a recursive or an iterative approach:
Recursive Approach:
    Visit the root node.
    Recursively traverse the left subtree.
    Recursively traverse the right subtree.

Iterative Approach:
    Use a stack to keep track of nodes to visit.
    Push the root node onto the stack.
    While the stack is not empty, pop a node, visit it, then push its right child followed by its left child onto the stack (to ensure left is processed before right).