class mathCalculations:
    def __init__(self, num1, num2, num3, num4):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
        self.num4 = num4

    def getSum(self):
        return self.num1 + self.num2 + self.num3 + self.num4

    def getAverage(self):
        return self.getSum()/4

# odd numbers and sum of odd numbers
    def getOdd(self):
        oddNum = self.num1, self.num2, self.num3, self.num4
        numbers = list(oddNum)
        sumNum = 0
        oddnums = []
        for i in numbers:
          if i % 2 != 0 :
            sumNum += i
            oddnums.append(i)
        print("The odd number(s) are:", oddnums)
        print("The sum of odd numbers is:", sumNum)


        # second method
    

    #  multiply by 2
    def multiply(self):
        ans = []
        multi = self.num1, self.num2, self.num3, self.num4
        multiplyList = list(multi)
        for x in multiplyList:
            y = x * 2
            ans.append(y)
        print("The input multiply by 2:", ans)      
  


