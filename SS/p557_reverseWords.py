#### 反转字符串中的单词Ⅲ ####

from typing import List


### Mine: #####

class Solution:
    # 切分成列表
    # 在列表中逆序
    # 连接数组
    def reverseWords(self, s:str) -> str:
        li = s.split(' ')
        return ' '.join(self.re_word(word) for word in li)
    
    def re_word(self, word:str) -> str:
        new = list(word)
        # new.reverse()
        i, j = 0, len(new) -1
        while i <= j:
            new[i], new[j] = new[j], new[i]
            i += 1
            j -= 1
        
        return ''.join(new)

if __name__ == '__main__':
    ins = Solution()
    s = "Let's take LeetCode contest"
    print(ins.reverseWords(s))

class Solution:
    # 新建一个数组
    # 往其中，按照原来逆序添加元素
    def reverseWords(self, s:str) -> str:
        ret = []
        length = len(s)
        i = 0
        while i < len(s):
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1
            
            for p in range(start, i):
                ret.append(s[start + i - 1 - p])
            
            while i < len(s) and s[i] == ' ':
                i += 1
                ret.append(' ')
        return ''.join(ret)

if __name__ == '__main__':
    ins = Solution()
    s = "Let's take LeetCode contest"
    print(ins.reverseWords(s))