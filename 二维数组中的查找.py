class Solution:
    # array 二维列表
    #分而治之，从右上角或者左下角开始判断
    #不能从左上角或者右下角，无法排除整行or列
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        
        # from top right corner
        i = 0
        j = col - 1
        while i < row and j >= 0:
            if array[i][j] > target:
                j -= 1
            elif array[i][j] < target:
                i += 1
            else:
                return True
