# print("#")
# print("#")
# print("#")

# def main ():
#     print_column(3)
 
# def print_column(height):
#     for _ in range (height):
#         print("#")

# main()

def main():
    print_square(3)

def print_square(size):
     # for each row in square
    for i in range (size):
        # for each brick in row
        for j in range (size):
            #print brick
            print("#", end="")
        
        #start a new line once finish a row
        print()


main()
