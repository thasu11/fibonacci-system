 
a = 0
i = 1
print ("1,  find a no. on a perticullar place")
print ("2,  find place on which the no. is")
g = input("enter the no. of the operation you want to perform: ")
if g == "1":
  place = int(input("which positioned no. do you want in fibonacci system:"))

  for f in range(place - 2):
    c=a+i
    a=i
    i=c

  print(c)
  



elif g == "2":
  num = int(input("which no. do you want to find the position of:"))
  c = a  # Initialize c with the value of a
  position = 2  # Initialize position counter
  while c < num:
    c = a + i
    a = i
    i = c
    position += 1
  if c == num:
    print(f"The position of {num} in the Fibonacci sequence is {position}")
  else:
    print(f"{num} is not found in the Fibonacci sequence")
