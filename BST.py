import tkinter as tk
import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BSTVisualizer:
    def __init__(self, canvas):
        self.root = None
        self.canvas = canvas
        self.node_radius = 20
        self.level_gap = 70
        self.x_gap = 40

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
        self.draw_tree()
        time.sleep(0.8)  # delay for animation

    def _insert(self, root, key):
        if key < root.key:
            if root.left:
                self._insert(root.left, key)
            else:
                root.left = Node(key)
        elif key > root.key:
            if root.right:
                self._insert(root.right, key)
            else:
                root.right = Node(key)

    def draw_tree(self):
        self.canvas.delete("all")
        if self.root:
            self._draw_node(self.root, 400, 50, 200)

    def _draw_node(self, node, x, y, x_offset):
        if node.left:
            self.canvas.create_line(x, y, x - x_offset, y + self.level_gap)
            self._draw_node(node.left, x - x_offset, y + self.level_gap, x_offset // 2)
        if node.right:
            self.canvas.create_line(x, y, x + x_offset, y + self.level_gap)
            self._draw_node(node.right, x + x_offset, y + self.level_gap, x_offset // 2)
        
        self.canvas.create_oval(
            x - self.node_radius, y - self.node_radius,
            x + self.node_radius, y + self.node_radius,
            fill="lightblue"
        )
        self.canvas.create_text(x, y, text=str(node.key), font=("Arial", 12, "bold"))

def run_visualization():
    root = tk.Tk()
    root.title("BST Visualization")
    canvas = tk.Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    tree = BSTVisualizer(canvas)

    # Nodes to insert one by one
    nodes_to_insert = [50, 30, 70, 20, 40, 60, 80]

    def animate():
        for key in nodes_to_insert:
            tree.insert(key)
            root.update()
            time.sleep(1)

    root.after(500, animate)  # start animation after 0.5s
    root.mainloop()

if __name__ == "__main__":
    run_visualization()