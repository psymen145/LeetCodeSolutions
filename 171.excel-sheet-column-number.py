class Solution:
    def titleToNumber(self, s: str) -> int:
        # notice a pattern
        # first place is 26 ^ 0
        # second place is 26 ^ 1
        # third place is 26 ^ 2
        
        # using A = 1 ... Z = 26 (call this x)
        # at each digits place (i)
        # generate a "value" at each place and we will call that v = ( 26 ^ i)
        # then iterate each digit value and perform v * x
        # sum up products
        
        # instead of generating a dictionary of all values (x) for the letters
        s = s[::-1]
        
        res = 0
        
        for i in range(len(s)):
            x = ord(s[i]) - ord("A") + 1
            v = 26 ** i
            
            res += v * x
            
        return res