num = [16, 18, 27, 16, 23, 21, 19]
no = len(num)
summ = sum(num)
mean = summ / no
print("The mean or average of all these numbers (", num, ") is", str(mean))
num.sort()
if no % 2 == 0:
    median1 = num[no//2]
    median2 = num[no//2 - 1]
    median = (median1 + median2)/2
else:
    median = num[no//2]
print("The median of the given numbers  (", num, ") is", str(median))
from collections import Counter
val = Counter(num)
findMode = dict(val)
mode = [i for i, v in findMode.items() if v == max(list(val.values()))]
if len(mode) == no:
    findMode = "The group of number do not have any mode"
else:
    findMode = "The mode of a number is / are: " + ', '.join(map(str, mode))
print(findMode)
