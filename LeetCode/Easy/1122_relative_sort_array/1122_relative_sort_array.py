class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = {num: 0 for num in arr2}
        remain, out = [], []
        for e in arr1:
            try:
                count[e] += 1
            except KeyError:
                remain.append(e)
        for num in arr2:
            out.extend([num] * count[num])
        remain.sort()
        out.extend(remain)
        return out
