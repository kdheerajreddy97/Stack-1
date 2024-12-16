# Similar to daily Temperatures question but it since its circular we need to iterate over it twice to find next greater number
# Dont forget to skip the number (i.e. appending to stack) that have already been added before
# Time: O(2n) Space: O(n) + O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mystack = []
        res = [-1] * n

        for i in range(2 * n):
            while mystack and nums[mystack[-1]] < nums[i % n]:
                temp = mystack.pop()
                next_greater = nums[i % n]
                res[temp] = next_greater
            # Append to stack only if it's the first iteration or if the element hasn't been processed
            if i < n:
                mystack.append(i % n)
            else:
                if mystack[-1] == i % n:
                    break

        return res