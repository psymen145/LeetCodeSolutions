class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        i = 0
        while True:
            if 2 ** i > n:
                return False
            elif 2 ** i == n:
                return True
            
            i += 1