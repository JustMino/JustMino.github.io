import random

X = 0
O = 0
Trial = 0
Accuracy = 0
Skipped = 0
Heads = 0
Tails = 0
x = 0

#defining the function of choosing either heads or tails
def Coinflip():
    global CoinSide
    CoinSide = random.randint(-1,1)
    while CoinSide == 0:
       CoinSide = random.randint(-1,1)
    return CoinSide

def Predict():
    global CFPre
    if Heads != 0:
        if Tails !=0:

            if Heads/Tails >= 1.5:
                CFPre = 1
            elif Tails/Heads >= 1.5:
                CFPre = -1
            else:
                CFPre = 0
        else:
            CFPre = 0
    else:
        CFPre = 0



for i in range(10000):
    Coinflip()
    Predict()
    if CoinSide == -1:
        Heads = Heads + 1
    elif CoinSide == 1:
        Tails = Tails + 1
    if CFPre != 0:
        if CFPre == CoinSide: #This checks if the coinflip and the prediction is the same and adds to either right or wrong.
            O = O + 1
        else:
            X = X + 1
        Trial = Trial + 1


#This makes the accuracy into a decimal so we can see the percentage.
Accuracy = O / Trial
#Prints the Results.
print(O, "was right")
print(X, "was wrong")
print("Accuracy was" , Accuracy*100,"%")
