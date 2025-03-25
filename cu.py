import tkinter

root=tkinter.Tk()
root.title("CU")
root.geometry("650x300")


label1=tkinter.Label(root, text="판매 수량", font=("맑은고딕",9))
label2=tkinter.Label(root, text="구매 수량", font=("맑은고딕",9))
banana=tkinter.Label(root, text="바나나 우유", font=("맑은고딕",9))
coffe=tkinter.Label(root, text="캔 커피", font=("맑은고딕",9))
lunchbox=tkinter.Label(root, text="도시락", font=("맑은고딕",9))
cola=tkinter.Label(root, text="콜라", font=("맑은고딕",9))
saewoo=tkinter.Label(root, text="새우깡", font=("맑은고딕",9))
gimbop=tkinter.Label(root, text="삼각김밥", font=("맑은고딕",9))






label1.place(x=15,y=70)
label2.place(x=15,y=140)
banana.place()


root.mainloop()
