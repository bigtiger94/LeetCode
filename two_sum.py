class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for ii in range(len(nums)):
            need = target-nums[ii]
            
            if target-nums[ii] in nums:
                if ii !=nums.index(need):
                    return(ii, nums.index(need))

        
        return(None)