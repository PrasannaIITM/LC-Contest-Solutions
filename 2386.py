import heapq

class Maxheap:
    def __init__(self):
        self.nums = []
        self.n = len(self.nums)
        
    def pop(self):
        (ele, i) = heapq.heappop(self.nums)
        return (-ele, i)
    
    def push(self, tup_ele):
        heapq.heappush(self.nums, (-tup_ele[0], tup_ele[1]))

class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        max_sum = sum([max(0, num) for num in nums])
        abs_nums = [abs(num) for num in nums]
        abs_nums.sort()
        
        max_heap = Maxheap()
        max_heap.push((max_sum - abs_nums[0], 0))
        next_sum = max_sum
        
        for t in range(k - 1):
            (next_sum, i) = max_heap.pop()
            if i + 1 < len(abs_nums):
                max_heap.push((next_sum + abs_nums[i] - abs_nums[i + 1], i + 1))
                max_heap.push((next_sum - abs_nums[i + 1], i + 1))

        return next_sum