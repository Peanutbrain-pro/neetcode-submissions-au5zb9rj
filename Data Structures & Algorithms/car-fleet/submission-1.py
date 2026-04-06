
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position) + 1

        cars = sorted(zip(position, speed), reverse=True)

        time_to_reach = (target - cars[0][0]) / cars[0][1]

        for i, (po, sp) in enumerate(cars):
            time = (target - po) / sp

            if time <= time_to_reach:
                fleets -= 1
            else:
                time_to_reach = time

        return fleets

