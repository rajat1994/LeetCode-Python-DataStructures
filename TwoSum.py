class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = {}
        k = 0
        j = 0
        for i in range(len(nums)):
            b[nums[i]] = i
            
        for j in range(len(nums)):
            k = target-nums[j]
            if k in b.keys()  and b.get(k)!=j:
                break
        return [j,b.get(k)]