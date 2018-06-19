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
# 关闭文件。如果没有缓冲，只有close()或者flush才会写入文件
txt_again.close()


# open（name，［，mode［，buffering］］）
# >>> f = open( ' myfile.txt ' , ' w ' , 1 )
#这时进入有缓冲的写模式
#>>> f.write( ' I love python! ' )
#这时在另一个终端查看时文件内容为空
#>>> f.close()
#这时再次查看，就可以看到 I love python！

#>>> f = open( ' myfile.txt ' , ' w ' , 0 )
#这时进入无缓冲的写模式
#>>> f.write( ' I love python! ' )
#这时在另一个终端用cat查看下文件内容，就可以查看到 I love python！