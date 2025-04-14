import random

dice1=0
dice2=0
dice3=0
cnt=0


while True:
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice3=random.randint(1,6)

    print(dice1,dice2,dice3)
    cnt +=1
    if dice1==dice2 and dice1==dice3:
            print("3개 주사위는 모두 ",dice1,"입니다.")
            print("같은 숫자가 나오기까지",cnt,"번 던졌습니다")

            break