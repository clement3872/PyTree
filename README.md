# PyTree projet

It's a little projet from the University, here is what it contains:
 - binTree.py: a mudule to use binary tree
 - Huffman.py: Huffman encore/decoding (needs binTree in the same folder)
 - window_main.py & subWin.py: basic GUI for binary tree (needs binTree and Huffman.py in the same folder)

# Requirements
Having Python installed, with tkinter and numpy modules.
(numpy is used for log2 and tkinter for GUI)
tkinter should be installed by default (exept on linux), to install numpy: pip install numpy

# More details

## binTree
A module to for basic binary trees (not BST, ...)

Contains:
 - BinaryTree: class
 - Node: class
 - merge_trees: function, args=(BinaryTree:tree1, BinaryTree:tree2)

First, create a tree using : BinaryTree() or BinaryTree("first value/Node()")

Usefull functions (considering tree = binTree.BinaryTree()):
- tree.insert(any:value) -> None
- tree.remove(any:value) -> None
- tree.delete(any:value) -> None
- tree.change_value(any:old_value, any:new_value)
- tree.delete_all() -> None
- tree.width_first_global(Node) -> list of binTree.Node // you can do: tree.depth_first_global(tree.root)
- tree.depth_first_global(Node) -> list of binTree.Node // same
- tree.display() -> None 
- tree.size()

