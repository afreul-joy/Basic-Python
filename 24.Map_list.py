# map() করলে সব সময় array/list পাবো 
# map() এর কাজ 3টি :
	# 1. প্রত্যেকটা element কে loop করবে 
	# 2. তারজন্য কোন একটি function apply করবে 
	# 3. তারপর সেই function এ যেই result গুলো পাবে সেটা array/list এর মাঝ রাখবে

def square (x):
  return x*x

num = [1,2,3,4,5]

result = list(map(square,num))   
print(result) 



