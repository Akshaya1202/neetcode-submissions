class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = []
        for i in range(len(nums)+1):
            freq.append([])
        hmap = {}
        for i in nums:
            hmap[i] = hmap.get(i,0)+1
        for i,v in hmap.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
            
