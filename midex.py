import tkinter

def btn_click():
    name=str(entryN.get())
    region=str(entryR.get())
    weight=int(entryW.get())

    str1="이름:",str(name)
    str2="주소:",str(region)
    str3="배송비:",int(weight)*5,"원"

    labelRes1=tkinter.Label(root,text=str1,font=("맑은고딕",10))
    labelRes1.place(x=50,y=200)
    labelRes2=tkinter.Label(root,text=str2,font=("맑은고딕",10))
    labelRes2.place(x=50,y=220)
    labelRes3=tkinter.Label(root,text=str3,font=("맑은고딕",10))
    labelRes3.place(x=50,y=240)


root=tkinter.Tk()
root.title("배송지 입력")
root.geometry("400x300")

labelN=tkinter.Label(root, text="받는 사람",font=("맑은 고딕",10))
labelR=tkinter.Label(root, text="주소",font=("맑은 고딕",10))
labelW=tkinter.Label(root, text="무게(g)",font=("맑은 고딕",10))

labelN.place(x=50, y=40)
labelR.place(x=50, y=80)
labelW.place(x=50, y=120)

btn=tkinter.Button(root, text="확인",command=btn_click)
btn.place(x=250,y=150)

entryN= tkinter.Entry(width=10)
entryR= tkinter.Entry(width=10)
entryW= tkinter.Entry(width=10)

entryN.place(x=120, y=40)
entryR.place(x=120, y=80)
entryW.place(x=120, y=120)


root.mainloop()