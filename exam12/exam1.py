# input里面的“”可以理解为print，就是说等于
# print("What")
# age = input()
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh ")

# 两个得到的结果是一致。
print(f"So, you're {age} old , {height} tall and {weight} heavy.")
print("So, you're {} old, {} tall and {} heavy.".format(age, height, weight))