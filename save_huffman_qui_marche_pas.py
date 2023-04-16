import binTree


class Node(object):
    
    def __init__(self, value=None, character=None, freq=None, left=None,right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.character = character
        self.freq = freq
        
    

class HuffmanTree(binTree.BinaryTree):
    # This class herits from binTree
    # note that adding/deleting/changing value of nodes in a Huffman Tree is non-sens
    
    def __init__(self, message=None, decoding=False, key=None):
        super().__init__()
        self.decoding = decoding
        self.message = str(message)
        
        # we use a Node with more attributes different 
        # than binTree.BinaryTree uses
        self.letters = []
        if not decoding: self.init()
        else:
            self.init_nodes(key)
    
    def get_key(self):
        l = self.frequence_letters()
        return l
    
    def init_nodes(self, key):
        l_nodes = []
        for freq,c in key:
            l_nodes.append(Node(value=f"{c}:{freq}", character=c, freq=int(freq)))
        
        self.init(l_nodes)
    
    def sort_list(self, l):
        # sort the list on the frequency of each node
        return sorted(l, key=lambda node: node.freq)

    def frequence_letters(self):
        # get a liste with frequencies of each character in the message
        d = {el:self.message.count(el) for el in self.message}
        l = [(freq,c) for c,freq in d.items()]
        return l

    def merge_nodes(self, node1, node2):
        new_node = Node(str(node1.freq+node2.freq), character="", freq=node1.freq+node2.freq,
                        left=node1, right=node2, parent=None)
        node1.parent = new_node 
        node2.parent = new_node

        return new_node

    def init(self, l_nodes=[]):
        
        if not self.decoding: 
            for freq,c in self.frequence_letters():
                n = Node(value=f"{c}:{freq}", character=c, freq=freq)
                self.letters.append(c)
                l_nodes.append(n)
        
        l_nodes = self.sort_list(l_nodes)

        
        while len(l_nodes)>1:
            node1 = l_nodes.pop(0)
            node2 = l_nodes.pop(0)
            new_node = self.merge_nodes(node1, node2)
            l_nodes = self.sort_list(l_nodes)
            l_nodes.append(new_node)
        
        self.root = l_nodes[0]
    
    def get_coded_value(self, value) -> str:
        
        def depth_first_rec(node, value, path=""):
            if node.character == value: return path
            else:
                p1, p2 = None, None
                if node.left:
                    p1 = depth_first_rec(node.left, value, path+"0")
                if node.right:
                    p2 = depth_first_rec(node.right, value, path+"1")
                
                return p1 if p1 is not None else p2
    
        
        return depth_first_rec(self.root, value)
    
    
    def encode(self):
        if not self.decoding:
            string = ""
            for c in self.message:
                string += self.get_coded_value(c)
            
            return string
        else:
            return ""
    
    def decode(self):
        pass

    
def encode(message):
    tree = HuffmanTree(str(message))
    return tree.encode(), tree.get_key()


if __name__ == '__main__':
    t1 = HuffmanTree("test")
    t2 = HuffmanTree("coucou")
    t1.display()
    t2.display()
    
    # methode 1
    # t1 = HuffmanTree("test")
    # t1.display()
    # key = t1.get_key()
    # print(t1.encode())
    
    # methode 2
    # coded_message, key = encode("test")
    # print(f"{coded_message=}")
    
    # t = HuffmanTree("010110", decoding=True, key=key)
    # t.display()
    
    # print(t.encode())
    # print(t.get_key())
    # for i in range(len(l)):
    #     print(t.get_coded_value(l[i]))