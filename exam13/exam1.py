# 运行程序时，需要依次输入4个参数  python exam1.py Lam Lamgor superLam
# 得到结果就是
# The script is called: exam1.py
# Your first variable is: Lam
# Your second variable is: Lamgor
# Your third variable is: superLam


from sys import argv
# argv进行解包（unpack），就是把argv中的东西取出来，解包，将所有参数依次赋值给左边的这些变量
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)