"""
a="100"
print(type(a))
"""
var1="pYthOn"
var2="화이팅!!"
"""
var3=var1+var2
var4=var2+var1
print(var3)
print(var4)
"""


str1len=len(var1)
str2len=len(var2)
print("두 문자열의 길이 차이는"+str(str1len-str2len)+"입니다.")

var5=var1.upper()
print(var5)
var6=var1.lower()
print(var6)


var7="""
선배, 마라탕 사주세요 (그래, 가자)
선배, 혹시 탕후루도 같이? (뭐? 탕후루도?)
그럼 제가 선배 맘에
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 내 맘이 단짠단짠
탕탕, 후루후루, 탕탕탕, 후루루루루
탕탕, 후루후루, 마라탕탕탕탕, 후루루루루
"""

numThang=var7.find("마라탕")
print(numThang)

numHuru=var7.count("후루")
print(numHuru)