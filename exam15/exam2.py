# 只用input写这个脚本
# 读取文件

filename = input("Where's your file: ")

txt = open(filename)

print(txt.read())

