# Python3 code for Max
# Water Container

def maxArea(A, Len) :

    area = 0

    for i in range(Len) :

        for j in range(i + 1, Len) :

           

            # Calculating the max area

            area = max(area, min(A[j], A[i]) * (j - i))

    return area
 
# Driver code

a = [ 1, 5, 4, 3 ]

b = [ 3, 1, 2, 4, 5 ]

c = [1,8,6,2,5,4,8,3,7]

d = [1,1]

e = [7,3]
 

len1 = len(a)

print(maxArea(a, len1))
 

len2 = len(b)

print(maxArea(b, len2))

len3 = len(c)

print(maxArea(c, len3))

len4 = len(d)

print(maxArea(d, len4))

len5 = len(e)

print(maxArea(e, len5))

 
