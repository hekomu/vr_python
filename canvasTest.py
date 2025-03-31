import tkinter
root=tkinter.Tk()
root.title("캔버스 만들기")
canvas=tkinter.Canvas(root,width=400,height=600,bg="skyblue")
bgImg=tkinter.PhotoImage(file="dd.jpg")
canvas.create_image(200,300,img=bgImg)
canvas.pack()


root.mainloop()