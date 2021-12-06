# Constructor Method
class Student :
  studentRoll = ""
  studentGpa = ""
  
  def  __init__(self,roll,gpa):
    self.studentRoll = roll 
    self.studentGpa = gpa

  def display(self):
    print(f"Roll = {self.studentRoll}, Gpa = {self.studentGpa}") 

rahim = Student("101","3.70")
rahim.display()


