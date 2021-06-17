class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_li = s.split()
        s_li.reverse()
        return ' '.join(s_li)