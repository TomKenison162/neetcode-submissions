class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [ x for x in str(int(''.join([str(y) for y in digits])) +1)]
        