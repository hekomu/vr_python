import tkinter


def btn_click():    
    sale_prices = {
        "banana": 1800,
        "coffee": 1800,
        "lunchbox": 4000,
        "coke": 1500,
        "shrimp": 2000,
        "gimbop": 1400
    }
    total_sales = (
        int(sale1.get() or 0) * sale_prices["coffee"] +
        int(sale2.get() or 0) * sale_prices["gimbop"]+
        int(sale3.get() or 0) * sale_prices["banana"] +
        int(sale4.get() or 0) * sale_prices["lunchbox"] +
        int(sale5.get() or 0) * sale_prices["coke"] +
        int(sale6.get() or 0) * sale_prices["shrimp"] 
    )

    buy_prices = {
        "banana": 800,
        "coffee": 500,
        "lunchbox": 3500,
        "coke": 700,
        "shrimp": 1000,
        "gimbop": 900
    }

    total_buy = (
        int(buy1.get() or 0) *  buy_prices["coffee"] +
        int(buy2.get() or 0) *  buy_prices["gimbop"]+
        int(buy3.get() or 0) * buy_prices["banana"] +
        int(buy4.get() or 0) *  buy_prices["lunchbox"] +
        int(buy5.get() or 0) *  buy_prices["coke"] +
        int(buy6.get() or 0) *  buy_prices["shrimp"] 
        
    )


    str1="오늘의 총 매출액은"+str(total_sales-total_buy)+"원 입니다."
    labelRes1=tkinter.Label(root,text=str1,font=("맑은고딕",10))
    labelRes1.place(x=78,y=230)

root=tkinter.Tk()
root.title("CU")
root.geometry("650x300")


label1=tkinter.Label(root, text="판매 수량", font=("맑은고딕",9))
label2=tkinter.Label(root, text="구매 수량", font=("맑은고딕",9))

banana=tkinter.Label(root, text="바나나 우유", font=("맑은고딕",9))
coffee=tkinter.Label(root, text="캔 커피", font=("맑은고딕",9))
lunchbox=tkinter.Label(root, text="도시락", font=("맑은고딕",9))
coke=tkinter.Label(root, text="콜라", font=("맑은고딕",9))
shrimp=tkinter.Label(root, text="새우깡", font=("맑은고딕",9))
gimbop=tkinter.Label(root, text="삼각김밥", font=("맑은고딕",9))

btn=tkinter.Button(root, text="계산",font=("맑은 고딕",10),command=btn_click)

sale1= tkinter.Entry(width=5)
sale2= tkinter.Entry(width=5)
sale3= tkinter.Entry(width=5)
sale4= tkinter.Entry(width=5)
sale5= tkinter.Entry(width=5)
sale6= tkinter.Entry(width=5)

buy1= tkinter.Entry(width=5)
buy2= tkinter.Entry(width=5)
buy3= tkinter.Entry(width=5)
buy4= tkinter.Entry(width=5)
buy5= tkinter.Entry(width=5)
buy6= tkinter.Entry(width=5)

#배치 
buy1.place(x=102,y=130)
buy2.place(x=197,y=130)
buy3.place(x=295,y=130)
buy4.place(x=392,y=130)
buy5.place(x=475,y=130)
buy6.place(x=563,y=130)


sale1.place(x=102,y=80)
sale2.place(x=197,y=80)
sale3.place(x=295,y=80)
sale4.place(x=392,y=80)
sale5.place(x=475,y=80)
sale6.place(x=563,y=80)

btn.place(x=80, y=180, width=530, height=25)

label1.place(x=15,y=80)
label2.place(x=15,y=130)

coffee.place(x=100,y=35)
gimbop.place(x=190,y=35)
banana.place(x=280,y=35)
lunchbox.place(x=390,y=35)
coke.place(x=480,y=35)
shrimp.place(x=560,y=35)



root.mainloop()
