class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) -1
        for i in range(len(s) - 1):
            if i == math.ceil(len(s)/2):
                break
            begin = s[i]
            last = s[j]
            s[i] = last
            s[j] = begin
            j -= 1
