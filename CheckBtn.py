import tkinter
from tkinter import PhotoImage
import tkinter.messagebox


root = tkinter.Tk()
root.title("캔버스")
root.geometry("800x600")

result=[
    "전생에 고양이였을 가능성은 매우 낮습니다.",
    "보통 사람입니다.",
    "꽤 고양이다운 구석이 있습니다.",
    "고양이와 비슷한 성격인 것 같습니다.",
    "고양이와 근접한 성격입니다.",
    "전생에 고양이었을지도 모릅니다.",
    "겉모습은 사람이지만, 속은 고양이일 가능성이 있습니다."
]



def chkBtnClick():
    numCheck =0
    if cvalue1.get()==True: numCheck +=1
    if cvalue2.get()==True: numCheck +=1
    if cvalue3.get()==True: numCheck +=1
    if cvalue4.get()==True: numCheck +=1
    if cvalue5.get()==True: numCheck +=1
    if cvalue6.get()==True: numCheck +=1
    if cvalue7.get()==True: numCheck +=1
    print(numCheck)

def BtnClick() :   
    numCheck =0
    if cvalue1.get()==True: numCheck +=1
    if cvalue2.get()==True: numCheck +=1
    if cvalue3.get()==True: numCheck +=1
    if cvalue4.get()==True: numCheck +=1
    if cvalue5.get()==True: numCheck +=1
    if cvalue6.get()==True: numCheck +=1
    if cvalue7.get()==True: numCheck +=1
    print(numCheck)
    textFiled.delete("1.0",tkinter.END)
    textFiled.insert("1.0","<진단결과>\n 당신의 고양이 지수는"
                    +str(int(numCheck/7*100))+"%입니다. \n"
                    +result[numCheck])


bg_img = PhotoImage(file="mina.png")
bg_label = tkinter.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


cvalue1=tkinter.BooleanVar()
cvalue1.set(False)
cbtn1=tkinter.Checkbutton(text="높은 곳이 좋다.",variable=cvalue1,command=chkBtnClick)
cbtn1.place(x=402,y=165)

cvalue2=tkinter.BooleanVar()
cvalue2.set(False)
cbtn2=tkinter.Checkbutton(text="공을 보면 굴리고 싶다.",variable=cvalue2,command=chkBtnClick)
cbtn2.place(x=402,y=205)

cvalue3=tkinter.BooleanVar()
cvalue3.set(False)
cbtn3=tkinter.Checkbutton(text="깜짝 놀라면 털이 곤두선다",variable=cvalue3,command=chkBtnClick)
cbtn3.place(x=402,y=245)

cvalue4=tkinter.BooleanVar()
cvalue4.set(False)
cbtn4=tkinter.Checkbutton(text="쥐구멍이 맘에 든다",variable=cvalue4,command=chkBtnClick)
cbtn4.place(x=402,y=285)

cvalue5=tkinter.BooleanVar()
cvalue5.set(False)
cbtn5=tkinter.Checkbutton(text="개에게 적대감이 든다",variable=cvalue5,command=chkBtnClick)
cbtn5.place(x=402,y=325)

cvalue6=tkinter.BooleanVar()
cvalue6.set(False)
cbtn6=tkinter.Checkbutton(text="생선 뼈를 발라먹고 싶다",variable=cvalue6,command=chkBtnClick)
cbtn6.place(x=402,y=365)

cvalue7=tkinter.BooleanVar()
cvalue7.set(False)
cbtn7=tkinter.Checkbutton(text="밤, 기운이 난다",variable=cvalue7,command=chkBtnClick)
cbtn7.place(x=402,y=405)

textFiled=tkinter.Text()
textFiled.place(x=330,y=50,width=420,height=90)

btn=tkinter.Button(text="진단하기",font=("맑은 고딕",24),command=BtnClick)
btn.place(x=430,y=480,width=150,height=60)



root.mainloop()