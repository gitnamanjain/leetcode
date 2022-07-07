class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                threesum = a+nums[left]+nums[right]
                if (threesum == 0):
                    res.append([a, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # while left < right and nums[right] == nums[right-1]:
                    #     right -= 1
                    left += 1
                    right -= 1
                elif(threesum > 0):
                    right = right-1
                elif(threesum < 0):
                    left = left+1
        return(res)
