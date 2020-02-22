class Solution:
    def isPalindrome(self, s: str) -> bool:
        # ideally we would just reverse the string to see if it's equal
        # however, since we are ignoring cases, and spaces...
        
        s = s.lower()
        stripped = ''
        
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                stripped += s[i]
                
        return stripped[::-1] == stripped