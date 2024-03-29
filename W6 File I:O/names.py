# names = []

# for _ in range(3):
#     name = input("what is your name? ")
#     names.append(name)

# for name in sorted(names):
#     print(f"hello,{name}")
# ______

# name = input("what is your name? ")


# # with open("name.txt", "a") as file:
# #     file.write(f"{name}\n") 

# ____ 
# with open ("name.txt", "r") as file:        
#     for line in file:
#         print("hello,", line.rstrip()) 
# _______
# # start to sort the answer

# names=[]
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello,{name}")
# _____________

# with open("names.txt") as file:
#     for line in sorted(file):
#         print("hello,", line.rstrip()) 

# ----------
names=[]
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello,{name}")