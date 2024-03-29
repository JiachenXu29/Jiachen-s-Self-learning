import re

email = input ("What is your email? ").strip()

print(email)

if re.search(r"^(\w|\s|-|\.)+@(\w+\.)?\w+\.(edu|com|gov|org)$", email, re.IGNORECASE):
    print("Vaild")
else:
    print("Invaild")
