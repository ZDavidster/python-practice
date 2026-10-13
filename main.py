name = input("enter your name")
age = int(input("Enter your age: "))

if age > 18:
  status = "adult"
else:
      status = "a "+" minor "

print("hello " + name + ", you "+ "are" +" " + "a" + status + " ")