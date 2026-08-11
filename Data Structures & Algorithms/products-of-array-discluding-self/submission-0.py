class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        post = [0]*len(nums)
        j = len(nums)-1
        pre[0] = nums[0]
        temp = nums[0]
        for i in range(1, len(nums)):
            pre[i] = temp * nums[i]
            temp = pre[i]
        post[len(nums)-1] = nums[len(nums)-1]
        temp = nums[len(nums)-1]
        for i in range(len(nums)-2 , -1, -1):
            post[i] = temp * nums[i]
            temp = post[i]
        res = []
        for i in range (len(nums)):
            if i == 0:
                res.append(post[1])
            elif i == len(nums)-1:
                res.append(pre[i-1])
            else:
                res.append(pre[i-1] * post[i+1])
        return res
