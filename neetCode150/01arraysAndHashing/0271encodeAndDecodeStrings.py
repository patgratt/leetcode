# neetcode solution - O(n)
class Codec:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> list[str]:
            res = []
            # pointer that marks start of string
            i = 0

            while i < len(s):
                j = i
                # necessary for multi-digit lengths
                while s[j] != "#":
                    j += 1
                length = int(s[i:j])
                res.append(s[j + 1 : j + 1 + length])
                i = j + 1 + length
            return res


# testcase1
tc1 = ["-=W",""]
codec = Codec()
print(codec.decode(codec.encode(tc1)))

# testcase2
tc2 = ["abc99#-efgh", "foo"]
print(codec.decode(codec.encode(tc2)))