

class Node(object):

    def __init__(self, value=None, character=None, freq=None, left=None,right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.character = character
        self.freq = freq
    

def sort_list_nodes(l):
    l.sort(key=lambda node:node.freq)
    return l

def frequence_message(message):
    # obtenir une liste avec la frequence des caracteres du message
    d = {el:message.count(el) for el in message}
    l = [(freq,c) for c,freq in d.items()]
    return l


def merge_nodes(node1, node2):
    new_node = Node(str(node1.freq+node2.freq), character="", freq=node1.freq+node2.freq,
                    left=node1, right=node2, parent=None)
    node1.parent = new_node 
    node2.parent = new_node

    return new_node

def create_huffman(l_nodes):
    while len(l_nodes)>1:
        node1 = l_nodes.pop(0)
        node2 = l_nodes.pop(0)
        new_node = merge_nodes(node1, node2)
        l_nodes = sort_list_nodes(l_nodes)
        l_nodes.append(new_node)
    
    return l_nodes[0]


def width_first_global(node) -> list:
    if node is None: return 
    
    l_nodes = []
    queue = [node]
    while queue:
        node = queue.pop(0)
        l_nodes.append(node)
        
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right) 
    
    return l_nodes


def test(message):
    freq = frequence_message(message)
    l_nodes = []
    for freq,c in freq:
        n = Node(value=f"{c}:{freq}", character=c, freq=freq)
        l_nodes.append(n)
    
    l_nodes = sort_list_nodes(l_nodes)

    root = create_huffman(l_nodes)
    l = width_first_global(root)
    return root
    # for node in l:
    #     print(node.value)




if __name__ == '__main__':
    test("test")