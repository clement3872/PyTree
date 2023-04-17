import tkinter as tk
import os
import binTree, Huffman



class Spacer(tk.Label):
    def __init__(self, frame):
        super().__init__(frame, text=" ")
        self.pack()


class ErrorWindow(object):
    def __init__(self, message=""):
        self.window = tk.Tk()
        self.window.geometry("300x120")
        self.window.title("Error")
        
        text_error = tk.Label(self.window, text=f"Error:\n{message}")
        b = tk.Button(self.window, text="OK", command=self.window.destroy)

        text_error.place(relx=.5, rely=.5, anchor="center")
        b.place(relx=.5, rely=1, anchor="s")

        self.window.mainloop()

def giveCodeWindow(message="", key=""):
    # why this doesn't work ???
    window = tk.Tk()
    
    Spacer(window)

    strv1 = tk.StringVar(); strv1.set(str(message))
    strv2 = tk.StringVar(); strv2.set(str(key))

    t1 = tk.Entry(window, textvariable=strv1)
    t2 = tk.Entry(window, textvariable=strv2)

    t1.pack()
    t2.pack()
    
    b = tk.Button(window, text="OK")
    b.pack(pady=20)
    
    window.mainloop()



class SubWindow(object):
    
    def __init__(self, action,tree, main_window):
        self.tree = tree
        self.main_window = main_window

        self.window = tk.Tk()
        self.window.geometry("250x100")


        self.entry = tk.Entry(self.window, text="")
        self.entry2 = tk.Entry(self.window, text="")

        self.label = tk.Label(self.window, text="No action defined")
        self.label2 = tk.Label(self.window, text="key:")
        self.b_apply = tk.Button(self.window, text="OK", command=self.window.destroy)

        if action == "add":
            self.set_add_interface()
        elif action == "delete":
            self.set_delete_interface()
        elif action == "open":
            self.set_open_interface()
        elif action == "save":
            self.set_save_interface()
        elif action == "encode":
            self.set_encode_interface()
        elif action == "decode":
            self.set_decode_interface()
        

        self.label.pack()
        self.entry.pack()
        if action == "decode":
            self.label2.pack()
            self.entry2.pack()
        self.b_apply.pack()

        self.window.mainloop()


    def set_add_interface(self):
        self.label.config(text="Value to insert:")
        self.b_apply.config(text="Add node", command=self.add_node)

    
    def set_delete_interface(self):
        self.label.config(text="Value to delete:")
        self.b_apply.config(text="delete node", command=self.delete_node)


    def set_open_interface(self):
        self.label.config(text="Path to the file (default is save.txt):")
        self.b_apply.config(text="Open saved tree", command=self.open_tree)

    def set_save_interface(self):
        self.label.config(text="Path to the file (default is save.txt):")
        self.b_apply.config(text="Save tree", command=self.save_tree)

    def set_encode_interface(self):
        self.label.config(text="Message to encode:")
        self.b_apply.config(text="Encode", command=self.encode_tree)

    def set_decode_interface(self):
        self.label.config(text="Message to decode:")
        self.label2.config(text="key:")
        self.b_apply.config(text="Decode", command=self.decode_tree)
        self.window.geometry("250x130")
    
    def add_node(self):
        self.tree.insert(self.entry.get())
        self.main_window.draw_tree(self.tree)

    def delete_node(self):
        if not self.tree.delete(self.entry.get()):
            ErrorWindow("Node does not exist")
        self.main_window.draw_tree(self.tree)

    def encode_tree(self):
        self.tree.delete_all()
        message = self.entry.get()
        self.tree = Huffman.HuffmanTree()
        message,key = self.tree.encode(message)

        self.main_window.draw_tree(self.tree)

        giveCodeWindow(message, key)


    
    def decode_tree(self):
        pass

    def open_tree(self):
        path = self.entry.get()
        if path == "": path = "save.txt"
        if os.path.exists(path):
            with open(path, 'r') as f:
                l_lines = f.readlines()
            
            tree_type = l_lines[0]
            l_nodes = eval(l_lines[1]) # of the key it's for Huffman
            
            self.tree.delete_all()
            # insert the nodes, checking tree type first
            if tree_type == "binTree\n":
                self.tree = binTree.BinaryTree()
                for el in l:
                    self.tree.insert(el)
            elif tree_type == "Huffman\n":
                self.tree = Huffman.HuffmanTree()
                self.tree.display()
                self.tree.decode("",l_nodes)

            self.main_window.draw_tree(self.tree)
            self.window.destroy()
        else:
            ErrorWindow("Tree needs to be saved or invalid path, path:\n%s" % path)
        
    
    def save_tree(self):
        if self.tree.root != None:
            path = self.entry.get()
            if path == "": path = "save.txt"
            l_values = [node.value for node in self.tree.width_first(self.tree.root)]
            with open(path, 'w') as f:
                if type(self.tree) == type(Huffman.HuffmanTree()):
                    f.write("Huffman")
                    f.write(str(self.tree.key))
                else:
                    f.write("binTree")
                    f.write(str(l_values))
        
            self.window.destroy()
        else:
            ErrorWindow("Insert a node into the tree first...")