class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber:
            a = columnNumber%26
            if a == 0:
                s += 'Z'
                columnNumber = columnNumber//26-1
            else:
                s += chr(a+64)
                columnNumber //= 26
        return s[::-1]

if __name__=='__main__':
    obj = Solution()
    print(obj.convertToTitle(52))