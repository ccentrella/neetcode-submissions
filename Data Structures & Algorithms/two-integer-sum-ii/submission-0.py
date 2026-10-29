class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            left_num, right_num = numbers[left], numbers[right]
            if left_num + right_num == target:
                return [left_num, right_num]
            elif left_num + right_num < target:
                left += 1
            else:
                right -= 1