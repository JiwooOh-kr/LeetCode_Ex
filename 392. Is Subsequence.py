# Answer 1
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         try:
#             idxs = [t.index(i) for i in s]
#             idxs_sort = sorted(idxs)
#             if idxs == idxs_sort:
#                 return True
#             else:
#                 return False
#         except:
#             return False
# Case : s = "aaaaaa", t = "bbaaaa" --> Failed

# Answer 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i])+1:]
            else:
                return False
        return True

'''
# Solution 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True
        subsequence = 0
        for i in range(0, len(t)):
            if subsequence <= len(s) -1:
                print(s[subsequence])
                if s[subsequence] == t[i]:
                    subsequence+=1
        return subsequence == len(s) 

# Solution 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        matched = 0
        for l in t:
            if s[matched] == l:
                matched += 1
            if matched == len(s): 
                return True
        return False
'''