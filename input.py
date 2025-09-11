# #BMI = 体重 / ( 身高 ** 2 )
# Weight = input("Please input your Weight(Kg): ")
# High = input("Please input your Height(m): ")
# BMI = float(Weight) / (float(High) ** 2)
# print("Your BMI is " + str(BMI))
# #___________________________________________________

# a = input("Please input your emotion factor(1-10): ")
# if float(a) >= 8.0:
#     print("You have a good day")
# else:
#     if float(a) >= 5.0:
#         print("You have a normal day")
#     else:
#         print("Cheer up")
# #——————————————————————————————————————————————————————

# Housework = int(input("How many times you do housework this weekend: "))
# Bag = int(input("How mang bags do you buy for Yun: "))
# if 3 < Housework <=10 and Bag >=2:
#     print("You are good!")
# else:
#     print("Go on……")
# #_______________________________________________________

# list = ["你好", 'Hello', None]
# print(list)
# list.append(True)
# print(list)
# list.append(66.6)
# print(list)
# list[1] = "bonyage"
# print(list)
# #_____________________________________________________________

# member = {("宋云",22):173, ("齐迪",24):176, ("石丹芙",21):156}
# member[("照青",22)] = 177
# print(member[("宋云",22)])
# s = input("请输入群聊成员姓名和年龄：").strip()
# if "," in s:
#     name, age = s.split(",")
# else:
#     name, age = s.split()
# try:
#     age = int(age)
#     name = str(name)
#     key = (name.strip(),age)
#     if key in member:
#         print("您查询的成员" + name + "身高如下")
#         print(member[key])
#     else:
#         print("该成员不属于该群聊")
# except ValueError:
#     print("输入的年龄应当是整数")
# #________________________________________________________________
#
# tempurature = {"a":36.2, "b":37.1, "c":36.4, "d":38.1}
# tempurature["e"] = 39.2
# for name,Tem in tempurature.items():
#     if Tem >= 37.0:
#         print(name + "你发烧了")
#     else:
#         print(name + "你的体温正常")
# #___________________________________________________________________

# list1 = ["ni", "hao", "ma", "?"]
# for char in list1:
#     print(char)
# #___________________________________________________________________

sum = 0
i = 0
user_input = input("请输入需要求和的数字，输入完毕按q即可返回平均值")
while user_input != "q":
    sum = sum + float(user_input)
    user_input = input("go on")
    i = i + 1
print(sum/i)