formatter = "{} {} {} {}"
# 格式化里面的内容，不允许少于formatter期望的参数（不知怎么说）
# 如果格式化内容多于formatter期望的参数，则格式化前面的几个（参数的数量）。
print(formatter.format(1, 2, 3, 4))
print("\n")
print(formatter.format("one" , "two" , "three" , "four"))
print("\n")
print(formatter.format(formatter, formatter, formatter, formatter))
print("\n")
lines = ("try your",
	"own text here",
	"maybe a poem",
	"or a song about fear")
# 如果lines前面没有* ， 则会报错
print(formatter.format(*lines))

print("\n")
# repr() 函数将对象转化为供解释器读取的形式。可以用来查找debug。
print(">>>>>>lines",repr(lines))
print("\n")
print(formatter.format(
    "try your",
	"own text here",
	"maybe a poem",
	"or a song about fear"
))