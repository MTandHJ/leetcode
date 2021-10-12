


class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                combinations.append(''.join(combination))
            else:
                # 当前是哪个数字
                digit = digits[index]
                # 这个数字对应的字母
                for letter in phoneMap[digit]:
                    # 添加这个数字
                    combination.append(letter)
                    backtrack(index+1)
                    # 做回溯，删除这个数字
                    combination.pop()
        
        combination = []
        combinations = []
        backtrack(0)
        return combinations