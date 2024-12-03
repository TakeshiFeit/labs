import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

class Ellipse:
    def __init__(self, x1, y1, x2, y2, color="black"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def new_color(self, color):
        self.color = color

    def from_dict(data):
        return Ellipse(int(data[0]), int(data[1]), int(data[2]), int(data[3]), data[4])

class EllipseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ellipses")
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.ellipses = []

        # Создание панели управления
        self.panel = tk.Frame(root)
        self.panel.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(self.panel, text="Load from file", command=self.load_from_file).pack(pady=5)
        tk.Button(self.panel, text="Move ellipse", command=self.move_ellipse).pack(pady=5)
        tk.Button(self.panel, text="Change color", command=self.change_color).pack(pady=5)
        tk.Button(self.panel, text="Segmentation", command=self.segmentation).pack(pady=5)


    def load_from_file(self):
        try:
            with open("text.txt") as txtfile:
                txt = txtfile.readline().split()
                self.ellipses = [Ellipse.from_dict(txt)]
            self.render_ellipses()
            messagebox.showinfo("Ыuccess", "Data loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"File upload error: {e}")

    def move_ellipse(self):
        if not self.ellipses:
            messagebox.showerror("Error", "There are no ellipses.")
            return

        dx = simpledialog.askinteger("Enter x", "Enter number:")
        dy = simpledialog.askinteger("Enter y", "Enter number:")
        self.ellipses[-1].move(dx, dy)
        self.render_ellipses()

    def change_color(self):
        if not self.ellipses:
            messagebox.showerror("Error", "There are no ellipses.")
            return

        n_color = simpledialog.askstring("Color", "Enter color:")
        self.ellipses[-1].new_color(n_color)
        self.render_ellipses()

    def segmentation(self):
        if not self.ellipses:
            messagebox.showerror("Error", "There are no ellipse.")
            return

        colors = ['red', 'green', 'blue', 'yellow']
        color_index = 0
        step = 360 // simpledialog.askinteger("Enter step", "Enter how many segments you need:")
        for a in range(0, 360, step):
            self.canvas.create_arc(
                self.ellipses[-1].x1, 
                self.ellipses[-1].y1, 
                self.ellipses[-1].x2, 
                self.ellipses[-1].y2, 
                start=a, 
                extent=step, 
                outline=colors[color_index])
            color_index = (color_index+1) % len(colors)

    def render_ellipses(self):
        self.canvas.delete("all")
        for ellipse in self.ellipses:
            self.canvas.create_oval(
                ellipse.x1,
                ellipse.y1,
                ellipse.x2,
                ellipse.y2,
                fill=ellipse.color
            )

root = tk.Tk()
app = EllipseApp(root)
root.mainloop()
