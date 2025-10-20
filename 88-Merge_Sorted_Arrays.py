class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # Shift the first m bits in nums1 to the end of nums1.
        for i in range(1,m+1):
            #nums1[(m - i) * -1] = nums1[i]
            nums1[-i] = nums1[m - i]

        curr_1i = -m # Index of current item being selected from nums1
        curr_2i = 0 # Index of current item being selected from nums2
        curr_res_i = 0 # Index of the current item being added to the result list
        while curr_res_i < (m + n):
            if m == 0:
                for i in range(n):
                    nums1[i] = nums2[i]
                curr_res_i = n # Terminate loop
            elif n == 0:
                curr_res_i = m # Terminate loop
            elif curr_2i == n:
                curr_res_i = m + n # Terminate loop
            else:
                if curr_1i == 0:
                    nums1[curr_res_i] = nums2[curr_2i]
                    curr_2i += 1
                elif nums2[curr_2i] < nums1[curr_1i]:
                    nums1[curr_res_i] = nums2[curr_2i]
                    curr_2i += 1
                else:
                    nums1[curr_res_i] = nums1[curr_1i]
                    curr_1i += 1
                curr_res_i += 1