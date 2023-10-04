class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # perform binary search
        # if less than than pivot search left of pivot
        # if bigger than pivot search right of pivot

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = int(l + ((r - l) / 2))

            if nums[m] == target:
                return m
            elif nums[m] < target: # search right
                l = m + 1
            elif nums[m] > target: # search left
                r = m - 1

        return -1
        

        