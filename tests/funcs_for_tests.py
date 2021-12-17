import sys

def minOfList(list):
    min = list[0]
    for i in range(len(list)):
        if list[i] < min:
            min = list[i]
    return min

def maxOfList(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

def sumOfList(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def prodOfList(list):
    prod = 1
    for item in list:
        prod *= item
    return prod

def fileReading(file):
    try:
        with open(file, "r") as numbers:
            numbersList = numbers.read()
    except FileNotFoundError:
        print("Файл с таким названием не найден")
        sys.exit(1)
    else:
        numbersListConverted = numbersList.split(',')
        for item in range(len(numbersListConverted)):
            numbersListConverted[item] = int(numbersListConverted[item])
        minimalNumber = minOfList(numbersListConverted)
        maximalNumber = maxOfList(numbersListConverted)
        sumOfNumbers = sumOfList(numbersListConverted)
        try:
            prodOfList(numbersListConverted)
        except ArithmeticError:
            print("В указанном файле содержится слишком много чисел")
            sys.exit(1)
        else:
            prodOfNumbers = prodOfList(numbersListConverted)
        return minimalNumber, maximalNumber, sumOfNumbers, prodOfNumbers