class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Phase 1: count frequency of each number
        frequency = {}
        for value in nums:
            frequency[value] = frequency.get(value, 0) + 1

        # Phase 2: bucket sort — index = frequency, value = list of nums with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, count in frequency.items():
            buckets[count].append(val)

        # Phase 3: traverse buckets from highest frequency to lowest, collect k values
        answer = []
        for bucket in reversed(buckets):
            for val in bucket:
                answer.append(val)
                if len(answer) == k:
                    return answer

        return answer