#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.82%)
# Likes:    4227
# Dislikes: 394
# Total Accepted:    641.8K
# Total Submissions: 2.3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # cases:
        # 1. longest palindrome starts in the first character
        #       solution: every iteration, we reverse string and see if it matches.
        # 2. palindrome starts in a random part of the string
        #       solution: 
        # 3. palindrome starts in the beginning but a longer one later on

        '''
        if len(s) < 1:
            return ""
        elif len(s) == 1:
            return s

        longest_palindrome = ''
        longest_palin_len = 0

        for i in range(0, len(s)):
            for j in range(i, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    if longest_palin_len < len(s[i:j]):
                        longest_palindrome = s[i:j]
                        longest_palin_len = len(s[i:j])

        return longest_palindrome
        '''

        #   S   A   M   A   S
        # S 1   0   0   0   1
        # A 0   1   0   1   0
        # M 0   0   1   0   0
        # A 0   0   0   1   0
        # S 0   0   0   0   1

        len_s = len(s)

        tbl = [[0 for i in range(len_s)] for j in range(len_s)]

        # fill in certain fields that we know are palindromes
        # length 1
        max_len = 1
        i = 0
        while i < len_s:
            tbl[i][i] = True
            i += 1

        # find 2 length palindromes
        start = 0
        i = 0
        while i < len_s - 1:
            if s[i] == s[i+1]:
                tbl[i][i+1] = True
                start = i
                max_len = 2

            i += 1

        k = 3
        while k <= len_s:
            i = 0
            while i < (len_s - k + 1):
                j = (i + k - 1)

                if tbl[i+1][j-1] and s[i] == s[j]:
                    tbl[i][j] = True
                    if k > max_len:
                        start = i
                        max_len = k

                i += 1

            k += 1

        return s[start:start+max_len]



