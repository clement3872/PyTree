import tkinter as tk
import binTree
from numpy import log2
import subWin


class Pointer(object):
    # Used as a pointer - to avoid global variables
    def __init__(self):
        self.value = None


class MainWindow(object):

    def __init__(self):
        self.window = tk.Tk()

        # Frame
        self.frame1 = tk.Frame(self.window) # for buttons
        self.frame2 = tk.Frame(self.window) # for the canvas

        self.l_pointers = []
        self.tree = binTree.BinaryTree()

        # Buttons
        b_add_node = tk.Button(self.frame1, text="Add node", command=self.add_node)
        b_remove_node = tk.Button(self.frame1, text="Remove node", command=self.remove_node)
        b_open_tree = tk.Button(self.frame1, text="Open tree", command=self.open_tree)
        b_save_tree = tk.Button(self.frame1, text="Save tree", command=self.save_tree)
        b_encode = tk.Button(self.frame1, text="Encode tree (not implemented)", command=None)

        self.canvas = tk.Canvas(self.frame2)

        # buttons etc on the window
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)
        b_add_node.pack()
        b_remove_node.pack()
        b_open_tree.pack()
        b_save_tree.pack()
        b_encode.pack()

        self.canvas.pack()

        for i in range(25):
            break
            self.tree.insert(str(i))
        
        # self.tree.delete(4)
        
        self.draw_tree(self.tree) 
    
    def display(self):
        self.window.mainloop()

    def add_node(self):
        sub_win = subWin.SubWindow("add", self.tree, self)
    
    def remove_node(self):
        sub_win = subWin.SubWindow("delete", self.tree, self)

    def open_tree(self):
        sub_win = subWin.SubWindow("open", self.tree, self)
        
    def save_tree(self):
        sub_win = subWin.SubWindow("save", self.tree, self)

    def draw_tree(self, tree):

        self.canvas.delete("all") # delete everything on the canvas
        if tree.root == None: return
        circle_radius = 20
        total_height = tree.get_height()
        line_width = 1

        canvas_size = ((2**(total_height)) * circle_radius*2, total_height*circle_radius*2 + 2)
        self.canvas.configure(width=canvas_size[0], height=canvas_size[1])
        # self.canvas.configure(height=1000, width=1900)
        # canvas_size = (1000,1900)

        def walk_tree_rec(node, current_height, old_rel_x, rel_x, canvas, canvas_size, circle_radius):
            """
            at the first iteration we need:
            current_height=0
            rel_x=1
            old_rel_x = 0 # or whatever
            """
            if node == None: return
            else:

                left_nominator = 2*rel_x - 1 # futur rel_x for left branch
                right_nominator = 2*rel_x + 1 # futur rel_x for right branch
                denominator = 2**(current_height+1)
                
                x = int(rel_x/denominator * canvas_size[0]) 
                y = current_height * circle_radius * 2 + circle_radius + 2 


                if current_height > 0:
                    canvas.create_line(int(old_rel_x/(2**(current_height)) * canvas_size[0]), 
                                        (current_height-1) * circle_radius * 2+ 2*circle_radius, 
                                        x,
                                        y-circle_radius,
                                        width=line_width)

                canvas.create_oval(x-circle_radius, 
                                    y-circle_radius,
                                    x+circle_radius, 
                                    y+circle_radius, fill="white")

                canvas.create_text(x,y, text=str(node.value))
                old_rel_x = rel_x

                walk_tree_rec(node.left, current_height+1, old_rel_x, left_nominator, canvas, canvas_size, circle_radius)
                walk_tree_rec(node.right, current_height+1, old_rel_x, right_nominator, canvas, canvas_size, circle_radius)
        
        walk_tree_rec(node=tree.root,
                      current_height=0,
                      old_rel_x="パスタ!", # it's overwrite after...
                      rel_x=1,
                      canvas=self.canvas,
                      canvas_size=canvas_size,
                      circle_radius=circle_radius)
    


# tree = binTree.BinaryTree()
# for i in range(10): tree.insert(str(i))

# sw = subWin.SubWindow("delete", tree)
# tree.display()



win = MainWindow()
win.display()