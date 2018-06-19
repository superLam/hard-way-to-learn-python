# 文字游戏

from sys import argv

script, user_name = argv
# 设置用户提示符
prompt = '\v '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask you a few question.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# 留意格式化工具！！
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. NOt sure where that is.
And you have a {computer} computer. Nice
"""
)