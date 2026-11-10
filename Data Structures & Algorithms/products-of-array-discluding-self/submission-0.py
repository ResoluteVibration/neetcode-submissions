class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr = []
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            new_arr.append(prefix)
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            new_arr[i] *= suffix
            suffix *= nums[i]
        return new_arr