class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # append (val, index) to a stack
        # pop every element whose val is less than the current val
        # for each element's index, store the difference of indices to the output array

        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                past = stack.pop()
                output[past[1]] = i - past[1]

            stack.append((t, i))

        return output

        # t: O(n)
        # s: O(n)