import tkinter as tk
import os

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


class SubWindow(object):
    
    def __init__(self, action,tree, main_window):
        self.tree = tree
        self.main_window = main_window

        self.window = tk.Tk()
        self.window.geometry("250x100")

        self.entry = tk.Entry(self.window)

        self.labeltk.Label(self.window, text="No action defined")
        self.b_apply = tk.Button(self.window, text="OK", command=self.window.destroy)

        if action == "add":
            self.set_add_interface()
        elif action == "delete":
            self.set_delete_interface()
        elif action == "open":
            self.set_open_interface()
        elif action == "save":
            self.set_save_interface()
        

        label.pack()
        self.entry.pack()
        self.b_apply.pack()

        self.window.mainloop()


    def set_add_interface(self):
        self.labeltk.Label(self.window, text="Value to insert:")
        self.b_apply = tk.Button(self.window, text="Add node", command=self.add_node)

    
    def set_delete_interface(self):
        self.labeltk.Label(self.window, text="Value to delete:")
        self.entry = tk.Entry(self.window)
        self.b_apply = tk.Button(self.window, text="delete node", command=self.delete_node)


    def set_open_interface(self):
        self.labeltk.Label(self.window, text="Path to the file (default is save.txt):")
        self.entry = tk.Entry(self.window)
        self.b_apply = tk.Button(self.window, text="Open saved tree", command=self.open_tree)


    def set_save_interface(self):
        self.labeltk.Label(self.window, text="Path to the file (default is save.txt):")
        self.entry = tk.Entry(self.window)
        self.b_apply = tk.Button(self.window, text="Save tree", command=self.save_tree)

    
    def add_node(self):
        self.tree.insert(self.entry.get())

        self.main_window.draw_tree(self.tree)

    
    def delete_node(self):
        self.tree.delete(self.entry.get())

        self.main_window.draw_tree(self.tree)
    
    def open_tree(self):
        path = self.entry.get()
        if path == "": path = "save.txt"
        if os.path.exists(path):
            with open(path, 'r') as f:
                l = eval(f.readlines()[0])
            
            self.tree.delete_all()
            for el in l:
                self.tree.insert(el)
            self.main_window.draw_tree(self.tree)
            self.window.destroy()
        else:
            ErrorWindow("Tree needs to be saved or invalid path, path:\n%s" % path)
        
    
    def save_tree(self):
        if self.tree.root != None:
            path = self.entry.get()
            if path == "": path = "save.txt"
            l_values = [node.value for node in self.tree.width_first_global(self.tree.root)]
            with open(path, 'w') as f:
                f.write(str(l_values))
            self.main_window.draw_tree(self.tree)
            self.window.destroy()
        else:
            ErrorWindow("Insert a node into the tree first...")