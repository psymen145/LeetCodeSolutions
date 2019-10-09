#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[': 
                my_stack.append(i)
            elif i == ')':
                if my_stack and '(' == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            elif i == '}':
                if my_stack and '{' == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
            elif i == ']':
                if my_stack and '[' == my_stack[-1]:
                    my_stack.pop()
                else:
                    return False
        
        if len(my_stack) != 0:
            return False
        else:
            return True
# @lc code=end

