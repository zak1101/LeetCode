def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums_len = len(nums)
    
    if nums_len < 2:
        return nums_len

    greatest = nums[0] - 1
    front_pointer = 0

    while front_pointer < nums_len:
        curr_num = nums[front_pointer]
        if curr_num <= greatest:
            for replacement_pointer in range(front_pointer, nums_len):
                if nums[replacement_pointer] > greatest:
                    greatest = nums[replacement_pointer]
                    nums[front_pointer] = greatest
                    break
            # If the num at the front pointer is not changed, no greater value was found, and all duplicates were removed.
            if curr_num == nums[front_pointer]:
                return front_pointer
        else:
            greatest = curr_num
        front_pointer += 1
    
    return front_pointer

nums = [1,2,2,3,3]

print(removeDuplicates(nums))

print(nums)