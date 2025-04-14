
"""
for i in range(50,101,3):    
    print(i,end=" ")



N=5
res=1
for i in range (1,N+1,1):
    res*=i

print(res)

n=2000
m=0

for i in range(1000,n+1,1):
    if i%2!=0:
        
        m+=i
        print(m)


for i in range(2,10,1):
    print("\n")
    for k in range(1,10,1):
        print(i,"*",k,"=",i*k)


i=0
while (i<3):
    print(i)
    i+=1


while True:
    print("ㅎ",end="")

while True:
    num1=int(input("숫자1 ==> "))
   
    if num1==0:
        print("0을 입력해서 계산을 종료합니다.")
        break
   
   
    num2=int(input("숫자2 ==> "))
    print(num1,"+",num2,"=",num1+num2)
    

"""
 #1부터 100까지 더하되 ,34의 배수는 더하지 않음

res=0
for i in range (1,101,1):
    if i%4==0:
        continue
    elif i%3==0:
        continue
    res+=i
print(res)