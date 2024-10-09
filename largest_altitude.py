class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude, max_altitude = 0,0
        for delta in gain:
            altitude += delta
            max_altitude = max(altitude, max_altitude)
        return max_altitude
