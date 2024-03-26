x = int(input("what's x? "))
y = int(input("what's y? "))

#using_if,elif and else
def compare():
    if x<y :
        print("x is less than y")
    elif x>y:
        print("x is greater than y")
    # elif x==y:
    #     print("x is equal to y")
    else:
        print("x is equal to y")

#using_or
def compare2():
    # if x<y or x>y:
    if x != y:
        print("x is not equal to y")
    else:
        print("x is equal to y")

compare2()