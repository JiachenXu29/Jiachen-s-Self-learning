# print("hello, world")



# except SyntaxError:
#      print("braces have been completed")


def get_int(assprompt):
    while True:
        try:
            x =int( input(assprompt))
            return x 
        except ValueError: 
            pass



def main():
    x= get_int("what is x?")
    condition =1 
    while condition <= x:
        print("12")
        condition += 1
    print(f"x is {x}")

main()