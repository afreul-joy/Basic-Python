# super ক্লাসে যদি constructor মেথড সেটাও এক্সেস করতে পারবে sub class 

# class A:        
#     def __init__(self):
#         print("in A init")

#     def feature1(self):
#         print("i am feature 1")

#     def feature2(self):
#         print("i am feature 2") 

# class B(A):     # B এর যদি constructor/init মেথড না থাকে তখনি A এর init মেথড B ব্যবহার করবে   
#     def feature3(self):
#         print("i am feature 3")

# object1= B()

# ------------------Another Situation--------------------  

# কিন্তু যদি B এর constructor/init মেথড থাকে তাহলে সে তার টাই ব্যবহার করবে 

# class A:        
#     def __init__(self):
#         print("in A init")

#     def feature1(self):
#         print("i am feature 1")

#     def feature2(self):
#         print("i am feature 2") 

# class B(A):    
#      def __init__(self):        # B এখন তার নিজের constructor/init ব্যবহার করবে 
#         print("in B init")  

#      def feature3(self):
#         print("i am feature 3")

# object1= B()

# ------------------Another Situation--------------------  

# কিন্তু যদি আমি চাই A এবং B ২টারই construtor/init মেথড ব্যবহার করতে তাহলে super().__init__() দিতে হবে 
# super কিওয়ার্ড এর মাধ্যমে parent ক্লাসের সব প্রাপারটি child পেয়ে যাবে 

class A:        
    def __init__(self):         # Method Overriding
        print("in A init")

    def feature1(self):
        print("i am feature 1")

    def feature2(self):
        print("i am feature 2") 

class B(A):    
     def __init__(self):        
        super().__init__()      # A এর init মেথড পেয়ে যাবে B
        print("in B init")  

     def feature3(self):
        print("i am feature 3")

object1= B()

