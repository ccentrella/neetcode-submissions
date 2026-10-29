class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Calculate product on left and right side for each value
        # Multiply these together to get correct product at each position

        left, right = 1, len(nums) - 2
        left_products, right_products = [1 for _ in nums], [1 for _ in nums]

        for _ in range(len(nums) - 1):
            left_products[left] = left_products[left-1] * nums[left-1]
            right_products[right] = right_products[right+1] * nums[right+1]
            left += 1; right -= 1

        result = [left_products[index] * right_products[index] for index in range(len(nums))]

        return result