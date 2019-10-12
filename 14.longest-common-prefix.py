#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        len_strs = len(strs)
        
        if len_strs == 1:
            return strs[0]
        
        longest = ""
        
        for i in range(len(strs[0])):
            counter = 0
            letter = strs[0][i]
            for word in strs:
                if len(word) > i and word[i] == letter:
                    counter += 1
                else:
                    break
            
            if counter == len_strs:
                longest += letter
            else:
                return longest
            
        return longest
# @lc code=end

