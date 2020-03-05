class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string in the list...
        # count how many charactesr of each string there are ( store in hash table )
        # after we count the entire string, and it doesn't match and existing hash tables
        # ... create new hash table
        
        anas = {}
        for string in strs:
            s = ''.join(sorted(string))
            if s in anas:
                anas[s].append(string)
            else:
                anas[s] = [string]
        return [ anas[x] for x in anas ]
        
        