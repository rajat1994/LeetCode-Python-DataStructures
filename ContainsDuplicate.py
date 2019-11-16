class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        b = {}
        a= False
        for i in range(len(nums)):
            if nums[i] in b:
                b[nums[i]] += 1
                if b[nums[i]]>1:
                    a=True
                    break
            else:
                b[nums[i]] = 1
             
        return a
