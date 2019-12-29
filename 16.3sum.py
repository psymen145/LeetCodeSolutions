class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution_list = []
        length_of_nums = len(nums)

        for i in range(length_of_nums-2):
            if i == 0 or i > 0 and nums[i - 1] != nums[i]:
                l = i+1
                r = length_of_nums-1

                while(l < r):
                    s = nums[i] + nums[l] + nums[r]
                    if s == 0:
                        solution_list.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while r > l and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1

        return solution_list