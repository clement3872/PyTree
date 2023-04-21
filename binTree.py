from numpy import log2


class Node(object):
    # Classic structure for a node
    def __init__(self, value=None, left=None,right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent



class BinaryTree(object):
    """
    Class for a binary tree
    Details are in each functions
    """
    
    def __init__(self, node=None):
        """BinaryTree

        Args:
            node (type: any - str advised): Node for the root. Defaults to None.
        """

        # This is to avoid a bug
        if node!=None and type(node)!=type(Node()):
            node = Node(node) # yes...
        
        self.root = node
    
    def size(self):
        """Return the size of the tree"""
        return len(self.width_first(self, self.root))
    
    def get_height(self):
        """Return the height of the tree"""
        def height_rec(node):
            if node == None: return 0
            else:
                return 1 + max(height_rec(node.left),height_rec(node.right))
        
        return height_rec(self.root)
    
    def insert(self, value) -> Node:
        """insert a value in the tree

        Args:
            value (type: any - str advised): if it's not a string, user won't
                be able to delete it on the GUI.

        Returns:
            Node: the new Node object.
        """
        
        if self.root is None:
            self.root = Node(value)
            return self.root
        else:
            l_nodes = [self.root]
            while l_nodes:
                node = l_nodes.pop(0)

                if node.left is None:
                    new_node = Node(value=value,parent=node)
                    node.left = new_node
                    return new_node
                elif node.right is None:
                    new_node = Node(value=value,parent=node)
                    node.right = new_node
                    return new_node
                else:
                    l_nodes.extend([node.left, node.right])

    def delete(self, value) -> bool:
        """delete the the first node that matches the given value.

        Args:
            value (type: any - str advised): 

        Returns:
            bool: True if the node has been deleted, else False.
        """ 
        
        if self.root is None: return False
        
        node = None
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.value == value:
                node = current
            else:
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right) 
        
        # if we found the node that we wanted to delete
        if node is not None:
            deepest_node = self.width_first(self.root)[-1]
            
            # replace the node with the deepest where it's needed
            if deepest_node == self.root: self.root = None

            elif node == deepest_node:
                if deepest_node.parent.left == deepest_node: deepest_node.parent.left = None
                else: deepest_node.parent.right = None

            elif node != deepest_node:
                # remove pointers to the deepest node in the tree
                if deepest_node.parent.left == deepest_node: deepest_node.parent.left = None
                else: deepest_node.parent.right = None

                # change pointers for the (old) deepest node
                deepest_node.left = node.left
                deepest_node.right = node.right
                deepest_node.parent = node.parent

                # replace pointers to the node we want to delete to the deepest node
                if node != self.root:
                    if node.parent.left == node: node.parent.left = deepest_node
                    else: node.parent.right = deepest_node
                else:
                    self.root = deepest_node
                if node.left != None: node.left.parent = deepest_node
                if node.right != None: node.right.parent = deepest_node

        return True
    
    
    def delete_all(self):
        """delete_all, delete all nodes in the tree"""        
        for node in self.depth_first(self.root):
            del node
        self.root = None


    def change_value(self, old_value, new_value) -> None:
        """change_value, replace old_value by new_value
            replaces the first it finds (if a node is found)

        Args:
            old_value (type: any - str advised): value that will be replaced 
            new_value (type: any - str advised): futur value
        """
        
        # A recursive way to find the node and replace it with the new value
        def depth_first_rec(node, old_value, new_value) -> None:
            if node is None: return 
            if node.value == old_value: node.value = new_value;return

            depth_first_rec(node.left, old_value, new_value)
            depth_first_rec(node.right, old_value, new_value)
        
        # we still need to run that function!
        depth_first_rec(self.root, old_value, new_value)


    def depth_first(self, node) -> list:
        """depth_first, apply this on the tree.

        Args:
            node (Node object): The Node you want to start with.

        Returns:
            list: list of Node objects in depth first order.
        """
        l = []
        if node is None: return l
        l.extend(self.depth_first(node.left))
        l.extend(self.depth_first(node.right))
        l.append(node)

        return l
    
    
    def width_first(self, node) -> list:
        """width path, apply this on the tree

        Args:
            node (Node object): The Node you want to start with

        Returns:
            list: list of Node objects in depth first order
        """        
        if self.root is None: return 
        
        l_nodes = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            l_nodes.append(node)
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right) 
        
        return l_nodes


    
    def display(self, search="") -> None:
        """display the tree in the console

        Args:
            search (str, optional): choose the methode to display the tree 
                between depth first and width first. Defaults is depth first.
        """        
        if search not in ["depth first", "width first"]: search = "width first"
        
        if search == "width first":
            l_nodes = self.width_first(self.root)
        elif search == "depth first":
            l_nodes = self.depth_first(self.root)
        
        if l_nodes != None:
            for node in l_nodes: print(node.value)
        print()


    def get_coded_value(self, ref_node) -> str:
        """get_coded_value, path to a node, left is 0 and right is 1
                it's useful for Huffman.

        Args:
            ref_node (Node object): The node of which to get the "path".

        Returns:
            str: a sequence of 0s and 1s
        """
        def depth_first_rec(node, ref_node, path="") -> str:
            if node==None: return ""
            elif node==ref_node: return path

            left = depth_first_rec(node=node.left, ref_node=ref_node,path=path+"0")
            right = depth_first_rec(node=node.right, ref_node=ref_node,path=path+"1")

            return left if left!="" else right
        
        return depth_first_rec(node=self.root, ref_node=ref_node)

    def get_coded_tree(self):
        """get_coded_tree, does depth_first_rec for all the value in the tree.

        Returns:
            list: lits of each coded values
        """        
        l_coded_values = []
        for node in self.width_first(self.root):
            l_coded_values.append((self.get_coded_value(node), node.value))
        
        return l_coded_values
    

    def decomposition(self, node):
        """decomposition, decompose the tree starting at node

        Args:
            node (type: any - str advised): the node where to start the decomposition

        Returns:
            list: list of Node objects
        """        
        return self.depth_first(node)


def merge_trees(tree1, tree2) -> BinaryTree:
    """merge_trees, does what is says.

    Args:
        tree1 (BinaryTree object): tree to merge with the other one.
        tree2 (BinaryTree object): tree to merge with the other one.

    Returns:
        BinaryTree: BinaryTree object.
    """    
    def merge_rec(root1, root2) -> Node:
        if root1 is None: return root2
        elif root2 is None: return root1

        root1.value += root2.value
        root1.left = merge_rec(root1.left, root2.left)
        root1.right = merge_rec(root1.right, root2.right)

        return root1
    
    return BinaryTree(merge_rec(tree1.root, tree2.root))



def test():
    """test
    Like it's said, it's just to test this file...
    """

    # creates 2 trees
    import random
    t1 = BinaryTree()
    for i in range(5): t1.insert(random.randint(0,10))
    t2 = BinaryTree()
    for i in range(5): t2.insert(random.randint(0,10))

    # displays width first
    print("Pacours en largeur");t1.display("width first")
    # displays depth first
    print("Pacours en profondeur");t1.display("depth first")

    # merges the trees
    merged_tree = merge_trees(t1, t2).display()

    t = BinaryTree(); [t.insert(i) for i in range(5)]
    print("t: ");t.display()
    print(t.get_coded_tree())


if __name__ == "__main__":
    """
    It's just to test this file...
    """
    # test() # you can try to uncomment if you want

    tree = BinaryTree()
    [tree.insert(i) for i in range(5)]
    tree.display()
    tree.delete(2)
    tree.display()
    print(tree.get_coded_tree())