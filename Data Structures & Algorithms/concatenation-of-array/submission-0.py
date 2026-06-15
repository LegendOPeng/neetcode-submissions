class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x = []
        for i in range(2):
            x.extend(nums)
        return x