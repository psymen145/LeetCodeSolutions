class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = len(a)
        if len(a) > len(b):
            max_len = len(a)
            b = ("0" * (len(a) - len(b))) + b
        elif len(a) < len(b):
            max_len = len(b)
            a = ("0" * (len(b) - len(a))) + a
        
        carry_over = False
        i = max_len - 1
        sum_str = ""
        while i >= 0 or carry_over:
            if i < 0 and carry_over:
                sum_str = "1" + sum_str
                break
            
            if a[i] == "1" and b[i] == "1":
                if carry_over:
                    sum_str = "1" + sum_str
                    carry_over = True
                else:
                    sum_str = "0" + sum_str
                    carry_over = True
            elif a[i] == "1" and b[i] == "0":
                if carry_over:
                    sum_str = "0" + sum_str
                    carry_over = True
                else:
                    sum_str = "1" + sum_str
                    carry_over = False
            elif a[i] == "0" and b[i] == "1":
                if carry_over:
                    sum_str = "0" + sum_str
                    carry_over = True
                else:
                    sum_str = "1" + sum_str
                    carry_over = False
            elif a[i] == "0" and b[i] == "0":
                if carry_over:
                    sum_str = "1" + sum_str
                    carry_over = False
                else:
                    sum_str = "0" + sum_str
                    carry_over = False
                    
            i -= 1
            
        return sum_str