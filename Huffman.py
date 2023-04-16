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
    
    def __init__(self, message=None):
        super().__init__()
        
        self.message = message
        
        # we use a Node with more attributes different 
        # than binTree.BinaryTree uses
        self.root = None; self.init()
        
    
    def open(self, d_tree):
        # TO DO
        pass
    
    def sort_list(self, l):
        # sort the list on the frequency of each node
        l.sort(key=lambda node:node.freq)
        return l

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

    def merge_nodes(self, node1, node2):
        new_node = Node(str(node1.freq+node2.freq), character="", freq=node1.freq+node2.freq,
                        left=node1, right=node2, parent=None)
        node1.parent = new_node 
        node2.parent = new_node

        return new_node

    def init(self):
        
        l_nodes = []
        for freq,c in self.frequence_letters():
            n = Node(value=f"{c}:{freq}", character=c, freq=freq)
            l_nodes.append(n)
        
        l_nodes = self.sort_list(l_nodes)

        
        while len(l_nodes)>1:
            node1 = l_nodes.pop(0)
            node2 = l_nodes.pop(0)
            new_node = self.merge_nodes(node1, node2)
            l_nodes = self.sort_list(l_nodes)
            l_nodes.append(new_node)
        
        self.root = l_nodes[0]
        


if __name__ == '__main__':
    t = HuffmanTree("test")
    t.display()
