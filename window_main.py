import tkinter as tk
from numpy import log2
import binTree, subWin, Huffman


class Pointer(object):
    # Used as a pointer - to avoid global variables
    def __init__(self):
        self.value = None


class Spacer(tk.Label):
    def __init__(self, frame):
        super().__init__(frame, text=" ")
        self.pack()


class MainWindow(object):

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PyTree GUI")
        # self.window.geometry("1350x830")

        # Frame
        self.frame1 = tk.Frame(self.window) # for buttons/labels
        self.frame2 = tk.Frame(self.window, height=800, width=1200) # for the canvas
        
        # The main Canvas
        self.canvas = tk.Canvas(self.frame2, height=800, width=1200)

        self.l_pointers = []
        self.tree = binTree.BinaryTree()

        # Labels
        t_title1 = tk.Label(self.frame1, text="Binary tree")
        t_title2 = tk.Label(self.frame1, text="Huffman (overrides current tree)")
        t_title3 = tk.Label(self.frame1, text="Other functionalities")

        # Buttons
        b_add_node = tk.Button(self.frame1, text="Add a node", command=self.add_node)
        b_remove_node = tk.Button(self.frame1, text="Remove a node", command=self.remove_node)
        b_open_tree = tk.Button(self.frame1, text="Open a file", command=self.open_tree)
        b_save_tree = tk.Button(self.frame1, text="Save as a file", command=self.save_tree)
        b_delete_all = tk.Button(self.frame1, text="Delete all nodes", command=self.delete_all_tree)
        b_encode = tk.Button(self.frame1, text="Encode message", command=self.encode)
        b_decode = tk.Button(self.frame1, text="Decode message", command=self.decode)
        b_modify = tk.Button(self.frame1, text="Modify a node", command=self.modify_node)
        b_decompose = tk.Button(self.frame1, text="Decompose tree", command=self.decompose_tree)

        # Sroll bars
        self.scroll_bar1 = tk.Scrollbar(self.frame2, orient="horizontal", command=self.canvas.xview)
        self.scroll_bar2 = tk.Scrollbar(self.frame2, orient="vertical", command=self.canvas.yview)
        self.canvas.config(xscrollcommand=self.scroll_bar1.set, yscrollcommand=self.scroll_bar2.set)

        # buttons etc on the window
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=0, column=1)

        t_title1.pack(pady=5,padx=10)
        b_add_node.pack()
        b_remove_node.pack()
        b_modify.pack()
        Spacer(self.frame1)

        t_title2.pack(pady=5,padx=10)
        b_encode.pack()
        b_decode.pack()
        Spacer(self.frame1)
        
        t_title3.pack(pady=5,padx=10)
        b_delete_all.pack()
        b_open_tree.pack()
        b_decompose.pack()
        Spacer(self.frame1)
        b_save_tree.pack()
        b_delete_all.pack()
        Spacer(self.frame1)

        self.scroll_bar2.pack(side="right", fill='y')
        self.scroll_bar1.pack(side="bottom", fill='x')
        self.canvas.pack(expand=True, side="left")

        
        self.draw_tree(self.tree) 
    
    
    def display(self):
        self.window.mainloop()

    def add_node(self):
        subWin.SubWindow("add", self)
    
    def remove_node(self):
        subWin.SubWindow("delete", self)

    def open_tree(self):
        subWin.SubWindow("open", self)
        
    def save_tree(self):
        subWin.SubWindow("save", self)
    
    def encode(self):
        subWin.SubWindow("encode", self)

    def decode(self):
        subWin.SubWindow("decode", self)

    def modify_node(self):
        subWin.SubWindow("modify", self)
    
    def decompose_tree(self):
        subWin.decomposition(self.tree)
        
    
    def delete_all_tree(self):
        self.tree.delete_all()
        self.draw_tree(self.tree)


    def draw_tree(self, tree):

        self.canvas.delete("all") # delete everything on the canvas
        if tree.root == None: return
        circle_radius = 20
        total_height = tree.get_height()
        line_width = 1

        canvas_size = ((2**(total_height)) * circle_radius*2, total_height*circle_radius*2 + 2)
        # because of the scrollbars we don't adjust the size of the canvas, for some reasons...
        # self.canvas.configure(width=canvas_size[0], height=canvas_size[1])
        
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
                y = current_height * circle_radius * 3 + circle_radius + 2 


                if current_height > 0:
                    canvas.create_line(int(old_rel_x/(2**(current_height)) * canvas_size[0]), 
                                        (current_height-1) * circle_radius * 3 + circle_radius, 
                                        x,
                                        y-circle_radius,
                                        width=line_width)


                old_rel_x = rel_x

                walk_tree_rec(node.left, current_height+1, old_rel_x, left_nominator, canvas, canvas_size, circle_radius)
                walk_tree_rec(node.right, current_height+1, old_rel_x, right_nominator, canvas, canvas_size, circle_radius)
                canvas.create_oval(x-circle_radius, 
                                    y-circle_radius,
                                    x+circle_radius, 
                                    y+circle_radius, fill="white")

                canvas.create_text(x,y, text=str(node.value))
        
        walk_tree_rec(node=tree.root,
                      current_height=0,
                      old_rel_x="パスタ!", # it's overwrite after...
                      rel_x=1,
                      canvas=self.canvas,
                      canvas_size=canvas_size,
                      circle_radius=circle_radius)

        self.canvas.config(scrollregion=self.canvas.bbox("all"))



win = MainWindow()
win.display()
