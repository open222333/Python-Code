# Approach 1: Horizontal scanning
# Approach 2: Vertical scanning
# Approach 3: Divide and conquer
# Approach 4: Binary search

class MySolution:
    def longestCommonPrefix(self, strs):
        # strsLen = len(strs)
        # itemLen = 200
        # itemPrefix = ''
        # for item in strs:  # 找出最小長度
        #     itemLen = min(itemLen, len(item))
        # for item2 in strs:
        pass


class zhanweitingSolution:
    def longestCommomPrefix(self, strs):
        if len(strs) == 0:
            return ''
        i = 0
        for i, chars in enumerate(zip(*strs), start=1):
            if len(set(chars)) != 1:
                i -= 1
                break
        return strs[0][:i]


strs = ["flower", "flow", "flight"]
for i, chars in enumerate(zip(*strs), 1):
    # print(set(chars))
    # print(len(set(chars)))
    print("i=", i, ",chars=", chars)
    if len(set(chars)) != 1:
        i -= 1
        print("i =", i)
        break

print(zhanweitingSolution().longestCommomPrefix(strs))
