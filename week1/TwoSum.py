class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # dict1
        # [2,  0]
        # [7,  1]
        # [11, 2]
        # [15, 3]

        res = [0] * 2
        dict1 = {}
        for index, value in enumerate(nums):
            dict1[value] = index

        # two sum 
        for index, value in enumerate(nums):

            dif = target - value

            if dif in dict1.keys() and dict1[dif] != index:
                res[0] = index
                res[1] = dict1.get(dif)
                return res
                

            