from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = {}
        for i in nums:
            if i not in frequency_map:
                frequency_map[i] = 1
            else:
                frequency_map[i] += 1
        
        # Convert the frequency map to a list of tuples
        frequency_tuple = [(i,j) for i, j in frequency_map.items()]
        
        # Sort the list of tuples by the frequency in descending order
        sorted_frequency_tuple = sorted(frequency_tuple, key=lambda x: x[1], reverse=True)
        
        # Return the first k elements of the sorted list
        return [i for i,j in sorted_frequency_tuple[:k]]
