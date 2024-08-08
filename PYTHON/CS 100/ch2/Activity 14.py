# Activity 14
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 10/20/2022

#TASK A

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "I love apples, apple are my favorite fruit"
for ch in "aplfzo":
    appears = txt.count(ch)
    print(ch,appears)
    
def countChar(ch,txt):
    count=0
    for letter in txt:
        if letter==ch:
            count=count+1
    return count

ch="m"
print(countChar(ch,txt))
# 
# #TASK B
# 
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "We kicked the ball"
x = txt.replace("a", "e")
print(x)

# txt="BEAD"
# txt=txt.replace("B", "R")
# print(txt)
# txt=txt.replace("E", "O")
# print(txt)
# txt=txt.replace("D", "M")
# print(txt)
# txt=txt.replace("R", "F")
# print(txt)
# txt=txt.replace("M", "L")
# print(txt)
# txt=txt.replace("A", "O")
# print(txt)
# 
def replaceChar(ch1,ch2,text):
    newtext=" "
    for letter in text:
        if letter==ch1:
            newtext=newtext+ch2
        else:
            newtext=newtext+letter
    return newtext
ch1="o"
ch2="#"
text="Wooster"
print(replaceChar(ch1,ch2,text))
# 
# #TASK C
# 
def replaceChar(ch1,ch2,text):
    newtext=" "
    for letter in text:
        if letter==ch1:
            newtext=newtext+ch2

        else:
            newtext=newtext+letter
    return newtext
ch1="d"
ch2="!"
text="ladder"
print("changing d (", ord(ch1), ") to ! (", ord(ch2), ")" )
print(replaceChar(ch1,ch2,text))


