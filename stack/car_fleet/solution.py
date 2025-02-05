class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = [(i, j) for i, j in zip(position, speed)]
        position_speed.sort(reverse=True)

        stack = []
        for p, s in position_speed:
            arrival_time = (target - p) / s
            print(arrival_time)
            stack.append(arrival_time)
            if len(stack) > 1:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        return len(stack)