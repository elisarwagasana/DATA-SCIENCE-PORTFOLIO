# Activity 8
#
#Author: Elisa Rwagasana Ishimwe  2 (11AM)
#
#Date: 9/13/2022

#2.
def sumAlternatingFractions(numTerms):
    # initialize summation to be 0 the additive identity
    sum = 0
    # start the denominator at 1
    denominator = 1
    # start the sign as positive
    sign = 1
    
    #repeat until the specified number of terms have
    # been summed
    for iter in range(numTerms):
        # compute the denominator value
        fraction = 1 / denominator
        # multiply it by the sign and sum
        sum = sum + (sign*fraction)
        # flip the sign to the alternate
        sign = sign * -1
        # compute new denominator by adding 1 to it
        denominator = denominator + 1 
        print("    ", sum)
    return sum


# steps = 10
# steps=50
# steps=100
# steps=250
# steps=500
# steps=1000
# steps=2000
# print("    ", sumAlternatingFractions(steps))
# print("The natural log of 2: ", 0.69314718056)

#3.

# This function computes the sums of the inverse of a base
# raised to successively higher powers
#
# sum = 1/1 + 1/n + 1/n**2 + 1/n**3 + 1/n**4 + ...
#
# This is a converging series that results in n/(n-1)

def sumInversePowers(numTerms, n):
    # initialize summation to be 0 the additive identity
    sum = 0
    #Start the denominator at 1 
    denominator = 1
    #repeat until the specified number of terms in the brackets have been summed 
    for iter in range(numTerms):
        #Compute the value of the denominator
        fraction = 1 / denominator
        #Add up the previous sum and the fraction we have
        sum = sum + fraction
        #compute the new denominator by multiplying it by the previous denominator without the power 
        denominator = denominator * n 
        print("    ", sum)
    return sum
# 
# steps = 10
# base = 3
# steps=12
# base=4
# steps=15
# base=5
# steps=17
# base=6
# steps=20
# base=7
# steps=25
# base=8
# steps=27
# base=9
# steps=30
# base=10
# print("    ", sumInversePowers(steps,base))
# print(">>> ", base/(base-1))


#5.

#Leibniz formula states that π/4=1/1−1/3+1/5−1/7+1/9−⋯
def leibniz(terms):
    sum=0
    denominator=1
    sign=1
    for inter in range(terms):
        fraction=1/denominator
        sum=sum+(sign*fraction)
        sign=sign*-1
        denominator=denominator+2
    return sum*4

print("Results for Leibniz formula:")
print(leibniz(200))
print(leibniz(500))
# 3.136592684838816
# 3.139592655589785

#Wallis formula states that π/2=2/1×2/3×4/3×4/5×6/5×6/7×8/7×⋯
def wallis(numPairs):
    approxPi=1
    denominator=1
    n=2
    for inter in range(numPairs):
        fraction1=n/denominator
        fraction2=n/(denominator+2)
        denominator=denominator+2
        fraction=fraction1*fraction2
        approxPi=approxPi*fraction
        n=n+2
    return approxPi*2

print("Results for Wallis formula:")
print(wallis(4))
print(wallis(20))
print(wallis(100))
# 2.972154195011337
# 3.103516961539231
# 3.133787490628159

#6. Archimedes Pi Approxinamtion is better 


