
# try:
#     marks = 10000
#     a = marks / 0
#     print(a)
# except Exception as e:
#     print("You Can Not Devide a number by 0 ",e)

# finally:
#     print("It Work's ")

try:
    marks = 10000
    a = marks / 0
    print(a)
except (ZeroDivisionError,TypeError,FileNotFoundError) :
    print("You Can Not Devide a number by 0 ")

finally:
    print("It Work's Successfully ")

