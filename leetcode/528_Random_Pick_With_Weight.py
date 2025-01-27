class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        We can create a prefix_sum array where each weight is the
        cumulative sum of weights up to that index.
        """
        self.prefix_sums = []
        self.total_sum = 0
        for weight in w:
            self.total_sum += weight
            self.prefix_sums.append(self.total_sum)

    def pickIndex(self):
        """
        :rtype: int
        Generate a random number in the range of [1, total_sum] where
        total_sum is the sum of weights.
        Use a binary search on the prefix_sum array to see which weight
        segment the random number will fall into.
        """
        target = random.randint(1, self.total_sum)
        return bisect_left(self.prefix_sums, target)
