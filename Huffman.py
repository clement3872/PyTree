import binTree


class HuffmanTree(binTree.BinaryTree):
    """HuffmanTree
        Herits of a binTree.BinaryTree
    """    
    
    def __init__(self):
        super().__init__()
        self.message = ""
        self.key = ""

    def get_frequency(self):
        """
        Returns the frequencies for each letter in a dictionary
        """
        d = {}
        for c in self.message:
            d[c] = self.message.count(c)
        return d

    def get_frequency_node(self, node):
        """get_frequency_node, a value of the Node

        Args:
            node (Node object): The node to get the frequency

        Returns:
            int: the frequency (it's for Huffman...)
        
        More details:
            node.value can be like "t:12" so we need to the 2 first characters 
            to get the frequency or it's like 16 so we need the value only
        """
        if type(node.value) == type(int()):
            return node.value
        else:
            return int(node.value[2:])
    
    def get_character(self, node):
        """get_character, a value of the Node

        Args:
            node (Node object): The node to get the character

        Returns:
            int or str: the charater (it's for Huffman...)
        """        
        if type(node.value) == type(int()):
            return node.value
        else:
            return node.value[0]
    
    def sort_list_nodes(self, l_nodes):
        """sort_list_nodes
            Sort the list in function of the frequencies of each node
        """
        return sorted(l_nodes, key=self.get_frequency_node)
    
    def merge_nodes(self, node1, node2):
        """merge_nodes, creates a new parent node, 
                node1 and node2 are left and right sons of the new node

        Args:
            node1 (Node object): left son
            node2 (Node object): right son

        Returns:
            Node Oject: new parent Node
        """        
        freq_n1 = self.get_frequency_node(node1)
        freq_n2 = self.get_frequency_node(node2)
        parent_node = binTree.Node(value=freq_n1+freq_n2,
                        left=node1,
                        right=node2)
        node1.parent = parent_node
        node2.parent = parent_node
        return parent_node
    
    def create_tree(self):
        """create_tree, Initialize a Huffman tree
        self.key needs to be set first (dictionnary on frequencies)
        """        
        l_nodes  = []
        for c,freq in self.key.items():
            l_nodes.append(binTree.Node(value=f"{c}:{freq}"))

        l_nodes = self.sort_list_nodes(l_nodes)
        
        while len(l_nodes)>1:
            node1 = l_nodes.pop(0)
            node2 = l_nodes.pop(0)
            new_node = self.merge_nodes(node1, node2)
            l_nodes.append(new_node)
            
            l_nodes = self.sort_list_nodes(l_nodes)
        
        self.root = l_nodes[0]
    
    
    def encode(self, message):
        """encode, encode the given message

        Args:
            message (str): message to encode

        Returns:
            (str, dict): (encoded message, the key)
        """        
        self.message = message
        self.key = self.get_frequency()
        self.create_tree()
        
        l = self.get_coded_tree()
        d_coded_values = {}
        for code,value in l:
            if type(value) is str: 
                d_coded_values[value[0]] = code
        
        encoded_message = ""
        for c in self.message:
            encoded_message += str(d_coded_values[c])
        
        return encoded_message,self.key
        
    def decode(self, message, key):
        """decode, decode the given message with key if it's possible

        Args:
            message (str): message to decode
            key (dict): the key

        Returns:
            str: decoded message
        """ 
        
        self.message = message
        self.key = key
        self.create_tree()
        
        decoded_message = ""
        current = self.root
        for bit in message:
            if bit == '0' and current.left is not None:
                current = current.left
            else:
                current = current.right
            if current.left is None and current.right is None:
                    decoded_message += current.value[0]
                    current = self.root
            
        return decoded_message


if __name__ == '__main__':
    t1 = HuffmanTree()
    print(t1.encode("test"))
    t2 = HuffmanTree()
    print(t2.decode('010110',{'t': 2, 'e': 1, 's': 1}))

    t1.display()
    t2.display()