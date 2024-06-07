# Copy/paste template from LeetCode below
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = dict()

        # Make hashmap with the number as key and count of occurance as value
        for number in nums:
            countDict[number] = countDict.get(number, 0) + 1

        # Bucket sort
        # Fill countBucket list with empty lists
        # Put as many empty lists as there possible different occurances.
        # Index of array represents the count of occurances. There can only be len(nums) + 1 possible different occurances.
        # ex: len(nums) = 6. Then the max number of occurances is 6 as a number can only appear 6 times (the same number appears 6 times).
        # but we add an additional slot for the 0th index, representing a number occuring 0 times for clarity. Logically, a number cannot
        # occur 0 times because that number would just not be in the list. We will just add a 0th index in the array so that we don't
        # have to adjust the index everywhere else.
        countBucket = [[] for _ in range(len(nums) + 1)]

        # Append the value of countDict to the countBucket list at key index
        for key, value in countDict.items():
            countBucket[value].append(key)

        # In descending order (because we want most frequent occurances),
        # append the number to result list
        # stop and return result list when we have len(result) == k
        result = []
        for number in range(len(countBucket) - 1, 0, -1):
            for value in countBucket[number]:
                result.append(value)
                if len(result) == k:
                    return result

# After copy/pasting the template from LeetCode, uncomment the following to start testing.
solution = Solution()
nums = [1,1,1,2,2,100, 100, 100, 100]
k = 2

nums2 = [1]
k2 = 1

print(solution.topKFrequent(nums, k))
print(solution.topKFrequent(nums2, k2))