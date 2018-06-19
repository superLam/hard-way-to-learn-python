# 文本编辑器
from sys import argv

# 这里输入的filename是等下写入文件的名字，不需要自己事先创建
script, filename = argv

print(f"We're going to erase {filename}.")
# ctrl+c 是退出脚本运行
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("what's your action? ")

# 用写入模式打开文件，如果文件不存在则会创建文件！
print("Opening the file...")
target = open(filename, 'w')

# 清除文件内容
# truncate表示截断，如果truncate(10)，表示只剩下前10个字符。
# write表示写入，应该是覆盖原文件。
# append表示追加，写在文件的末尾。
print("Truncating the file. Goodbye.") 
target.truncate()

print("Now I'm going to ask you for three lines.")

# 这里的\n代表是输入后的换行，不是文件上的换行
line1 = input("line 1: "+"\n")
line2 = input("line 2: "+"\n")
line3 = input("line 3: "+"\n")
back = "\n"
print("I'm going to write these to the file.")

# 写入文件
# 只用一个target.write()将line1-line3打印出来
target.write(line1+back+line2+back+line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print('And finally, we close it.')

# 关闭文件
target.close()

