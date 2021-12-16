
num1 = 10
num2 = 20
num3 = 30

if num1 > num2 and num1 > num3:  # and এভাবে লিখে দিতে হবে 
    print(num1) 
elif num2>num1 and num2 >num3:
    print(num2)
else:
    print(num3)


user = input("Enter A Text :")

# or লিখতে গেলে == ব্যবহার করতে হবে
if(user=='a' or user=='e' or user=='i' or user =='u'):  
    print("Vawel")
else:
    print("Consonent")


     