class Solution:
    def encode(self, strs: List[str]) -> str:
        length_list = []
        for string in strs:
            length_list.append(len(string))

        encoding = str(length_list)
        return encoding + "".join(strs)

    def decode(self, s: str) -> List[str]:
        # print(s)
        decoded_list = []

        count_list = []
        start = 1
        for i, char in enumerate(s[1:], start=1):
            # print(char)
            # print(i, char)
            if char == ",":
                # print(start, i - 1)
                count_list.append(int(s[start:i]))
                start = i + 2

            if char == "]":
                # start = i + 1
                if s[i - 1] != "[":
                    count_list.append(int(s[start:i]))

                start = i + 1
                break

            # value = 10 * value + int(char)
            # count_list.append(int(char))

        # print(count_list)

        i = start
        # print(i)
        for count in count_list:
            decoded_list.append(s[i : i + count])
            i += count

        # print(decoded_list)
        return decoded_list