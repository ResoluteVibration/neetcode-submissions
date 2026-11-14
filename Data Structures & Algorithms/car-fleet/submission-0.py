class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        cars = sorted(zip(position, speed), reverse = True)
        for p, s in cars:
            time = (target-p)/s
            if not st or time > st[-1]:
                st.append(time)
        return len(st)