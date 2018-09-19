tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(listName):
    colWidths = [0] * len(listName)
    colWidthsResult = 0
    for k in range(listName):
        for i in range(listName[k]):
            if len(colWidths[k]) < len(listName[k][i]):
                colWidths[k] = listName[k][i]

    for j in range(colWidths):
        if len(colWidthsResult) < len(colWidths[j]):
            colWidthsResult = len(colWidths[j]
            return colWidthsResult

for i in range(tableData):
  for j in range(len(tableData[i])):
    print(tableData[j][i])


#===========================================

#!/usr/bin/python3
# you can think of x and y as coordinates

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    # create a new list of 3 "0" values: one for each list in tableData
    colWidths = [0] * len(table)
    # search for the longest string in each list of tableData
    # and put the numbers of characters in the new list
    for y in range(len(table)):
        for x in table[y]:
            if colWidths[y] < len(x):
                colWidths[y] = len(x)

    # "rotate" and print the list of lists
    for x in range(len(table[0])) :
        for y in range(len(table)) :
            print(table[y][x].rjust(colWidths[y]), end = ' ')
        print()
        x += 1

printTable(tableData)
