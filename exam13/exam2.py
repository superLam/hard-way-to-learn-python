from sys import argv

code_name , human_name1, human_name2 = argv

age1 = input("How old are {}? ".format(human_name1))
height1 = input("How tall are {}? ".format(human_name1))
weight1 = input("How much do {} heavy? ".format(human_name1))

age2 = input("How old are {}? ".format(human_name2))
height2 = input("How tall are {}? ".format(human_name2))
weight2 = input("How much do you {} heavy? ".format(human_name2))

print("So {} is {} old, {} tall and {} heavy".format(human_name1, age1, height1, weight1))
print("So {} is {} old, {} tall and {} heavy".format(human_name2, age2, height2, weight2))