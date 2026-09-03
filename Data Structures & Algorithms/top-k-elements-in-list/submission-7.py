class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        b = {}

        for ch in nums:
            if ch in b:
                b[ch] += 1
            else:
                b[ch] = 1

        d = []

        for c in sorted(b, key=b.get, reverse=True):
            d.append(c)

        return d[:k]

        # # def topKFrequent(nums, k):
        # b = {}

        # for ch in a:
        #     if ch in b:
        #         b[ch] += 1

        #     else:
        #         b[ch] = 1
        # # print(b)
        # d = []
        # for c in b:
        #     if b[c] >= k:

        #         d.append(c)

            

        # return d

        

                 




        