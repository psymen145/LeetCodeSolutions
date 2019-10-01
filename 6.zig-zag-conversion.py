#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (33.08%)
# Likes:    1172
# Dislikes: 3561
# Total Accepted:    355.3K
# Total Submissions: 1.1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:

    def convert(self, s: str, numRows: int) -> str:
        # numrows 2 : 0 2 4 6 8
        # numrows 3 : 0 4 8 12
        # numrows 4 : 0 6 12 18

        # trivial solution
        if numRows == 1:
            return s
        
        if s == "":
            return ""

        buckets = [[] for r in range(numRows)]

        i = 0
        lvl = 0
        while i < len(s):   
            buckets[lvl].append(s[i])

            if lvl == numRows - 1:
                decrease = True
            if lvl == 0:
                decrease = False 

            if not decrease:
                lvl += 1
            else:
                lvl -= 1


            i += 1

        ret_str = ''
        for row in buckets:
            for num in row:
                ret_str += str(num)

        return ret_str
