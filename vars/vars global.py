abc = "awesome"

def myfunc():
  print("python is " + abc)

myfunc()


# if u use the global keyword, the var. belongs to the global scope
def myfunc2():
  global x
  x = "fantastic"

myfunc2()

print("Python is " + x)


# to change the value of a global variable inside a function, refer tothe var using the global kw
xyz = "cool"

def myfunc3():
  global x 
  x = "fantastic"

myfunc3()

print("python is " + xyz)
