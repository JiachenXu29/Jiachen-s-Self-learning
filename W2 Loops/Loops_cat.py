
# i = float(input("insert the times you want to meow "))
# #i=3

# n = float (i - i + 1)

# while n <= i:
#     print("meow")
    
#     # n = n + 1
#     n += 1



# ______



# for i in [0.2,1,1,2]:
#     if i < 2 :
#         print("meow")
#     else:
#         print (list(range(223)))


# __----

# for _  in range (int(input ("how many times you want cat meow? "))):
    # print("meow")

#

# while True:
#     n = int(input("What's n? "))
#     # if n < 0:
#     #     print("Please insert a positive number: ")
#     #     continue
#     # else:
#     #     break

#     if n>0:
#         break
#     else:
#         print("please insert again: ")

# for _ in range (n):
#     print ("meow")


def main():
    # number = get_number()
    meow ( get_number() )

def get_number():
    while True:
        n = int(input("what is n? "))
        if n > 0:
            break
    return n


def meow (n):
    for _ in range (n):
        print ("meow")
        
main()
