class Solution:
    def intToRoman(self, num: int) -> str:
        final_roman = ''
        
        if num // 1000 > 0:
            thousands = num // 1000
            
            for i in range(thousands):
                final_roman += 'M'
            
            num -= (thousands * 1000)
            
        if num // 900 > 0:
            final_roman += 'CM'
            num -= 900
            
        if num // 500 > 0:
            final_roman += 'D'
            num -= 500
            
        if num // 400 > 0:
            final_roman += 'CD'
            num -= 400
            
        if num // 100 > 0:
            hundreds = num // 100
            
            for i in range(hundreds):
                final_roman += 'C'
                
            num -= (hundreds * 100)
        
        if num // 90 > 0:
            final_roman += 'XC'
            num -= 90
            
        if num // 50 > 0:
            final_roman += 'L'
            num -= 50
            
        if num // 40 > 0:
            final_roman += 'XL'
            num -= 40
            
        if num // 10 > 0:
            tens = num // 10
            
            for i in range(tens):
                final_roman += 'X'
                
            num -= (tens * 10)
            
        if num // 9 > 0:
            final_roman += 'IX'
            num -= 9
            
        if num // 5 > 0:
            final_roman += 'V'
            num -= 5
            
        if num // 4 > 0:
            final_roman += 'IV'
            num -= 4
            
        if num // 1 > 0:
            ones = num // 1
            
            for i in range(ones):
                final_roman += 'I'
                
            num -= (ones * 1)
            
        return final_roman