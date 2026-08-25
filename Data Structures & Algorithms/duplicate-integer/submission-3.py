class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        l = 0

        for i in range(l+1,len(nums)):

            if nums[l] == nums[i]:

                return True

            else:

                l += 1

            
        return False

        