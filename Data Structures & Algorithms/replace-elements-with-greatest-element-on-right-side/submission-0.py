class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = -1
        ans = [0] * len(arr)
        ans[-1] = rightmax
        print(ans)
        for i in range(len(arr)-2,-1,-1):
            rightmax = max(arr[i+1], rightmax)
            ans[i] = rightmax
        return ans