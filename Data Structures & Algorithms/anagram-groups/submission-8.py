class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            hmap[key].append(i)
        return list(hmap.values())