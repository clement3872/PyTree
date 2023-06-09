import tkinter as tk
import os, pyperclip
import binTree, Huffman, platform


class Spacer(tk.Label):
    def __init__(self, frame):
        super().__init__(frame, text=" ")
        self.pack()

class ErrorWindow(object):
    """Class to create a popup window

    """
    def __init__(self, message=""):
        self.window = tk.Tk()
        self.window.geometry("300x120")
        self.window.title("Error")
        
        text_error = tk.Label(self.window, text=f"Error:\n{message}")
        b = tk.Button(self.window, text="OK", command=self.window.destroy)

        text_error.place(relx=.5, rely=.5, anchor="center")
        b.place(relx=.5, rely=1, anchor="s")

        self.window.mainloop()

def decomposition(tree):
    """Display the decomposition of the current tree in a new window

    Args:
        tree (BinaryTree): The targeted tree
    """
    l_nodes = tree.decomposition(tree.root)
    if len(l_nodes) > 0:
        tmp_win = tk.Tk()
        tmp_win.title("Decomposition")
        string = ""
        for node in l_nodes:
            string += f"{str(node.value)}{str(node)}\n"
        tk.Label(tmp_win, text=string).pack(padx=10,pady=10)
        
        tmp_win.mainloop()
    else:
        ErrorWindow("Tree is empty")


class GiveCodeWindow():
    """Create a new window to display a message
    """
    def __init__(self, message="", key=""):
        """Constructor of GiveCodeWindow class.

        Args:
            message (str): The message to show. Defaults to "".
            key (str): The key to show. Defaults to "".
        """
        self.message = str(message)
        self.key = str(key)

        window = tk.Tk()
        window.title("Message box")
        window.geometry("250x140")


        t1 = tk.Label(window, text="Message: "+str(message))
        t2 = tk.Label(window, text="Key: "+str(key))
        b_copy1 = tk.Button(window, text="Copy message", command=self.copy_message)
        b_copy2 = tk.Button(window, text="Copy key", command=self.copy_key)

        if self.message.strip() != "":
            Spacer(window)
            t1.pack()
            b_copy1.pack()
        if self.key.strip() != "":
            Spacer(window)
            t2.pack()
            b_copy2.pack()
            window.geometry("250x220")
        
        b = tk.Button(window, text="OK", command=window.destroy)
        b.pack(pady=20)
        
        window.mainloop()
    
    def copy_message(self):
        """Copies the message to the clipboard
        """
        if platform.system() != "Linux":
            pyperclip.copy(str(self.message))
        else:
            pyperclip.set_clipboard("xclip")
            pyperclip.copy(str(self.message))
    
    def copy_key(self):
        """Copies the key to the clipboard
        """
        if platform.system() != "Linux":
            pyperclip.copy(str(self.key))
        else:
            pyperclip.set_clipboard("xclip")
            pyperclip.copy(str(self.key))
    



