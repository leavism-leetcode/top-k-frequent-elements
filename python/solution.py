# Copy/paste template from LeetCode below
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numberCount = dict()

        for number in nums:
            numberCount[number] = numberCount.get(number, 0) + 1

        result = []

        for _ in range(k):
            largest = max(numberCount.values())
            for key in numberCount:
                if numberCount[key] == largest:
                    result.append(key)
                    numberCount.pop(key)
                    break
        
        return result

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
solution = Solution()
nums = [1,1,1,2,2,3]
k = 2

nums2 = [1]
k2 = 1

print(solution.topKFrequent(nums, k))
print(solution.topKFrequent(nums2, k2))