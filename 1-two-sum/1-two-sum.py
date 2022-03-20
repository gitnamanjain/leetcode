class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={} 
        for i in range(len(nums)):
            if(not (target-nums[i]) in hashmap):
                hashmap[nums[i]]=i
            else:
                return([hashmap[target-nums[i]],i])
