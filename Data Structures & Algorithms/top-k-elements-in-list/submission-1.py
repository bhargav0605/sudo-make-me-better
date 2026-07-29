import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # phase 1
        frequency = {}
        values = []
        answer = []
        for index, value in enumerate(nums):
            if value in frequency:
                frequency[value] = frequency.get(value) + 1
            else:
                frequency[value] = 1

        print(f"{frequency}")

        # phase 2
        # heap = [(-count, val) for val, count in frequency.items()]
        # values = [[]] * len(nums)
        values = [[] for _ in range(len(nums)+1)]
        print(f"{values}")
        for val, count in frequency.items():
            print(f"{val}, {count}")
            values[count].append(val)
        

        for bucket in reversed(values):
            if bucket:
                for val in bucket:
                    answer.append(val)
            if len(answer) == k:
                break

        return answer