class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)
        even = False
        if (len1 + len2) % 2 == 0:
            even = True

        left_split_len = (len1 + len2) // 2
        if not nums1:
            if not even:
                return nums2[left_split_len]
            else:
                return (nums2[left_split_len - 1] + nums2[left_split_len]) / 2
        elif not nums2:
            if not even:
                return nums1[left_split_len]
            else:
                return (nums1[left_split_len - 1] + nums1[left_split_len]) / 2

        right_first = None
        left_last = None

        # iterate on nums2
        high1 = None
        low2 = 0
        high2 = len2 - 1

        while low2 <= high2:
            mid = (low2 + high2) // 2

            # if mid - low2 == left_split_len - 1:
            #     if nums2[mid] <= nums1[0]:
            #         right_first = min()
            if mid < left_split_len - 1:
                high1 = left_split_len - mid - 2

                if mid + 1 < len2 and nums2[mid + 1] < nums1[high1]:
                    # nums1 contains an element from the right side
                    # which means more elements from the nums2 are in left side
                    low2 = mid + 1
                    continue

                elif high1 + 1 < len1 and nums1[high1 + 1] < nums2[mid]:
                    # nums2 contains an element from the right side, so more elements from nums1 are in left
                    if mid == 0 or low2 == high2:
                        if left_split_len >= len1:
                            right_first = nums2[mid]
                        else:
                            right_first = min(nums1[left_split_len], nums2[mid])

                        left_last = nums1[left_split_len - 1]

                    high2 = mid - 1
                    continue

                else:
                    if high1 is not None:
                        left_last = max(nums1[high1], nums2[mid])
                        if high1 + 1 < len1:
                            if mid + 1 < len2:
                                right_first = min(nums1[high1 + 1], nums2[mid + 1])
                            else:
                                right_first = nums1[high1 + 1]
                        else:
                            right_first = nums2[mid + 1]
                    else:
                        left_last = nums2[mid]
                        right_first = nums2[mid + 1]

                    break

            else:
                # the whole left split selection is in nums2
                if nums2[mid] > nums1[0]:
                    # this means that one of the element of the left side is in nums1 and right side element in nums2
                    if mid == 0 or low2 == high2:
                        if left_split_len >= len1:
                            right_first = nums2[mid]
                        else:
                            right_first = min(nums1[left_split_len], nums2[mid])

                        left_last = nums1[left_split_len - 1]

                    high2 = mid - 1
                    continue

                right_first = min(nums1[0], nums2[mid + 1])
                left_last = nums2[mid]
                break

        if even:
            return (left_last + right_first) / 2
        else:
            return right_first

