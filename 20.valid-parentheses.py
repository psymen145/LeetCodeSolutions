class Solution:
    def isValid(self, s: str) -> bool:        
        paren_dict = {'}': '{',
               ')': '(',
               ']': '['}
        
        tmp_stack = []
        
        for char in s:
            if char not in paren_dict:
                tmp_stack.append(char)
            else:
                if not tmp_stack:
                    return False
                
                if paren_dict[char] != tmp_stack.pop():
                    return False
                
            
        if not tmp_stack:
            return True
        else:
            return False
        

