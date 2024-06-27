"""
days are ordered, so we can do binary search to check each day
when flowers are bloomed. then look at adjacent flowers.
"""
from collections import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        start, end = min(bloomDay), max(bloomDay)
        min_days = -1
        while start <= end:
            days = (start + end) // 2
            count, bouquets = 0, 0
            for flower in bloomDay:
                count = count + 1 if flower <= days else 0
                if count == k:
                   bouquets += 1
                   count = 0
            if bouquets >= m:
                min_days = days
                end = days - 1
            else:
                start = days + 1
        return min_days
