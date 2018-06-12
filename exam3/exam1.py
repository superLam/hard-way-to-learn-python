# --coding=utf-8--

#1. 使用 # 在代码每一行的前一行为自己写一个注解，说明一下这一行的作用。
#4. 有没有发现计算结果是”错”的呢？计算结果只有整数，没有小数部分。研究一下这是为什么，搜索一下“浮点数(floating point number)”是什么东西。
#5. 使用浮点数重写一遍 ex3.py，让它的计算结果更准确

#计算鸡的数量
print('i will now count my chickens: ')
print('Hens ', 25 + 30 / 6)
print('Roosters ', 100 - 25 * 3 % 4 )

#计算蛋的数量
print('Now i will count the eggs: ')
#即使设置成保留两位小数，可是还是会四舍五入，结果是7；可是当1/4修改成1.0/4的时候，结果就会是6.75
print('%.2f' %(3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6))  
print('is it true that 3 + 2 < 5 - 7 ?')
print(3 + 2 < 5 - 7)

#当print的内容不是全部在引号里面，输出时就会出现括号。
print('what is 3 + 2 ? ', 3 + 2)
print('what is 5 - 7 ? ', 5 - 7)
print("Oh, that's why it's False.")
print('How about some more.')

#这里会直接判断true或者false。
print('Is it greater ? ' , 5 > -2 )
print('Is it greater or equal?' , 5 >= -2)
print('Is it less or equal?', 5 <= -2)
