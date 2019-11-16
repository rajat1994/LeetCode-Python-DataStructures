class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        b = {}
        
        for i in nums:
            
         if i in b:
            b[i]+=1
         else:
            b[i]=1
            
        for x in b:
            if b[x] == 1 :
                return x
