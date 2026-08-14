class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x
        m = 0
        res= 0
        while i <= j:
            m = (i+j) // 2
            power = m*m
            if power == x:
                return m
            elif power < x:
                i = m+1
                res = m
            else:
                j = m-1
        return res