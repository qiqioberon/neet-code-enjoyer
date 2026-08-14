class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        maps = {}
        CD = False
        CN = False
        for i in range(len(nums)):
            val = nums[i]
            if val not in maps:
                maps[val] = i
            else:
                CD = True
                if abs(i - maps[val]) > k:
                    maps[val] = i
                else:
                    CN = True
        return CD & CN
            