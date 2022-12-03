# A=Rock B=Paper C=Scissors
# Rock 1 Paper 2 Scissors 3
# x = lose y = draw z = win

#lose: 0 draw: 3 win: 6

rock_paper_outcomes = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7
}

def getComparisons():
    comparisons = []
    while True:
        x = input()
        if not x in rock_paper_outcomes.keys():
            break
        comparisons.append(x)
    
    scores = []
    for i in comparisons:
        scores.append(rock_paper_outcomes[i])
    return scores

def sumList(l:list):
    total = 0
    for i in l:
        total += i
    return total

print(sumList(getComparisons()))