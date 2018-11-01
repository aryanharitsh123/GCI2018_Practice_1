y = str(input(" Name "))
print("Hello {}, please to meet you!".format(y))
def reverse(s): 
  str = ""
  for i in s: 
    str = i + str
  return str
  
s = y
print ("Did you know that your name backwards is {}?".format(reverse(s)))