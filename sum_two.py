class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        List = []
        x = len(nums) -1
        for i in (range(len(nums) -1)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    List.append(i)
                    List.append(j)
                    return List
                else:
                    pass
        