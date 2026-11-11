class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        seen = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            target = -nums[i]
            while left < right:
                total = nums[left] + nums[right]
                if total == target:
                    found = [nums[i], nums[left], nums[right]]
                    if found not in seen:
                        seen.append(found)
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return seen