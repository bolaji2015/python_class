# from json import JSONEncoder
# import random as rd

# items = ["muideen", "ayomide", ["mariam", "ade"], "sola"]

# item = rd.choice(items)

# if isinstance(item, list):
#     name = rd.choice(item)
#     name = name.upper()
# else:
#     name = item.upper()

# print(name)

# # try:
# #     name = item.upper()
# # except AttributeError:
# #     name = rd.choice(item)
# #     name = name.upper()
# #     print(name)
# # else:
# #     print(name)

# # print(name)
# # print(type(name))
# import json
# print(dir(json))



# file = open("data.txt", mode="r")

# data = file.readlines()
# file.close()


with open("data.txt", mode="r") as file:
    data = file.readlines()

new_list = [name.rstrip("\n")  for name in data]

with open("letter.txt", mode="r") as obj:
    letter = obj.read()

for name in new_list:
    m_letter = letter.replace("[name]", name.title())
    with open(f"{name.lower()}.txt", mode="w") as new_letter:
        new_letter.write(m_letter)




