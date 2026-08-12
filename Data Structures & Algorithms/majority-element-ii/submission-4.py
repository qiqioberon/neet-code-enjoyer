class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        maps = {}
        for i in nums:
            maps[i] = maps.setdefault(i, 0) + 1
            if maps[i] > len(nums)/3:
                if i not in res:
                    res.append(i)
        return res