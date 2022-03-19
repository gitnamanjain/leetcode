class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2={}
        for i in nums:
            if(i in nums2):
                return True
            nums2[i]=1
        return False