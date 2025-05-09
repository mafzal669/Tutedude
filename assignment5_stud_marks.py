stud_marks= {"Afzal": 90, "Faisal": 75, "Neelu":85}
name = input("Enter Student's name: ")
if name in stud_marks:
    print("{}'s marks: {}".format(name, stud_marks[name]))
else:
    print("No Student found with name {}".format(name))