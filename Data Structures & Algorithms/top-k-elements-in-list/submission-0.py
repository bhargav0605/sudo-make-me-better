import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # phase 1
        frequency = {}
        answer = []
        for index, value in enumerate(nums):
            if value in frequency:
                frequency[value] = frequency.get(value) + 1
            else:
                frequency[value] = 1

        print(f"{frequency}")

        # phase 2
        heap = [(-count, val) for val, count in frequency.items()]
        heapq.heapify(heap)

        print(f"{heap}")

        for i in range(k):
            top = heapq.heappop(heap)
            answer.append(top[1])

        print(f"{answer}")

        return answer