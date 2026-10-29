class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Two step solution
        # Create dictionary based on number of times, NOT number
        # Iterate from END of dictionary and continue for K non-null values

        # Step 1: Calculate and store count for each number
        occurrences_by_num = {}
        for num in nums:
            occurrences_by_num[num] = occurrences_by_num.get(num, 0) + 1

        # Step 2: Transform data to retrieve numbers for each count
        occurrences_by_count = {}
        for num, count in occurrences_by_num.items():
            nums_at_count = occurrences_by_count.get(count, [])
            nums_at_count.append(num)
            occurrences_by_count[count] = nums_at_count

        # Step 3: Retrieve top k greatest counts
        output, current_count = [], len(nums)
        while len(output) < k:
            output += occurrences_by_count.get(current_count, [])
            current_count -= 1

        return output