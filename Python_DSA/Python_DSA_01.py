def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    s = 0
    e = len(nums) - 1
    while s < e :
        nums[s], nums[e] = nums[e], nums[s]
        s+=1
        e-=1
    return nums


################################################################


def insert_element_at_position(nums, element, position):
    """
    Args:
     nums(list_int32)
     element(int32)
     position(int32)
    Returns:
     list_int32
    """
    nums.insert(position - 1, element)
    nums.pop()
    return nums
