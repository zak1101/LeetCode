class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Handle edge case where an empty list is given.
        if len(nums) == 0:
            return 0

        complete = False
        halt_front_incr = False
        front_i = -1
        back_i = -1
        while not complete:
            if not halt_front_incr:
                front_i += 1

            # Check if the pointers meet / the front pointer ends up behind the back pointer.
            if front_i >= (back_i + len(nums)):
                complete = True

            #Check the num at the current front index
            if nums[front_i] == val:
                halt_front_incr = True
                # If a non-val num is at the curr back index, swap the two elements.
                if nums[back_i] != val:
                    nums[front_i] = nums[back_i] # Swap the val number found in the front with the non-val number in the back.
                    nums[back_i] = val # Not strictly needed given the back_i is incremented anyway.
                    halt_front_incr = False
                else:
                    back_i -= 1 # Move the back pointer left.
            # Handle final iteration where front_i is updated to store the correct num of non-val numbers.
            elif complete:
                front_i += 1
        return front_i