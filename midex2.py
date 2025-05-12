
"""
name=input("원본 문자열==>")
n=len(name) #반복문 문자열
print("반대 문자열==>",name[3]+name[2]+name[1]+name[0])
"""

name = input("원본 문자열==> ")
n = len(name)
result = ""
for i in range(n-1, -1, -1):  # 뒤에서부터 앞으로 반복
    result += name[i]
print("반대 문자열==>", result)