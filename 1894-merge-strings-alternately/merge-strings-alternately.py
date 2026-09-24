class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=[];
        n1, n2=len(word1), len(word2)
        l=max(n1,n2)
        for i in range(l):
            if i<n1:
                m.append(word1[i])
            if i<n2:
                m.append(word2[i])
        return "".join(m)

        