class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        sum=0
        for i in nums:
            if sum<0:
                sum=0
            sum+=i
            maxsum=max(sum,maxsum)
        return maxsum