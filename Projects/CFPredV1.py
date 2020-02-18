import random.randint

X = 0 #X is the amount of wrong guesses
O = 0 #O is for amount of right guesses
Trial = 0
Accuracy = 0
def Coinflip(): #defining the function of choosing either heads or tails
    global CoinSide
    CoinSide = random.randint(-1,1)
    while CoinSide == 0 :
       CoinSide = random.randint(-1,1)
    return CoinSide

def Predict(): #This does the same thing as the coinflip but the outcome of this will be used to see the accuracy of the coinflip itself
    global CFPre
    CFPre = random.randint(-1, 1)
    while CFPre == 0:
        CFPre = random.randint(-1, 1)
    return CFPre

for i in range(10000): #repeats the coinflip and prediction 10k times
    Coinflip()
    Predict()
    if CFPre == CoinSide: #This checks if the coinflip and the prediction is the same and adds to either right or wrong.
        O = O + 1
    else:
        X = X + 1
    Trial = Trial + 1

Accuracy = O / Trial #This makes the accuracy into a decimal so we can see the percentage.
print(O, "was right")
print(X, "was wrong")
print("Accuracy was" , Accuracy*100,"%")
