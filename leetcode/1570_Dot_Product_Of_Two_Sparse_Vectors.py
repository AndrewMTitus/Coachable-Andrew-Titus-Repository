class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        we create a dictionary that only stores non-zero elements,
        with indices as keys and elements as values.
        """
        self.pairs = {}
        for i, num in enumerate(nums):
            if nums != 0:
                self.pairs[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        we iterate over the two vectors and check if the smaller
        dictionary has the same indices in the other vector. If so, 
        we sum the product of the matching values. We also want to swap
        vectors in the case where one is smaller than the other, so
        that we always iterate over the smallest vector leading to more
        efficient computations.
        """
        result = 0
        if len(self.pairs) > len(vec.pairs):
            self.pairs, vec.pairs = vec.pairs, self.pairs
        for i, val in self.pairs.items():
            if i in vec.pairs:
                result += val * vec.pairs[i]
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
