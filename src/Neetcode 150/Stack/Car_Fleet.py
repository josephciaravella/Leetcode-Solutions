class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True) # cars sorted by starting position

        stack = []
        for car in cars:
            pos, spd = car 
            time = (target - pos)/spd
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)