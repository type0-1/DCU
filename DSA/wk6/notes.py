"""
Trees:

Nodes, Subtree, (Ancestor, Descendant) -> Children & Parent.

Edge: Pair in tree T is pair of nodes (u, v) such that u is parent of v.

Tree is ordered: If children of the nodes have meaningful linear order.

Depth:

Root has depth 0
Depth P has depth of (1 + depth of parent)

Binary Tree:

Must satisfy these 3 conditions:

- Every node has at most two children
- Each child node is labeled as left or right child
- A left child precedes a right child in the order of children of a node.

To be a proper binary tree, it must have either zero or two children for each node.

"""