class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = sum(int(i) ** 2 for i in str(n))
            if n == 1:
                return True
            elif n not in seen:
                seen.add(n)
            else:
                break
        return False
