import tkinter as tk
from tkinter import PhotoImage
import random


def click_btn():
    result_label["text"]=random.choice(["대길","중길","소길","흉"])
    text.insert(tk.END, result_label["text"] + "\n")


def mouseMove(event):
    x=event.x
    y=event.y
    labelMouse["test"]=str(x)+","+str(y)


root = tk.Tk()
root.title("제비뽑기")
root.geometry("800x600")


root.bind("<Motion>", mouseMove)
labelMouse=tk.Label(root,text=",")
labelMouse.pack()

canvas = tk.Canvas(root, width=800, height=600)
canvas.place(x=0, y=0)
canvas.create_rectangle(351, 394, 601, 520, fill="darkgray", outline="red", width=5)


bg_img = PhotoImage(file="miko.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


result_label = tk.Label(root, text="??", font=("맑은 고딕",80), bg="white")
result_label.place(x=380, y=100)

draw_button = tk.Button(root, text="제비뽑기", font=("맑은 고딕", 30),
                        command=click_btn
                    )
draw_button.place(x=385, y=380)


text=tk.Text()
text.pack()





root.mainloop()