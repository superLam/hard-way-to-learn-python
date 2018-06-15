# 章节格式如下。
# what = XXX
# print(f"what")
# 以后打印的时候就可以不必print('what ',what),可以直接print(f'what {what}')

# 进行浮点数的四舍五入。round(1.7333)=2

name = 'superLam'
age = 23
height = 175
weight = 58
eyes = 'Black'
teeth = 'White'
hair ='Black' 


print(f"Let's talk about {name}.")
print(f"He's {height} centimetres tall.")
print(f"He's {weight} kilo heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")


total = age + height + weight
print(f"If i add {age} , {height} , and {weight} I get {total}.")


print('\n'*3) #空行3行
#试着使用变量将厘米和千克转换成米和斤。不要直接键入答案，使用python的数学计算功能来完成。



name = 'superLam'
age = 23  #years
height = 175 #metres
weight = 58  #kilo
eyes = 'Black'
teeth = 'White'
hair ='Black' 


print(f"Let's talk about {name}.")
print(f"He's {height / 100} metres tall.")
print(f"He's {weight * 2} halfkilo heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")


total = age + height + weight
print(f"If i add {age} , {height / 100} , and {weight * 2} I get {total}.")