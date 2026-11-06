class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        res = []
        for i in strs:
            key = ''.join(sorted(i))
            hmap[key].append(i)
        for i in hmap.values():
            res.append(i)
        return res