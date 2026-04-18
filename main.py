# print("Student Information")
# print("--------------------")

# file = open("student_information.txt", "r")

# str(input)

# def record_add():

# def record_overwrite():

# update = str(input("Would you like to update the record? Y/N: "))

# if update == "Y":
#     record_update()
# if update == "N":
# else:



{1, "mia", "artist"}

studentinfo = "studentinfo.txt"

def add_student():
    roll = input("Enter roll number")
    name = 
    intro = 
    with open (studentinfo, "a") as f:
        f.write(f"{roll}, {name}, {intro}\n")
    print("Student added")

def update_intro():
    update_roll = input("Enter a roll number to update: ")
    updated = False
    with open(studentinfo, "r") as f:
        lines = f.readlines()
    with open(studentinfo, "w") as f:
        for line in line:
            parts = line.split(",")
            if len(parts)!=3
                continue #basically a pass statement and goes to the next statement
            roll, name, intro = parts
            if roll == update_roll
                new_intro = input("Enter a new intro: ")
                f.write(f"{roll}, {name}, {intro}\n")
            else:
                f.write(line)   #accounts for when an entered roll number does not math any preexisting ones
    if updated:
        print("intro updated")
    else:
        print("not found")