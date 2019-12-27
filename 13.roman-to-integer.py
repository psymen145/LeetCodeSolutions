class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_hash = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        sum = 0
        skip_next = False
        
        for i in range(len(s)):
            if skip_next:
                skip_next = False
                continue
            
            if s[i] == 'I' and (i+1) < len(s) and s[i+1] == 'V':
                sum += 4
                skip_next = True   
            elif s[i] == 'I' and (i+1) < len(s) and s[i+1] == 'X':
                sum += 9
                skip_next = True
            elif s[i] == 'X' and (i+1) < len(s) and s[i+1] == 'L':
                sum += 40
                skip_next = True
            elif s[i] == 'X' and (i+1) < len(s) and s[i+1] == 'C':
                sum += 90
                skip_next = True
            elif s[i] == 'C' and (i+1) < len(s) and s[i+1] == 'D':
                sum += 400
                skip_next = True
            elif s[i] == 'C' and (i+1) < len(s) and s[i+1] == 'M':
                sum += 900
                skip_next = True 
                    
            elif s[i] in symbol_hash:
                sum += symbol_hash[s[i]]
                
        return sum
                
            