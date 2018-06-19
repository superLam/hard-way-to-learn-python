# \t是TAB制表符，\\双斜杠代表\，第一个斜杠是转义序列，第二个斜杠是输出
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat"

# 三个单引号和三个双引号的作用是一样的，并且都可以在里面添加注释
# 但输出的时候还是会输出
fat_cat = '''
I'll do a list:
\t* Cat food #你好
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)