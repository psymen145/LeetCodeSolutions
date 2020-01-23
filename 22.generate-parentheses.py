class Solution(object):
    def __init__(self):
        self.well_formed_list = []
    
    def createSolution(self, s, left, right, n):
        if left == n and right == n:
            self.well_formed_list.append(s)
            return
        
        if left < n:
            self.createSolution(s+'(',left+1,right,n) #1
        if right < left:
            self.createSolution(s+')',left,right+1,n)
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.createSolution('', 0, 0, n)
        
        return self.well_formed_list
        