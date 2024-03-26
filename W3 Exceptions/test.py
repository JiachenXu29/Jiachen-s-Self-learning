def get_int():
    first_attempt = True
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            if first_attempt:
                print("x is not an integer. Please try again.")
                first_attempt = False
            # No else needed; just loop again silently

def main():
    x = get_int()
    condition = 1
    while condition <= x:
        print("12")
        condition += 1
    print(f"x is {x}")

main()
