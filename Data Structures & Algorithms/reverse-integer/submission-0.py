class Solution:
    def reverse(self, x: int) -> int:
        originalx = x
        x = abs(x)

        result = 0
        while x > 0:
            
            lastint = x % 10
            x = x//10
            result = (result * 10) + lastint

        if originalx  < 0:
            result = -result

        if result > 2**31 -1 or result < -2**31:
            result = 0
             
        return result


