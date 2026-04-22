class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = nums1
        n2 = nums2
        if len(n2) < len(n1):
            n1, n2 = n2, n1

        # n1 is the smaller array
        if len(n1) == 0:
            mid = len(n2) // 2
            if len(n2) % 2:
                return n2[mid]
            else:
                return (n2[mid] + n2[mid - 1]) / 2

        # no empty lists
        # the median should be in the right element if only one
        required_left_elements = (len(n1) + len(n2)) // 2
        is_even = True if (len(n1) + len(n2)) % 2 == 0 else False
        l = 0
        r = len(n1) - 1
        # print(f"n1: {n1}\tn2: {n2}")
        while l <= r:
            mid = (l + r) // 2
            n2_left_last = required_left_elements - mid - 2
            # print(n2[: n2_left_last + 1])
            # print(n1[: mid + 1])
            # print()

            if (mid + 1) < len(n1):
                if n2[n2_left_last] > n1[mid + 1]:
                    # need to make n1 left side larger
                    l = mid + 1
                    continue

            if (n2_left_last + 1) < len(n2):
                if n1[mid] > n2[n2_left_last + 1]:
                    # need to make n1 left side smaller
                    r = mid - 1
                    continue

            # got the left elements
            if (mid + 1) < len(n1):
                if (n2_left_last + 1) < len(n2):
                    right_first = min(n1[mid + 1], n2[n2_left_last + 1])
                else:
                    right_first = n1[mid + 1]
            else:
                right_first = n2[n2_left_last + 1]

            if is_even:
                if n2_left_last >= 0:
                    left_last = max(n1[mid], n2[n2_left_last])
                else:
                    left_last = n1[mid]
                return (left_last + right_first) / 2
            else:
                return right_first

        # n1 array doesn't contain any left split elements
        if required_left_elements < len(n2):
            right_first = min(n2[required_left_elements], n1[0])
        else:
            right_first = n1[0]

        if is_even:
            left_last = n2[required_left_elements - 1]
            return (left_last + right_first) / 2
        else:
            return right_first

