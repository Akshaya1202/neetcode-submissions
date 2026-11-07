class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap = {}
        for i,v in enumerate(numbers):
            diff = target - v
            if diff in hmap:
                return [hmap[diff]+1, i+1]
            hmap[v] = i
        