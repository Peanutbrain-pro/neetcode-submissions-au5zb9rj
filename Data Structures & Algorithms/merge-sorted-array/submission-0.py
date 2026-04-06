class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        ptr1, ptr2, ptr3 = 0, 0, 0
        temp: List[float] = [float("inf")] * m
        temp_top = 0
        for i in range(m):
            if ptr2 < n and nums1[i] < nums2[ptr2]:
                if nums1[i] < temp[ptr3]:
                    # print(
                    #     f"{i}th iteration: {nums1},    temp = {temp}, ptr3={ptr3}, nums2 = {nums2[ptr2:]}"
                    # )
                    continue
                else:
                    # print("--------------ptr3 should change")
                    temp[temp_top] = nums1[i]
                    temp_top += 1
                    nums1[i] = temp[ptr3]
                    ptr3 += 1
            else:
                temp[temp_top] = nums1[i]
                temp_top += 1
                if ptr2 < n and nums2[ptr2] < temp[ptr3]:
                    nums1[i] = nums2[ptr2]
                    ptr2 += 1
                else:
                    # print("---------------ptr3 should change")
                    nums1[i] = temp[ptr3]
                    ptr3 += 1

        #     print(
        #         f"{i}th iteration: {nums1},    temp = {temp}, ptr3={ptr3}, nums2 = {nums2[ptr2:]}"
        #     )

        # print(f"First m indexes done\nptr1={ptr1}, ptr2={ptr2}, ptr3={ptr3}")
        for i in range(n):
            if ptr2 >= n and ptr3 < m:
                nums1[m + i] = temp[ptr3]
                ptr3 += 1
                continue
            if ptr3 >= m and ptr2 < n:
                nums1[m + i] = nums2[ptr2]
                ptr2 += 1
                continue

            if nums2[ptr2] < temp[ptr3]:
                nums1[m + i] = nums2[ptr2]
                ptr2 += 1
            else:
                nums1[m + i] = temp[ptr3]
                ptr3 += 1

            # print(
            #     f"{i}th iteration: {nums1},    temp = {temp}, ptr3={ptr3}, nums2 = {nums2[ptr2:]}"
            # )