

text = "Encryption is the method by which information is converted into secret code that hides the information's true meaning. The science of encrypting and decrypting information is called cryptography. In computing, unencrypted data is also known as plaintext, and encrypted data is called ciphertext"
#change everything to lower case
text=text.lower() 
#Count the frequency that each letter appears
letterCount=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def getAlphaPos(ch):
    return ord(ch)-ord('a')

def countLetters(letterList):
    for letter in text:
        #if it is between lower case a and lower case z (this also removes space and periods)
        if 'a'<=letter and letter<='z':  
            idx=getAlphaPos(letter)
            letterCount[idx]+=1
        
countLetters(text)

for loc in range(len(letterCount)):
    #give me the character asociated with 97,98 etc)
    print(chr(loc+ord('a')), " " , letterCount[loc])  
    
    
        
    


    