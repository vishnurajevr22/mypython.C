import tkinter as tk

root = tk.Tk()
root.title("canvas sample")
c = tk.Canvas(root, width=1000, height=1000, bg="white")
c.pack()
d = [
    c.create_rectangle(100, 150, 150, 200, outline="red", fill="pink"),
    c.create_rectangle(160, 150, 210, 200, outline="red", fill="pink"),
    c.create_rectangle(220, 150, 270, 200, outline="red", fill="pink"),
    c.create_rectangle(280, 150, 330, 200, outline="red", fill="blue"),
    c.create_oval(110, 200, 120, 210, outline="red", fill="black"),
    c.create_oval(130, 200, 140, 210, outline="red", fill="black"),
    c.create_oval(170, 200, 180, 210, outline="red", fill="black"),
    c.create_oval(190, 200, 200, 210, outline="red", fill="black"),
    c.create_oval(230, 200, 240, 210, outline="red", fill="black"),
    c.create_oval(250, 200, 260, 210, outline="red", fill="black"),
    c.create_oval(290, 200, 300, 210, outline="red", fill="black"),
    c.create_oval(310, 200, 320, 210, outline="red", fill="black"),
]


def nmove():
    for i in d:
        c.move(i, 3, 0)
    c.after(30, nmove)


nmove()

root.mainloop()
