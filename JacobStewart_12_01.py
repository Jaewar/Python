# Jacob L Stewart
# Chapter 12 Assignment 01
# Modify the selection sort algorithm to sort a list of integers in descending order.

def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp
    return values


def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] > values[minPos]:
            minPos = i
    return minPos


def main():
    myList = [1, 5, 23, 0, 13, 54, 32, 12, 0]
    sortList = selectionSort(myList)
    print(sortList)


main()