class SubWindow(object):
    """Class to create subwindow"""
    def __init__(self, action, main_window):
        """Constructor of the SubWindow class

        Args:
            action (str): ('add', 'delete', 'open', 'save', 'encode', 'decode, 'modify')
            main_window (MainWindow): The main window
        """
        self.main_window = main_window

        self.window = tk.Tk()
        self.window.title("Sub Window")
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
        elif action == "modify":
            self.set_modify_interface()
        

        self.label.pack()
        self.entry.pack()
        if action in ["decode", "modify"]:
            self.label2.pack()
            self.entry2.pack()
        self.b_apply.pack()
        
        self.window.mainloop()


    def set_add_interface(self):
        """Set the interface to add a node"""
        self.window.title("Adding a node")
        self.label.config(text="Value to insert:")
        self.b_apply.config(text="Add node", command=self.add_node)

    
    def set_delete_interface(self):
        """Set the interface to remove a node
        """
        self.window.title("Removing a node")
        self.label.config(text="Value to delete:")
        self.b_apply.config(text="delete node", command=self.delete_node)


    def set_open_interface(self):
        """Set the interface to load a tree from a file
        """
        self.window.title("Open a file")
        self.label.config(text="Path to the file (default is save.txt):")
        self.b_apply.config(text="Open saved tree", command=self.open_tree)

    def set_save_interface(self):
        """Set the interface to save the current tree in a txt file
        """
        self.window.title("Save to a file")
        self.label.config(text="Path to the file (default is save.txt):")
        self.b_apply.config(text="Save tree", command=self.save_tree)

    def set_encode_interface(self):
        """Set the interface to encode a message based on the user's entry
        """
        self.window.title("Encode a message")
        self.label.config(text="Message to encode:")
        self.b_apply.config(text="Encode", command=self.encode_tree)

    def set_decode_interface(self):
        """Set the interface to decode a message given by the user
        """
        self.window.title("Decode a message")
        self.label.config(text="Message to decode:")
        self.label2.config(text="key:")
        self.b_apply.config(text="Decode", command=self.decode_tree)
        self.window.geometry("250x130")

    def set_modify_interface(self):
        """Set the interface to modify a node in the current tree.
        """
        self.window.title("Modify node value:")
        self.label.config(text="Current node value:")
        self.label2.config(text="New value:")
        self.b_apply.config(text="Apply", command=self.modify)
        self.window.geometry("250x130")

    
    def add_node(self):
        """Add a node to the current tree"""
        if type(self.main_window.tree) == type(Huffman.HuffmanTree()):
            root = self.main_window.tree.root
            self.main_window.tree = binTree.BinaryTree()
            self.main_window.tree.root = root
        self.main_window.tree.insert(self.entry.get())
        self.main_window.draw_tree(self.main_window.tree)

    def delete_node(self):
        """Remove a node to the current tree
        """
        if not self.main_window.tree.delete(self.entry.get()):
            ErrorWindow("Node does not exist")
        self.main_window.draw_tree(self.main_window.tree)

    def encode_tree(self):
        """Encode a message givent by the user
        """
        message = self.entry.get()
        if message.strip() != "":
            self.main_window.tree.delete_all()
            self.main_window.tree = Huffman.HuffmanTree()
            message,key = self.main_window.tree.encode(message)

            self.main_window.draw_tree(self.main_window.tree)

            GiveCodeWindow(message, key)
    def decode_tree(self):
        """Decode a message givent by the user

        Returns:
            string: Decoded message
        """
        message = self.entry.get()
        key = self.entry2.get()
        
        if message.strip() != "":
            # Some security
            try:
                key = eval(key)
            except:
                ErrorWindow("Invalid key")
            
            self.main_window.tree.delete_all()
            self.main_window.tree = Huffman.HuffmanTree()
            message = self.main_window.tree.decode(message,key)
            self.main_window.draw_tree(self.main_window.tree)
            GiveCodeWindow(message)
        return message

    def open_tree(self):
        """Load a tree from a txt file. Defaults saved file is "save.txt".
        """
        path = self.entry.get()
        if path == "": path = "save.txt"
        if os.path.exists(path):
            with open(path, 'r') as f:
                l_lines = f.readlines()
            
            tree_type = l_lines[0]
            l_nodes = eval(l_lines[1]) # of the key it's for Huffman
            
            self.main_window.tree.delete_all()
            # insert the nodes, checking tree type first
            if tree_type == "binTree\n":
                self.main_window.tree = binTree.BinaryTree()
                for el in l_nodes:
                    self.main_window.tree.insert(el)
            elif tree_type == "Huffman\n":
                self.main_window.tree = Huffman.HuffmanTree()
                self.main_window.tree.display()
                self.main_window.tree.decode("",l_nodes)

            self.main_window.draw_tree(self.main_window.tree)
            self.window.destroy()
        else:
            ErrorWindow("Tree needs to be saved or invalid path, path:\n%s" % path)
        
    
    def save_tree(self):
        """Save the current tree in a txt file.
        """
        if self.main_window.tree.root != None:
            path = self.entry.get()
            if path == "": path = "save.txt"
            l_values = [node.value for node in self.main_window.tree.width_first(self.main_window.tree.root)]
            with open(path, 'w') as f:
                if type(self.main_window.tree) == type(Huffman.HuffmanTree()):
                    f.write("Huffman\n")
                    f.write(str(self.main_window.tree.key))
                else:
                    f.write("binTree\n")
                    f.write(str(l_values))
        
            self.window.destroy()
        else:
            ErrorWindow("Insert a node into the tree first...")
    
    def modify(self):
        """Modify a node in the current tree"""
        current_value = self.entry.get()
        new_value = self.entry2.get()
        
        self.main_window.tree.change_value(current_value, new_value)
        self.main_window.draw_tree(self.main_window.tree)