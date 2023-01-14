class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        in_s = []
        in_t = []

        for i in range(len(s)):
            if not s[i] in in_s:
                in_s.append(s[i])
            if not t[i] in in_t:
                in_t.append(t[i])

        idx_s = []
        idx_t = []

        for i in range(len(s)):
            idx_s.append(in_s.index(s[i]))
            idx_t.append(in_t.index(t[i]))

        return idx_s == idx_t

'''
# Solution 1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(set(t)) == len(set(s)) and len({(a,b) for a,b in zip(s,t)}) == len(set(s))):
            return True
        return False

# Solution 2
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]

# Solution 3
class Solution(object):
    def isIsomorphic(self, s, t):
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        if map1 == map2:
            return True
        return False
'''