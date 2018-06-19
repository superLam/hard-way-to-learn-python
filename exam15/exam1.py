# 从sys模块里面导入argv
from sys import argv

# 依次输入参数并赋值
script, filename = argv

# 这里open返回的是一个file对象，而不是file内容；read返回的才是file内容。
txt = open(filename)

print(f"Here's your file {filename}: ")
# read返回是file内容
print(txt.read())
txt.close()
# 用input读取获取文件名称
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
# 关闭文件
txt_again.close()
