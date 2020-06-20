import heapq

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        ## NON HEAP SOLUTION
        
        # get the number of times each number appears
        # use hashtbl
        
        ndict = {}
        fdict = {}
        
        for i in nums:
            if i not in ndict:
                ndict[i] = 1
            else:
                ndict[i] += 1
                
        # map the frequencies to the ndict key
        
        for key, value in ndict.items():
            if value not in fdict:
                fdict[value] = [key]
            else:
                fdict[value].append(key)
            
        # starting from the max # of elements down to 0, created a "key" list that is basically
        # sorted from highest frequency to lowest frequency
        
        slist = []
        for i in range(len(nums), 0, -1):
            if i in fdict:
                slist += fdict[i]
                
        # finally return the result
        return [slist[i] for i in range(k)]
        
        """
        
        ndict = {}
        f_lst = []
        
        for i in nums:
            if i not in ndict:
                ndict[i] = 1
            else:
                ndict[i] += 1
                
        for key, val in ndict.items():
            f_lst.append((-val, key))
            
        heapq.heapify(f_lst)
        
        ret_lst = []
        for i in range(0,k):
            ret_lst.append(heapq.heappop(f_lst)[1])
            
        return ret_lst