class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for i in nums1:
             for j in nums2:
                if ((i==j) and (i not in res)):
                    c1=nums1.count(i)
                    c2=nums2.count(i)
                    if c2>c1:
                        res.extend([i]*c1)
                    else:
                        res.extend([i]*c2)
        return res
        