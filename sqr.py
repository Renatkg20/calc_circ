#calculation fo the area of the compile
def circul_area(r):
  p = 3.14
  a = p*(r**2)
  return f"Area of circul equal {a}"

def sqr_area(a):
  S = a**2
  return f"Area of square equal {S}"


def rect_area(a, b):
  S = a * b
  return f"Area of rectangle equal {S}"


user_input = input("Pls choose what do u want to calculate ?  1 = circul, 2 = square, 3 = rectangle \n")
if user_input == "1":
  val = int(input("Please enter the radius of circul = "))
  print(circul_area(val))
elif user_input == "2":
  val1 = int(input("Please enter the side of the square = "))
  print(sqr_area(val1))
elif user_input == "3":
  val2 = int(input("Please enter the a of the rectangle = "))
  val3 = int(input("Please enter the b side of the rectangle = "))
  print(rect_area(val2, val3))


