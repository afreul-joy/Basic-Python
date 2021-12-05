# student নামক একটি ক্লাস ক্রিয়েট করা হয়েছে ,এবং ক্লাসের কিছু প্রপার্টি যেমন : Roll,GPA 
#  এখন এই student ক্লাস সকলেই ব্যবহার করতে পারবে,

# Rahim,Karim,Rabeya এই অব্জেক্ট এগুলা ক্লাস কে এক্সেস করতে পারবে 

# অতএব ক্লাস একটি টেমপ্লেট/মেইনকপি এটি কে যতবার ইচ্ছা ফটোকপি করে পারবো 

class Student :
  roll = ""
  gpa = ""

rahim = Student()
rahim.roll = 101
rahim.gpa = 3.75

print(f"Roll = {rahim.roll}, Gpa = {rahim.gpa}")

karim = Student()
karim.roll = 102
karim.gpa = "3.80"

print(f"Roll = {karim.roll}, Gpa = {karim.gpa}")



   