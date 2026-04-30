"""Task №1 from Data Structures Curse"""

from array import array, ArrayType

def move_zeros_to_end(arr: ArrayType) -> ArrayType:
    """
    Functions moves all zeros to the end without changing the order of non-zero elements.

    Arguments:
    - arr: ArrayType, not ordered array with int elements in it.

    Return: ArrayType, ordered array with int elements in it.
    """
    coef = 0
    iters = len(arr)
    for i in range(iters):
        pos = i - coef
        if arr[pos] == 0:
            deleted = arr.pop(pos)
            arr.insert(-1, deleted)
            coef += 1
    return arr

if __name__ == '__main__':
    myarr = array('I', [0, 1, 0, 2, 0, 3, 0])
    print(move_zeros_to_end(myarr))
