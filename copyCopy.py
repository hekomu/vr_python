inFile = open("test.txt","r",encoding="UTF-8")
outFile=open("outTest.txt","w",encoding="UTF-8")

while True:
    strFile=inFile.readline()
    strFileChange=""
    for ch in strFile:
        chNum=ord(ch)
        chNum=chNum -100
        chChange=chr(chNum)
        strFileChange+=chChange
    if(strFile==""):
        break
    print(strFileChange,end="")
    
    outFile.writelines(strFile)

inFile.close()
outFile.close()