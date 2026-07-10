class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = {}
        if(len(s) != len(t)): return False
        for i in range(len(s)):
            maps[s[i]] = maps.get(s[i], 0) + 1
            maps[t[i]] = maps.get(t[i], 0) - 1
        for a in maps.values():
            if (a != 0): 
                return False
        return True