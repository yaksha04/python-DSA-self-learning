```python
class Solution:
    def minmaxGasDist(self, stations: list[int], k: int) -> float:
        l = 0.0
        h = float(stations[-1] - stations[0])

        if h == 0:
            return 0.0

        for _ in range(100):
            mid = (l + h) / 2
            req = 0

            for i in range(1, len(stations)):
                gap = stations[i] - stations[i - 1]
                req += int((gap - 1e-12) / mid)

                if req > k:
                    break

            if req <= k:
                h = mid
            else:
                l = mid

        return h
```
