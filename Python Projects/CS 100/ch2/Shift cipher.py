# char='e'
# 
# code=chr(ord(char) +1)
# print(char+" " +code)

plaintext="python"
codedText=""

for ch in plaintext:
    code=chr(ord(ch) +1)
    print(ch+" " +code)
    codedText=codedText+code
print(codedText)

resultText=""
for ch in codedText:
    code=chr(ord(ch) -1)
    print(ch+" " +code)
    resultText=resultText+code
print(resultText)
# 
# 
# def getAlphaPos(ch):
#     pos=ord(ch)-ord('a')
#     return pos
# for ch in "abcdefghijklmnopqrstuvwxyz":
#     print(ch, end=" ")
#     print(ord(ch), end=" ")
#     print(getAlphaPos(ch), end=" ")
#     newPos=(getAlphaPos(ch)+1) %26 
#     print(newPos, end=" ")
#     newCh=chr(newPos+ord('a'))
#     print(newCh)
#     
# #     
# def getShiftChar(ch, shift):
#     if ch==' ':
#         return ' '
#     newPos=(getAlphaPos(ch)+shift) %26
#     return chr(newPos+ord('a'))
#     
plaintext="zamboni"
codedText=" "
def getAlphaPos(ch):
    pos=ord(ch)-ord('a')
    return pos
for ch in "abcdefghijklmnopqrstuvwxyz":
    print(ch, end=" ")
    print(ord(ch), end=" ")
    print(getAlphaPos(ch), end=" ")
    newPos=(getAlphaPos(ch)+1) %26 
    print(newPos, end=" ")
    newCh=chr(newPos+ord('a'))
    print(newCh)
for ch in plaintext:
    code=chr(ord(ch) +1)
    print(ch+" " +code)
    codedText=codedText+code
print(codedText)

resultText=""
for ch in codedText:
    code=chr(ord(ch) -1)
    print(ch+" " +code)
    resultText=resultText+code
print(resultText)
