

def two_min_list_nodes(l) -> tuple:
    # obtenir les 2 plus petites valeurs de la liste (retourne les indices)
    j,j2 = 0,1
    if type(l) is list and len(l) >= 2:
        for i in range(len(l)):
            if l[i] < l[j] and i!=j2: j = i
            if l[i] <= l[j2] and i!=j: j2 = i
    
    return j,j2



class Node(object):
    # stucture d'un noeud
    def __init__(self, value=None, frequency=None, left=None, right=None) -> None:
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right


class Huffman(object):
    
    def __init__(self) -> None:
        self.root = None

    # def insert(self, value, frequency) -> None:
    #     """NOT IMPLEMENTED YET - you may delete everything in this function"""

        # if self.root == None: 
        #     self.root = Node(value, frequency)

        # elif self.root.left == None and self.root.right == None:
        #     new_node = Node(value=value, frequency=frequency)
        #     tmp = self.root
        #     self.root = Node(value=None, frequency=frequency+tmp.frequency)
        #     if value > tmp.value:
        #         self.root.left = tmp
        #         self.root.right = new_node
        #     else:
        #         self.root.right = tmp
        #         self.root.left = new_node
        # else: 
        #     #here especially... 
        #     new_node = Node(value, frequency)
        #     if value > self.root.value:
        #         left_value = self.root.left.frequency if self.root.left else 0
        #         right_value = self.root.right.frequency if self.root.right else 0
        #         new_root = Node(value=None, frequency=left_value+right_value+frequency, left=self, right=None)
                


    def search(self, value=None) -> Node: 
        # parcours en largeur modifie ("breadth first" en anglais)
        if self.root is None: return 
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value: return node
            
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right) 


    def change_value(self, value, new_value):
        node = self.search(value)
        node.value = new_value

    def delete(self, value) -> None:
        
        def delete_node(node, side) -> None: 
            # supprime un noeud et termine la fonction
            tmp = node
            node = eval(f"node.{side}")
            # on raccroche le reste de l'arbre s'il existe
            if node.right.value!=None: tmp.left = node.right
            elif node.left.value!=None: tmp.right = node.left
            else: 
                tmp.left = None
                del node
            return 

        if self.root is not None:
            if self.root.value == value:
                self.root = None
        else:
            queue = [self.root]
            while queue:# and value != current.value and current != None:
                current = queue.pop(0)
                if current.left.value==value: delete_node(current, "left")
                elif current.right.value==value: delete_node(current, "right")

    
    def get_coded_value(self,value) -> str:
        # cherche dans l'arbre et retourne la valeur codee pour le noeud
        def depth_first_rec(node, path="") -> str:
            if not node or node.value==value: return path

            #print(node.value)
            # print(path)
            depth_first_rec(node.left,path+"0")
            depth_first_rec(node.right,path+"1")
        
        return depth_first_rec(self.root)
    

    def create_tree(self, l):
        leaf_nodes = sort_list_nodes([Node(value=char, frequency=freq) for freq,char in l])
        size = len(leaf_nodes)
        while size > 1:
            sort_list_nodes(leaf_nodes)
            n1 = leaf_nodes.pop(0)
            n2 = leaf_nodes.pop(0)
    

def sort_list_nodes(l):
    l.sort(key=lambda node:node.frequency)
    return l


def code_message(message):
    # obtenir une liste avec la frequence des caracteres du message
    d = {el:message.count(el) for el in message}
    l = [(freq,c) for c,freq in d.items()]
    print(l)
    
    # comme son nom l'indique :
    tree = Huffman()
    tree.create_tree(l)


print(code_message(message="this is a test"))