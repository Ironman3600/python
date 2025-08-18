try:
  marks = {'uday': '80','kumar': '96','sunny':'83'}
  user = str(input("Enter the student's name: "))
  print(f"{user}'s marks: {marks[user]}")
except:
 print("Student not found.")
