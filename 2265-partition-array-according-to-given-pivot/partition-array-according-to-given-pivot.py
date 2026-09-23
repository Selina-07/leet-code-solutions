class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        small=[]
        big=[]
        piv=[]
        for i in nums:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                big.append(i)
            elif i == pivot:
                piv.append(i)
            else:
                continue
        s=len(small)
        b=len(big)
        p=len(piv)
        nums[0:s]=small
        nums[s:s+p]=piv
        nums[s+p:b+s+p]=big
        return nums

        
        