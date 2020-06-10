class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # trivial, time limit exceeded
        """
        ret_arr = []
        for i in range(len(T)):
            count = 0
            for j in range(i+1, len(T)):
                count += 1
                if T[j] > T[i]:
                    break
            else:
                count = 0
            
            ret_arr.append(count)
            
        return ret_arr
        """
        # 74 75 72 77
        # 1 2 1 0
        
        
        ans = [0] * len(T)
        stk = []
        
        for i, t in enumerate(T):
            while stk and t > T[stk[-1]]:
                curr = stk.pop()
                ans[curr] = i - curr
            
            stk.append(i)
        
        return ans