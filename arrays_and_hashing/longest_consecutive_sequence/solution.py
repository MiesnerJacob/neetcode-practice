class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_unique_nums = sorted(set(nums))

        if not sorted_unique_nums:
            return 0
        if len(sorted_unique_nums) == 1:
            return 1

        counts = []
        counter = 1
        last = None

        for i in sorted_unique_nums:
            if last == None:
                pass
            elif i == last + 1:
                counter += 1
            else:
                counter = 1
            counts.append(counter)
            last = i
        return max(counts)