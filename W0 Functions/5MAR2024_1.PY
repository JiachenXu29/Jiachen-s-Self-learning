# Ask user for their name and and Remove whitespace from str and capitalize user's name
name = input("what is your name? ").strip().title()
   
#Split user's name into first name and last name
# jason xu
firstname, lastname = name  .split(" ")

# Say hello to user
print(f"hello, {firstname}")
