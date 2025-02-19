class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2) - len(s1) + 1):
            if sorted(list(s1)) == sorted(list(s2[i:i + len(s1)])):
                return True
        return False