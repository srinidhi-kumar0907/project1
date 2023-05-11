1.#CODE
PI = 3.14
r = float(input("The radius of a circle:"))
area = PI *(r*r)
print("The area of the circle with radius is:",area)

#OUTPUT
The radius of a circle:1.1
The area of the circle with radius is:3.799400000000008
  
  
  2.#CODE
  filename = input("Input the Filename: ")
file_extns = filename.split(".")
print ("The extension of the file is : " + repr(file_extns[-1]))

#OUTPUT
Input the Filename:abc.py
  The extension of the file is :'py'
