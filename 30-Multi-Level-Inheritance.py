# Multi Level inheritance
class A:
    def feature1(self):
        print("i am feature 1")

    def feature2(self):
        print("i am feature 2")

class B(A):
    def feature3(self):
        print("i am feature 3")

class C(B):
    def feature4(self):
        print(("i am feature 4"))

firstClass= C()
firstClass.feature1()
firstClass.feature2()
firstClass.feature3()
firstClass.feature4()











