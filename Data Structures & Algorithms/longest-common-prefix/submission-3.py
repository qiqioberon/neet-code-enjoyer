class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
            return strs[0]
        maps={}
        for string in strs:
            temp = ""
            for s in string:
                temp += s
                maps[temp] = maps.get(temp, 0) + 1
        sortedMap = dict(sorted(maps.items(), key= lambda x: (x[1], len(x[0])), reverse=True))
        if sortedMap == {}: 
            return ""
        res = next(iter(sortedMap.values()))
        if res != 1 and res == len(strs):
            return str(next(iter(sortedMap)))
        else: 
            return ""
