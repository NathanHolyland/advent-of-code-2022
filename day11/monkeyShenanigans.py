from __future__ import annotations
from math import floor
import re

# a turn is, inspect active item. Throw it to a monkey deterimed by its test, then move on to the next item

# every 6 lines is a monkey, 1 line whitespace between monkeys

#syntactical form of starting items
# every occurence of [0-9]+ on line 1

#syntactical forms of operations (regex) on line (starting from 0) 2
# value is always the only occurence of [0-9]+

# * if contains (* [0-9]+)
# / if contains (/ [0-9]+)
# + if contains (+ [0-9]+)
# - if contains (- [0-9]+)
# SPECIAL CASE: **2 if contains (old * old) (Hence operator=** and value=2)

#syntactical form of test (regex) on line 3-5
# testDivisor = [0-9]+ on line 3
# TRUE monkey index = [0-9]+ on line 4
# FALSE monkey index = [0-9]+ on line 5

MonkeyList = []

class Monkey:
    def __init__(self, startingItems, operation, test, throwTo):
        self.items = startingItems # each item is just a worry level (float)
        self.operation = operation # [operator, number]
        self.test = test # int (has to be divisible by this integer for index0 of throwTo, otherwise index1)
        self.throwTo = throwTo # [TrueMonkey, FalseMonkey]

        self.inspectionTotal = 0
    
    def receiveItem(self, item):
        self.items.append(item)

    def throwItem(self, monkey, item):
        MonkeyList[monkey].receiveItem(item)
        #print(f"{MonkeyList.index(self)} threw to {monkey}")

    def inspectActiveItem(self, item, multiple):
        operator = self.operation[0]
        value = self.operation[1]
        self.inspectionTotal += 1
        if operator == "*":
            item = item * value
        elif operator == "+":
            item = item + value
        elif operator == "-":
            item = item - value
        elif operator == "/":
            item = item / value
        elif operator == "**":
            item = item*item
        
        item = item%multiple # restrict value without reducing divisibility
        if item%self.test == 0:
            self.throwItem(self.throwTo[0], item)
        else:
            self.throwItem(self.throwTo[1], item)
        self.items = []
    
    def performTurn(self, multiple):
        for item in self.items:
            self.inspectActiveItem(item, multiple)
    
    def __repr__(self):
        return (f"Monkey {MonkeyList.index(self)}\n  items: {self.items}\n  Operation: new = old {self.operation[0]} {self.operation[1]}\n  Test: % {self.test}\n    true: Monkey {self.throwTo[0]}\n    false: Monkey {self.throwTo[1]}\n\n")

def constructMonkeys(lines):
    multiple = 1
    for i in range(len(lines)):
        line_index = i%7
        line = lines[i]
        if line_index == 0:
            items = []
            operation = []
            testDivisor = None
            throwTo = []

        elif line_index == 1: # item line
            strItems = re.findall("[0-9]+", line)
            items = [int(i) for i in strItems]
        elif line_index == 2: # operation line
            strListVal = re.findall("[0-9]+", line)
            if len(strListVal) != 0:
                value = int(strListVal[0])
            if re.search("\*\ [0-9]+", line):
                operation = ["*", value]
            elif re.search("\+\ [0-9]+", line):
                operation = ["+", value]
            else:
                operation = ["**", 2]
        elif line_index == 3:
            testDivisor = int(re.search("[0-9]+", line)[0])
            multiple *= testDivisor
        elif line_index == 4 or line_index == 5:
            throwTo.append(int(re.search("[0-9]+", line)[0]))
            if i == len(lines)-1:
                MonkeyList.append(Monkey(items, operation, testDivisor, throwTo))
        if line_index == 6:
            MonkeyList.append(Monkey(items, operation, testDivisor, throwTo))
    return multiple

def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()
    multiple = constructMonkeys(lines)
    numberOfRounds = 10000
    for _ in range(numberOfRounds):
        for monkey in MonkeyList:
            #print(monkey)
            monkey.performTurn(multiple)
    for i in range(len(MonkeyList)):
        print(f"Monkey {i} had {MonkeyList[i].inspectionTotal} inspections")

if __name__ == "__main__":
    main()