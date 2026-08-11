class Solution:
    def isAlpha(self, s:str) -> bool:
        if s >= 'a' and s <= 'z' :
            return True
        elif s >= 'A' and s <= 'Z' :
            return True
        elif s >= '0' and s <= '9' :
            return True

        return False
        

    def isPalindrome(self, s: str) -> bool:
        j = len(s) -1
        i = 0
        while i < len(s) :
            while self.isAlpha(s[i]) == False and i< len(s)-1:
                i += 1
            while self.isAlpha(s[j]) == False and j > -1:
                j -= 1
            print(s[i], s[j], i, j)
            if s[i].lower() != s[j].lower():
                print(s[i].lower(), s[j].lower())
                print(i,j)
                return False
            elif s[i].lower() == s[j].lower():
                j -= 1
                i +=1  
        return True