# এ প্রতিটা element এর জন্য একটি condition দিবো যদি শর্ত match হয় তাহলে ঐ element টাকে দিবে একটি array এর মাধ্যমে return করে দিবে
#  যদি element না পাই তাহলে []empty array দিবে

num = [1,2,3,4,5,6,7,9,10]

def bigNum (x):
  if(x>=5):
    return x

result = list(filter(bigNum,num))
# print(result)

''' 
python এ map & filter ২টি পারামিটার রিসিভ করে (ফাংশন এবং লিস্ট/এরে)  
map()
filter()

'''

num = [1,2,3,4,5,7,8,9,10,11,12,13,14,15]

def arr(x):
  if x % 2==0 and x % 5 ==0:
    return x
  

evn = list(filter(arr,num))
print(evn)