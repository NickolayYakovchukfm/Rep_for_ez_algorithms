class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = strs[0]
        if len(strs) == 0:
            return ""
        for i in range(len(strs)):
            j = 0
            while True:
                if j >= min(len(strs[i]), len(ans)):
                    ans = ans[:min(len(strs[i]), len(ans))]
                    break
                if ans[j] != strs[i][j]:
                    ans = ans[:j:]
                j += 1
        return ans
