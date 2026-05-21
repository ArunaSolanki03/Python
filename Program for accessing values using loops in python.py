#print all the keys of a dictionary
student={"Name":"Kiran","Age":22,"Regno":562,"Branch":"CSE"}
for x in student:
    print(x)
#print all the values of a dictionary
print("Values are:")
for x in student:
    print(student[x])
#print all the keys and values of a dictionary
print("keys and values are:")
for x,y in student.items():
    print(x,y)