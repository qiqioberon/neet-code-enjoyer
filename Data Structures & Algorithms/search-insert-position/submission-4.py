class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1] < target:
            return len(nums)
        if nums[0] > target:
            return 0
        l, r = 0, len(nums) - 1
        m = (l+r)//2
        while l < r:
            m = (l+r)//2
            print(nums[m], target)
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
        return l if nums[l] >= target else m if nums[m] >= target else r if nums[r] >= target else -1
