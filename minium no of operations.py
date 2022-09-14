class Solution:
   def solve(self, s, t):
      k, n = len(t), len(s)
      ans = 10**10
      for i in range(n - k + 1):
         ss = s[i:i+k]
         ans = min(ans, sum(ss[j]!=t[j] for j in range(k)))
      return ans
ob = Solution()
print(ob.solve(input("s1:"), input("s2:")))
