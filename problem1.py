# Brute Force: Time: O(n2)
# Using Stack: Time: O(n), Space: O(n) + O(n) (Stack + res array)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for i in range(0, n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp = stack.pop()
                warmer_day = i - temp
                res[temp] = warmer_day
            stack.append(i)
        return res