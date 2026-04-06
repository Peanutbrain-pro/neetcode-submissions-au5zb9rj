class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_ptr = m + n - 1

        while last_ptr >= 0:
            if n - 1 < 0:
                break
            if m - 1 < 0:
                # print("nums1 finished copying nums2")
                nums1[last_ptr] = nums2[n - 1]
                n -= 1
                last_ptr -= 1
                continue

            n1 = nums1[m - 1]
            n2 = nums2[n - 1]
            # print(n1, n2)
            if n1 < n2:
                nums1[last_ptr] = n2
                n -= 1
            else:
                nums1[last_ptr] = n1
                m -= 1

            last_ptr -= 1

            # print("nums1: ", nums1, "\tnums2: ", nums2)
