inputPath="AoC_day2_22_input.txt"
d = {'rock':'scissors','paper':'rock','scissors':'paper'}
rd= {'scissors':'rock','rock':'paper','paper':'scissors'}
con={'A':'rock','X':'lose','B':'paper','Y':'tie','C':'scissors','Z':'win'}
val={'rock':1,'paper':2,'scissors':3}
score=0
with open(inputPath, "r") as encodedStrategyGuide:
    inputString=encodedStrategyGuide.read()
    rounds=inputString.split("\n")    
    
for round in rounds:
    opponentInput, roundResult=round.split(" ")
    opponetChoice=con[opponentInput]
    roundOutcome=con[roundResult]
    userChoice='tbd'
    if roundOutcome=='win':
        userChoice=rd[opponetChoice]
        score+=val[userChoice]+6
    elif roundOutcome=="tie":
        userChoice=opponetChoice
        score+=val[userChoice]+3
    else:
        userChoice=d[opponetChoice]
        score+=val[userChoice]
    
print(score)