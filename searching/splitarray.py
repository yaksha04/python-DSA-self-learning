class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = (l + r) // 2

            parts = 1
            cursum = 0

            for num in nums:
                if cursum + num > mid:
                    parts += 1
                    cursum = 0

                cursum += num

            if parts <= k:
                r = mid
            else:
                l = mid + 1

        return l
