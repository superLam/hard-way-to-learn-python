days = "Mon Tue Wed Thu Fri Sat Sun"
# \是转置符号。\n是换行符。如果中间需要加上“”，那么在双引号前需要\"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ",days)
print("Here are the months: ",months)

# 在三个双引号“”“内，输入的所有字符都会以原本形式输出，无论里面有多少个单引号，双引号。
# 在它们里面，如果不是顶格，那么输出的时候也会出现空格。
print("""
There's something going on here.
With the three double-qutes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")