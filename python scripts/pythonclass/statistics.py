# Using oop Concept find the mean, mode, median and the range of the following
# numbers[8, 5, 7, 9, 5, 1, 5]

class Statistics:
    def __init__(self, rec):
        self.sample = [float(x) for x in rec]

    def my_mean(self):
        return sum(self.sample) / len(self.sample)

    def my_range(self):
        return max(self.sample) - min(self.sample)

    def my_median(self):
         lensample = len(sorted(self.sample))
         items_sample = sorted(self.sample)
         if (lensample % 2 == 0):
             indexOne = lensample/2
             indexTwo = indexOne - 1

             firstVal = items_sample[int(indexOne)]
             secondVal = items_sample[int(indexTwo)]

             ans = firstVal + secondVal
             return ans/2

         else:
            middleIndex = lensample//2
            middle_no = items_sample[middleIndex]
            return middle_no

    def my_mode(self):
        dict_vals = {}
        for i in self.sample:
            if (i not in dict_vals):
                dict_vals.update({i:self.sample.count(i)})
        max_value = max(dict_vals.values())

        for key,value in dict_vals.items():
            if(value == max_value):
                return key

             

   
statObj = Statistics([8, 5, 7, 9, 5, 1, 5, 11, 20, 20, 20, 20, 20, 30, 46])
print("Mean", statObj.my_mean(),"\n")
print("Median", statObj.my_median(),"\n")
print("Mode", statObj.my_mode(),"\n")
print("Range", statObj.my_range(),"\n")

          

