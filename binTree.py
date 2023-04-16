from numpy import log2


class Node(object):

    def __init__(self, value=None, left=None,right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent



class BinaryTree(object):

    def __init__(self, node=None):

        if node!=None and type(node)!=type(Node()):
            node = Node(node) # yes
        
        self.root = node
    
    def size(self):
        return len(self.width_first(self, self.root))
    
    def get_height(self):
        
        def height_rec(node):
            if node == None: return 0
            else:
                return 1 + max(height_rec(node.left),height_rec(node.right))
        
        return height_rec(self.root)
    
    def insert(self, value) -> Node:
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
        # find the node a value in the tree
        # replace that node with the deepest one in the tree

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
        for node in self.depth_first_global(self.root):
            del node
        self.root = None


    def change_value(self, old_value, new_value) -> None:
        
        def depth_first_rec(node, old_value, new_value) -> None:
            if node is None: return 
            if node.value == old_value: node.value = new_value;return

            depth_first_rec(node.left, old_value, new_value)
            depth_first_rec(node.right, old_value, new_value)
        
        depth_first_rec(self.root, old_value, new_value)


    def depth_first_global(self, node) -> list:
        # parcours en profondeur (depth first)
        # Cette fonction est récursive
        l = []
        if node is None: return l
        l.append(node)
        l.extend(self.depth_first_global(node.left))
        l.extend(self.depth_first_global(node.right))

        return l
    
    # parcours en largeur (width path)
    def width_first(self, node) -> list:
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
        
        if search not in ["depth first", "width first"]: search = "width first"
        
        if search == "width first":
            l_nodes = self.width_first(self.root)
            for node in l_nodes: print(node.value)
        elif search == "depth first":
            l_nodes = self.depth_first_global(self.root)
            for node in l_nodes: print(node.value)
        print()

    
    def get_coded_value(self, ref_node) -> str:
        # cherche dans l'arbre et retourne la valeur codee pour le noeud
        def depth_first_rec(node, ref_node, path="") -> str:
            if node==None: return ""
            elif node==ref_node: return path

            left = depth_first_rec(node=node.left, ref_node=ref_node,path=path+"0")
            right = depth_first_rec(node=node.right, ref_node=ref_node,path=path+"1")

            return left if left!="" else right
        
        return depth_first_rec(node=self.root, ref_node=ref_node)
    

    def get_coded_tree(self):
        l_coded_values = []
        for node in self.width_first(self.root):
            l_coded_values.append((self.get_coded_value(node), node.value))
        
        return l_coded_values


    def size(self) -> int:
        l = self.width_first(self.root)
        return len(l) 

    def decomposition(self) -> None:
        pass

    def to_string(self) -> str:
        pass



def merge_trees(tree1, tree2) -> BinaryTree:
    def merge_rec(root1, root2) -> Node:
        if root1 is None: return root2
        elif root2 is None: return root1

        root1.value += root2.value
        root1.left = merge_rec(root1.left, root2.left)
        root1.right = merge_rec(root1.right, root2.right)

        return root1
    
    return BinaryTree(merge_rec(tree1.root, tree2.root))



def test():
    # Cette section a pour but de tester le programme 

    # on crée 2 arbres binaires de 5 éléments (aléatoires: entre 0 et 10) chacun 
    # (on pourrait en mettre plus)
    import random
    t1 = BinaryTree()
    for i in range(5): t1.insert(random.randint(0,10))
    t2 = BinaryTree()
    for i in range(5): t2.insert(random.randint(0,10))

    # Parcours en largeur
    print("Pacours en largeur");t1.display("width first")
    # Parcours en profondeur
    print("Pacours en profondeur");t1.display("depth first")

    merge_trees(t1, t2).display()

    t = BinaryTree(); [t.insert(i) for i in range(5)]
    print("t: ");t.display()
    print(t.get_coded_tree())


if __name__ == "__main__":
    # test()

    tree = BinaryTree()
    [tree.insert(i) for i in range(5)]
    tree.display()
    tree.delete(2)
    tree.display()
    print(tree.get_coded_tree())