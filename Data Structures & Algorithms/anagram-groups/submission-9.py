class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        res = []
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            hmap[key].append(strs[i])
        for i in hmap.values():
            res.append(i)
        return res