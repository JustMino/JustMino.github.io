import random

X = 0
O = 0
Trial = 0
Accuracy = 0
Chances = 50
Count = 1


#defining the function of choosing either heads or tails
def Coinflip():
    global CoinSide
    CoinSide = random.randint(-1,1)
    while CoinSide == 0:
       CoinSide = random.randint(-1,1)
    return CoinSide

def Predict():
    global CFPre
    global chance
    chance = random.randrange(1,100)
    if chance > Chances:
        CFPre = 1
    if chance <= Chances:
        CFPre = -1
    return CFPre

def Chancechange():
    global Count
    global multi
    global Chances
    if Count >= 1:
        if CoinSide == 1:
            Count = Count + 1
        else:
            Count = -1
            Chances = 50
    elif Count <= -1:
        if CoinSide == -1:
            Count = Count - 1
        else:
            Count = 1
            Chances = 50
    if Count <= -1:
        multi = 1
    elif Count >= 1:
        multi = -1
    Chances = Chances + (Count + multi) * 0.1
    return Count

#repeats the coinflip and prediction 10k times
for i in range(10000):
    Coinflip()
    Predict()
    if CFPre == CoinSide: #This checks if the coinflip and the prediction is the same and adds to either right or wrong.
        O = O + 1
    else:
        X = X + 1
    Trial = Trial + 1
    Chancechange()

#This makes the accuracy into a decimal so we can see the percentage.
Accuracy = O / Trial
#Prints the Results.
print(O, "was right")
print(X, "was wrong")
print("Accuracy was" , Accuracy*100,"%")
