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


#################################################################

def get_intersection_with_maintained_frequency(a, b):
    """
    Args:
     a(list_int32)
     b(list_int32)
    Returns:
     list_int32
    """
    result = []
    counts = {}

    for x in a:
        counts[x] = counts.get(x, 0) + 1

    for x in b:
        if counts.get(x, 0) > 0:
            result.append(x)
            counts[x] -= 1

    return result

#####################################################################

def count_alphabets(s):
    """
    Args:
     s(str)
    Returns:
     int32
    """
    #First Attempt
    '''count = 0
    for a in s:
        if (a >= 'a' and a <= 'z') or (a >= 'A' and a <= 'Z') :
            count += 1
    return count'''
    #Most Pythonic
    return sum(ch.isalpha() for ch in s)

######################################################################

def uppercase_to_lowercase(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    # Write your code here.
    return s.lower()

######################################################################

def reverse_words(s):
    """
    Args:
     s(str)
    Returns:
     str
    """
    return ' '.join(reversed(s.split()))

######################################################################


def get_pivot_index(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     int32
    """
    total = sum(numbers)
    left = 0

    for i, x in enumerate(numbers):
        right = total - x - left
        if right == left:
            return i
        left += x

    return -1

######################################################################

def find_first_occurrence(s, to_find):
    """
    Args:
     s(str)
     to_find(char)
    Returns:
     int32
    """
    return s.find(to_find)

######################################################################

def length_of_last_word(sentence):
    """
    Args:
     sentence(str)
    Returns:
     int32
    """
    words = sentence.split()
    return len(words[-1]) if words else 0

######################################################################
