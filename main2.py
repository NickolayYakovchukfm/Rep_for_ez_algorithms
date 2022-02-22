class Solution:
    def longestSubarray(self, nums):
        start_of_zero = 0
        len_of_1s = 0
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 0
            hashmap[nums[i]] += 1
            
            while 0 in hashmap and hashmap[0] > 1:
                hashmap[nums[start_of_zero]] -= 1
                start_of_zero += 1
                
            len_of_1s = max(len_of_1s, i - start_of_zero)
        
        return len_of_1s
