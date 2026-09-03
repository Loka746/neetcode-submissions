class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # def topKFrequent(nums, k):
        a = {}

        for num in nums:
            if num not in a:
                a[num] = 1
            else:
                a[num] += 1

        return sorted(a, key=a.get, reverse=True)[:k]

        

                 




        