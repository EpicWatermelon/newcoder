# -*- coding:utf-8 -*-
#str不能被直接替换

#解1：使用python内建方法append [O(1)]
#新建一个k，遇到空格append('%20')，其他情况添加原字符。
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        k = []
        for index,i in enumerate(s):
            if i == ' ':
                k.append('%20')
            else:
                k.append(i)
        #list->str
        return "".join(k)

#解2：在原str上修改，建立两个指针，遍历该str
