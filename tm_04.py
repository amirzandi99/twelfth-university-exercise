def selectionSort(number):
    n = len(number)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            if(number[j] < number[minIndex]):
                minIndex = j
        (number[i], number[minIndex]) = (number[minIndex], number[i])
    return number
# 
# 
def printArray(number):
    print("array : ", end='')
    for i in range(len(number)):
        print(number[i], end=' ')
    print("\n")