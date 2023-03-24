from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            res = target - nums[i] 
            dic[res] = i
            
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == target - nums[i]:
        #             return [i,j]

if __name__ == '__main__':
    soln = Solution()
    nums = [2,3,4,5,6,7,8]
    target = 9
    print(soln.twoSum(nums,target))
