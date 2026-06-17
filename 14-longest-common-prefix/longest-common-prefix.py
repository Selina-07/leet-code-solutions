class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        new=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]!=last[i]:
                return new
            else:
                new+=first[i]
        return new
        