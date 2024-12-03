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

# import tkinter as tk
# from tkinter import filedialog, messagebox
# import csv


# class Ellipse:
#     """Класс для работы с эллипсом."""
#     def __init__(self, x, y, width, height, color="black"):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = color

#     def move(self, dx, dy):
#         """Перемещает эллипс на заданное расстояние."""
#         self.x += dx
#         self.y += dy


#     def change_color(self, new_color):
#         """Меняет цвет эллипса."""
#         self.color = new_color

#     def to_dict(self):
#         """Возвращает данные эллипса в виде словаря."""
#         return {"x": self.x, "y": self.y, "width": self.width, "height": self.height, "color": self.color}

#     @staticmethod
#     def from_dict(data):
#         """Создает объект Ellipse из словаря."""
#         return Ellipse(int(data["x"]), int(data["y"]), int(data["width"]), int(data["height"]), data["color"])


# class EllipseApp:
#     """Приложение для управления эллипсами."""
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Управление эллипсами")
#         self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
#         self.canvas.pack(fill=tk.BOTH, expand=True)
#         self.ellipses = []

#         # Создание панели управления
#         self.panel = tk.Frame(root)
#         self.panel.pack(side=tk.LEFT, fill=tk.Y)

#         tk.Button(self.panel, text="Загрузить из файла", command=self.load_from_file).pack(pady=5)
#         tk.Button(self.panel, text="Сохранить в файл", command=self.save_to_file).pack(pady=5)
#         tk.Button(self.panel, text="Добавить эллипс", command=self.add_ellipse).pack(pady=5)
#         tk.Button(self.panel, text="Переместить эллипс", command=self.move_ellipse).pack(pady=5)
#         tk.Button(self.panel, text="Изменить цвет", command=self.change_ellipse_color).pack(pady=5)

#     def load_from_file(self):
#         """Загружает эллипсы из CSV файла."""
#         file_path = filedialog.askopenfilename(filetypes=[("CSV файлы", "*.csv")])
#         if not file_path:
#             return

#         try:
#             with open(file_path, newline='') as csvfile:
#                 reader = csv.DictReader(csvfile)
#                 self.ellipses = [Ellipse.from_dict(row) for row in reader]
#             self.render_ellipses()
#             messagebox.showinfo("Успех", "Данные успешно загружены.")
#         except Exception as e:
#             messagebox.showerror("Ошибка", f"Ошибка загрузки файла: {e}")

#     def save_to_file(self):
#         """Сохраняет эллипсы в CSV файл."""
#         file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV файлы", "*.csv")])
#         if not file_path:
#             return

#         try:
#             with open(file_path, mode='w', newline='') as csvfile:
#                 fieldnames = ["x", "y", "width", "height", "color"]
#                 writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#                 writer.writeheader()
#                 for ellipse in self.ellipses:
#                     writer.writerow(ellipse.to_dict())
#             messagebox.showinfo("Успех", "Данные успешно сохранены.")
#         except Exception as e:
#             messagebox.showerror("Ошибка", f"Ошибка сохранения файла: {e}")

#     def add_ellipse(self):
#         """Добавляет новый эллипс."""
#         self.ellipses.append(Ellipse(100, 100, 50, 30, "black"))
#         self.render_ellipses()

#     def move_ellipse(self):
#         """Перемещает эллипс."""
#         if not self.ellipses:
#             messagebox.showerror("Ошибка", "Нет эллипсов для перемещения.")
#             return

#         self.ellipses[-1].move(dx, dy)
#         self.render_ellipses()

#     def change_ellipse_color(self):
#         """Меняет цвет эллипса."""
#         if not self.ellipses:
#             messagebox.showerror("Ошибка", "Нет эллипсов для изменения цвета.")
#             return

#         new_color = "blue"
#         self.ellipses[-1].change_color(new_color)
#         self.render_ellipses()

#     def render_ellipses(self):
#         """Отображает эллипсы на холсте."""
#         self.canvas.delete("all")
#         for ellipse in self.ellipses:
#             self.canvas.create_oval(
#                 ellipse.x,
#                 ellipse.y,
#                 ellipse.x + ellipse.width,
#                 ellipse.y + ellipse.height,
#                 fill=ellipse.color
#             )


# root = tk.Tk()
# app = EllipseApp(root)
# root.mainloop()