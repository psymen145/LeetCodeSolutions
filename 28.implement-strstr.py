class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        
        if len_needle == 0:
            return 0
        
        for i in range(len(haystack)):
            # check if it is even possible the needle is in the haystack by comparing lens
            if needle[0] == haystack[i]:
                if len_needle + i <= len(haystack):
                    for j in range(len_needle):
                        if haystack[i + j] == needle[j]:
                            if j == len_needle - 1:
                                return i
                            else:
                                continue
                        else:
                            break
                else:
                    return -1
                
        return -1