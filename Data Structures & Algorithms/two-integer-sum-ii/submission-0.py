class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers
        f, l = 0, len(numbers)-1
        while f < l :

            if n[f] + n [l] == target:
                return [f+1, l+ 1]
            elif n[f] + n [l] > target:
                l -=1
            elif n[f] + n [l] < target:
                f +=1
            



        