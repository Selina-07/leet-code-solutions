class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in sentences:
            words=1
            for j in i:
                if j==" " :
                    words+=1
            if words>max:
                max=words
        return max
            
