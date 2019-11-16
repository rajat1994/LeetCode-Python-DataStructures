class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
      if k == 0:
        nums = nums
            
      else:
        
        a= nums[len(nums)-k:len(nums)]
        b= nums[0:len(nums)-k]
        
        z = a+b
        
        for i in range(len(z)):
            nums[i] = z[i]
            