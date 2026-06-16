class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for x, nu in enumerate(nums):
                if num + nu == target and i != x:
                    return [i, x]
                else:
                    continue
                
        