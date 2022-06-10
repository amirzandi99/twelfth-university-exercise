class high_precision_t:
    def __init__(self, num):
        self.digits = []
        self.sign = 0
        self.decpt = -1
        for i in range(len(num)):
            if(num[0] == '-'):
                self.sign = -1
            elif(num[i] == '.'):
                self.decpt = i
            else:
                self.digits.append(int(num[i]))
    def print_high(self):
        if(self.sign < 0):
            print("-", end='')
        for i in range(len(self.digits)):
            if(self.decpt == i):
                print(".", end='')
            print(self.digits[i], end='')
        print()
    def __print(self, pNum1, pNum2, pNum3, Len, opt):
        print("\n")
        print("   ", end='')
        for i in range(Len):
            print(pNum1[i], end='')
        print()
        print(f"{opt}  ", end='')
        for i in range(Len):
            print(pNum2[i], end='')
        print()
        print("   ", end='')
        for i in range(Len):
            print("-", end='')
        print()
        if(len(pNum3) == len(pNum2)):
            print("   ", end='')
        else:
            print("  ", end='')
        n = len(pNum3)
        for i in range(n):
            print(pNum3[n-i-1], end='')
        print()
    def __placement(self, n1, n2):
        Num1, Num2, pNum1, pNum2 = [], [], [], []
        Len1 = len(n1)
        Len2 = len(n2)
        if(Len1 > Len2):
            x = Len1 - Len2
            for i in range(x):
                Num2.append(0)
            for i in range(Len2):
                Num2.append(n2[i])
            for i in range(Len1):
                Num1.append(n1[i])
            Len = Len1
        elif(Len1 < Len2):
            x = Len2 - Len1
            for i in range(x):
                Num1.append(0)
            for i in range(Len1):
                Num1.append(n1[i])
            for i in range(Len2):
                Num2.append(n2[i])
            Len = Len2
        else:
            for i in range(Len1):
                Num1.append(n1[i])
            for i in range(Len2):
                Num2.append(n2[i])
            Len = Len1
        # 
        n = len(Num1)
        for i in range(n):
            pNum1.append(Num1[i])
            pNum2.append(Num2[i])
        for i in range(n//2):
            Num1[i], Num1[n-i-1] = Num1[n-i-1], Num1[i]
            Num2[i], Num2[n-i-1] = Num2[n-i-1], Num2[i]
        # 
        return Num1, Num2, pNum1, pNum2, Len
    def add_high(self,other):
        Add = []
        n1, n2 = [], []
        for i in range(len(self.digits)):
            n1.append(self.digits[i])
        for i in range(len(other.digits)):
            n2.append(other.digits[i])
        Num1,Num2,pNum1,pNum2,Len = self.__placement(n1, n2)
        # 
        for i in range(Len):
            add = Num1[i] + Num2[i]
            if(add > 9):
                if(i < Len-2):
                    Num1[i+1] += 1
                    add -= 10
                    Add.append(add)
                else:
                    add -= 10
                    Add.append(add)
                    Add.append(1)
            else:
                Add.append(add)
        # 
        self.__print(pNum1, pNum2, Add, Len, "+")