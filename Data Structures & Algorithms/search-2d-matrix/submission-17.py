def binary1(low:int, high:int, matrix:List[List[int]], target:int):
    med = (high+low)//2
    if low>high or med> len(matrix) -1:
        return -1
    print(med)
    if list_resolve(matrix[med], target) == ">":
        return binary1(med+1, high, matrix, target)
    elif list_resolve(matrix[med], target) == "<":
        return binary1(low, med-1, matrix, target)
    else:
        return med
def list_resolve(nums, target):
    if nums[0] > target:
        return "<"
    elif target > nums[-1]:
        return ">"
    if nums[0] <= target <= nums[-1]:
        return "="
def binary2(low:int, high:int, matrix:List[int], target:int):

    med = (high+low)//2
    if low>high:
        return False

    if target > matrix[med]:
        return binary2(med+1, high, matrix, target)
    elif target < matrix[med]:
        return binary2(low, med-1, matrix, target)
    else:
        return True

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) ==1:
            if len(matrix[0]) ==1:
                return target == matrix[0][0]
            else:
                return  binary2(0, len(matrix[0])-1, matrix[0], target)
        elif len(matrix[0]) ==1:
            return  binary2(0, len([item for sublist in matrix for item in sublist])-1, [item for sublist in matrix for item in sublist], target)
        return binary2(0, len(matrix[0])-1, matrix[binary1(0, len(matrix), matrix, target)], target)
        




        