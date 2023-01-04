class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        symbols = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        symbols_i = 'VX'
        symbols_x = 'LC'
        symbols_c = 'DM'
        for i in range(len(s)):
            try:
                if (s[i] == 'I' and s[i+1] in symbols_i) or (s[i] == 'X' and s[i+1] in symbols_x) or(s[i] == 'C' and s[i+1] in symbols_c) :
                    num -= symbols[s[i]]
                else:
                    num += symbols[s[i]]
            except:
                num += symbols[s[i]]
        return num