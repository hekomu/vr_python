import tkinter
import tkinter.font

def click_btn():
    labelE=tkinter.Label(root, text="동", font=("새굴림",24))
    labelE.place(x=600,y=200)
    labelW=tkinter.Label(root, text="서", font=("새굴림",24))
    labelW.place(x=200,y=200)
    labelS=tkinter.Label(root, text="남", font=("새굴림",24))
    labelS.place(x=400,y=300)
    labelN=tkinter.Label(root, text="북", font=("새굴림",24))
    labelN.place(x=400,y=100)

    txt=entry.get()
    str1= txt
    labeltxt=tkinter.Label(root, text=str1, font=("새굴림",24))
    labeltxt.place(x=250,y=350)



root =tkinter.Tk()

root.title("첫번째 윈도우")
root.geometry("800x600")

entry= tkinter.Entry(width=5)
entry.place(x=200,y=350,width=40)

btn=tkinter.Button(root, text="버튼",font=("새굴림",10),command=click_btn)
btn.place(x=250, y=350, width=42, height=32)

"""print(tkinter.font.families())"""


root.mainloop()