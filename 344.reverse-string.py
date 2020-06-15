class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        p1 = 0
        p2 = len(s)-1
        
        while p1 < p2:
            tmp = s[p1]
            s[p1] = s[p2]
            s[p2] = tmp
            p1 += 1
            p2 -= 1
        