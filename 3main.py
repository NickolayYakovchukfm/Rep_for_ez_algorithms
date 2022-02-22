#python Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        n = str(x)
        new_string = n[::-1]
        if new_string == n:
            return True
        else:
            return False
#python Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            result = target - nums[i]
            if result in hashmap:
                return [i, hashmap[result]]
            hashmap[nums[i]] = i
#python Richest Customer Weath
class Solution(object):
    def maximumWealth(self, accounts):
        ans = sum(accounts[0])
        for i in range(len(accounts)):
            if sum(accounts[i]) > ans:
                ans = sum(accounts[i])
        return ans
