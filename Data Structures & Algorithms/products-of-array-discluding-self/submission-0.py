class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]
        length = len(nums)

        pref = 1
        for i in nums[:-1]:
            pref *= i
            output.append(pref)

        # print(nums)
        # print("Prefixed output: ", output)

        post = 1
        # print("this is the list for post loop", nums[:0:-1])
        for i, num in enumerate(nums[::-1]):
            # print("Post: ", post, " Index: ", length - i - 1)
            output[length - i - 1] *= post
            # print(output)
            post *= num

        # print(output)

        return output