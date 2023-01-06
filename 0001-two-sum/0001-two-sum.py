class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for x in range(len(nums)):
            needed = target - nums[x]
            
            if needed in table:
                return [table[needed],x]
            
            table[nums[x]] = x