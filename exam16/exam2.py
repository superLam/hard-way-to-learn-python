# 写一段与上个习题类似的脚本，使用read进行读取你写的内容。

from sys import argv

script, filename = argv

target = open(filename,'a')
line = '\ngood night'
target.write(line)
target.close()

# 这里需要先关闭file，然后重新打开file。
# 
target = open(filename,'r')
print(target.read())
target.close()


# read是读取文件内容，readline是读取文件中的一行
# 如果readline()写上数字5，会读取前5个字符，例如good morning，则good 。
# 通常情况下是使用readlines()，与read一样读取整个文件内容。
# readlines()自动将文件内容分析成一个行列表,该列表就可以用for..in..进行处理。


# 