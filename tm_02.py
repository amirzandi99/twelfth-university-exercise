def bubbleSort(number):
    n = len(number)
    for i in range(n):
        for j in range(n):
            if(j < n-1):
                if(number[j] > number[j+1]):
                    temp = number[j]
                    number[j] = number[j+1]
                    number[j+1] = temp
    return number
# 
# 
def printArray(number):
    print("array : ", end='')
    for i in range(len(number)):
        print(number[i], end=' ')
    print("\n")