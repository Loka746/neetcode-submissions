class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []


        for i in range(len(nums)):

            a = nums[i] * nums[i]

            output.append(a)

        output.sort() 

        return output
        