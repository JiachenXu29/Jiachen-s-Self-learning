# # # with open("students.csv") as file:
# # #     for line in file:
# # #         name, city = line.rstrip().split(",")
# # #         print(f"{name} is in {city}")

# # # now if we want to sort the answer

# # # import csv

# # # students = []

# # # with open("students.csv") as file:
# # #     reader = csv.DictReader(file)
# # #     for row in reader:
# # #         students.append({"name": row["name"], "home":row["home"]}) 


# # # for student in sorted(students, key=lambda student: student["name"]):  

# # #     print(f"{student['name']} is from  {student['home']}")  
# # ________

# # now we are going to write the data to the csv file

# import csv
# name = input("what is your name? ")
# home = input("where is your home? ")

# with open("students.csv", "a") as file:
#     writer = csv.DictWriter(file , fieldnames=["name","home"])
#     writer.writerow({"name":name, "home":home})


