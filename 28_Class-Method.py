# ক্লাসের ভিতরে ফাংশন তৈরি করা কে মেথড বলে 

class Student :
  studentRoll = ""
  studentGpa = ""
  
  def details (self,roll,gpa):
    self.studentRoll = roll  # self.studentRoll ব্যবহার করার কারন হল 
    self.studentGpa = gpa

  def display(self):
    print(f"Roll = {self.studentRoll}, Gpa = {self.studentGpa}")

rahim = Student()
rahim.details("101","3.70")
rahim.display()

 