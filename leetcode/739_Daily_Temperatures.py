class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []

        #Iterate in reverse
        for i in range(n - 1, -1, -1):
            #Pop from stack until warmer temp found
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            #if stack not empty find days to wait.
            if stack:
                answer[i] = stack[-1] - i

            #Push the current day's index onto stack
            stack.append(i)
        
        return answer

        #time O(n) each index is pushed and popped
        #at most once.
        #space O(n) for stack and output array
