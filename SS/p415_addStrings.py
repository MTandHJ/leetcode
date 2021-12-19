
import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = ''
        while i >= 0 or j >= 0 or add != 0:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0
            result = x + y + add
            print('result', result)

            # if 
            if result // 10 > 0:
                ans += chr(ord('0') + result % 10)
                add = result // 10
            else:
                ans += str(result)
                add = 0
            print('ans', ans)
            # sys.exit()
            # add = result % 10 if res
            i -= 1
            j -= 1
        ans = ans[::-1]
        return ans

ins = Solution()
print(ins.addStrings('456', '77'))