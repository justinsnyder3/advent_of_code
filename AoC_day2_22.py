inputPath="AoC_day2_22_input.txt"
d = {'rock':'scissors','paper':'rock','scissors':'paper'}
con={'A':'rock','X':'rock','B':'paper','Y':'paper','C':'scissors','Z':'scissors'}
score=0
with open(inputPath, "r") as encodedStrategyGuide:
    inputString=encodedStrategyGuide.read()
    roundValues=inputString.split("\n")
    
for round in roundValues:
    opponentInput, userInput=round.split(" ")
    opponetChoice=con[opponentInput]
    userChoice=con[userInput]
    if d[opponetChoice]==userChoice:
        pass
    elif d[userChoice]==opponetChoice:
        score+=6
    else:
        score+=3
    if userInput=='X':
        score+=1
    elif userInput=="Y":
        score+=2
    else:
        score+=3
    
print(score)