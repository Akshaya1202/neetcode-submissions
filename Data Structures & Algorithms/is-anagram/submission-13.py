class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc,tc = {},{}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sc[s[i]] = sc.get(s[i],0) + 1
            tc[t[i]] = tc.get(t[i],0) + 1
        return sc == tc