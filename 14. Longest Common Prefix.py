class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret = ""

        for i in range(200):
            tmp = []
            try:
                for s in strs:
                    tmp.append(s[i])

                if all(i == tmp[0] for i in tmp):
                    ret += tmp[0]
                else:
                    break
            except:
                break

        return ret

'''
# Solution 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        prefix = ""
        for i in l:
            if len(set(i))==1:
                prefix += i[0]
            else:
                break
        return prefix

# Solution 2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre     

# Solution 3
class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        if not S: return ''
        m, M, i = min(S), max(S), 0
        for i in range(min(len(m),len(M))):
            if m[i] != M[i]: break
        else: i += 1
        return m[:i]
'''