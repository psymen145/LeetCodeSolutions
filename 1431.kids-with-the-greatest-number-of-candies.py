class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # just add all the candies for the current kid...
        # if not bigger than the previous greatest...
        # then false
        
        greatest_num_candies = max(candies)
        ret = []
        
        for kid in candies:
            if kid + extraCandies >= greatest_num_candies:
                ret.append(True)
            else:
                ret.append(False)
                
        return ret