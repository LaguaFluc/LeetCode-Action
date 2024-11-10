
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        
        ans = [-1, -1]
        left, right = 0, n - 1
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
        if nums[left] != target:
            return ans 
        ans[0] = left

        right = n - 1
        while (left < right):
            print(left, right)
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid  + 1
        if nums[right - 1] != target:
            return ans
        ans[1] = right - 1
        return ans 


nums = [5,7,7,8,8,10]
target = 8

print(Solution().searchRange(nums, target))
nums = [5,7,7,8,8,10]
target = 6

print(Solution().searchRange(nums, target))