# 定义type_of_people
type_of_people = 10
# 把type_of_people 放在另一个定义x上
x = f"There are {type_of_people} types of people"

# 定义binary和do_not
binary = "binary"
do_not = "don't"
# 把binary和do_not放在定义y上
y = f"Those who know {binary} and those who {do_not}."

# 打印x,y
print(x)
print(y)

# 打印
print(f"i said: {x}")
print(f"i also said: {y}")


hilarious = False
# {}是给format留的？当我写下面代码时，输出是一样的。
# 可能这里是展示.format函数的用法吧？！
# joke_evaluation = "Isn't that joke so funny?"
# print(joke_evaluation,hilarious)

joke_evaluation = "Isn't that joke so funny? {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of.."
e = "a string with a right side."
# w和e分别都赋值了字符串，所以显示的是w和（+）e的字符串
print(w + e)