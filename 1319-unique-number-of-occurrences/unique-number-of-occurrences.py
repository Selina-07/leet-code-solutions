class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res=[]
        chumma=[]
        for i in arr:
            c=0
            if i not in chumma:
                c=arr.count(i)
                res.append(c)
                chumma.append(i)
        if len(set(res))!= len(res):
            return False
        else:
            return True







        