# print Patricia , Faith , Phionah and Annitah
names = ["Patricia", "Faith", "Phionah", "Annitah"]
print(names)

#add masha at the fourth position
names = ["Patricia", "Faith", "Phionah", "Annitah"]
names.insert(3, 'Masha')
print(names)

#update the name phiona Aladina
name=["patricia","Faith","Anitah","phiona"]
index=name.index('phiona')
name[index] = "phiona Aladina"
print(name)

#display the length of the student list
student=["patricia","Faith","Anitah","phiona Aladina"]
lenght=[len(student) for student in student]
print(lenght)

#print all the students name having updated using a four loop
studentName= ["patricia","Faith","Anitah","phiona Aladina"]
for name in studentName:
    print(studentName)

#calculate the total marks for the student marks variable and the answer is 304
studentMarks=[80,56,78,90]
totalMarks = sum(studentMarks)
print("Total marks:", totalMarks)