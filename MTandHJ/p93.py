

from typing import List

from base import version


class Solution:

    @version("32ms, 15mb")
    def restoreIpAddresses(self, s: str) -> List[str]:
        def search(s, stages):
            if stages == 0: 
                if len(s) > 0:
                    return []
                else:
                    return ['']
            if len(s) == 0 and stages > 0:
                return []
            head = ''
            ans = []
            for i, x in enumerate(s[:3]):
                head += x
                if int(head) > 255:
                    break
                sub = search(s[i+1:], stages - 1)
                for y in sub:
                    mark = '.' if y else ''
                    ans.append(mark.join((head, y)))
                if i == 0 and x == '0':
                    break
            return ans
        return search(s, 4)

    @version("32ms, 15.1mb")
    def restoreIpAddresses(self, s: str) -> List[str]:
        def search(s, stages):
            if stages == 0: 
                if len(s) > 0:
                    return []
                else:
                    return ['']
            head = ''
            ans = []
            for i, x in enumerate(s[:3]):
                head += x
                if int(head) > 255:
                    break
                for y in search(s[i + 1:], stages - 1):
                    mark = '.' if y else ''
                    ans.append(mark.join((head, y)))
                if i == 0 and int(x) == 0:
                    break
            return ans
        return search(s, 4)




# test = Solution()
# print(test.restoreIpAddresses(
#     "25525511135"
# ))

