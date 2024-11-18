def calculate_force():
    mass=float(input("Enter the Maass:"))
    acceleration=float(input("Acceleration:"))
    force=mass*acceleration
    print(force)

def calculate_first_linear_equation():

    U= float(input("Enter the value of u= initial velocity:"))
    T= float(input("Enter the the value of time :"))
    A= float(input("Enter a= acceleration:"))
    final_vleocity=U+A*T
    print(final_vleocity)

def calculate_second_linear_equation():

    U= float(input("Enter the value of u= initial velocity:"))
    T= float(input("Enter the the value of time :"))
    A= float(input("Enter a= acceleration:"))
    distance=U*T+0.5*A*T**2
    print(distance)

def calculate_third_linear_equation():
    
    U= float(input("Enter the value of u= initial velocity:"))
    S= float(input("Enter the the value of distance :"))
    A= float(input("Enter a= acceleration:"))
    V=(U**2+2*A*S)**0.5
    print(V)

def calculate_potential_difference():
    i=float(input("Enter the value of current =I:"))
    r=float(input("Enter the value of resistor=R:"))
    v=r*i
    print(v)

print ("welcome to physics class")
print ("You have 5 choices to calculate your problems")
print("1. is for Force")
print("2. is for first linear equation")
print("3. is for second linear equation")
print ("4.third linear equation")
print ("5.calculate potential differnce")
Number=float(input("Choose from 1-5 to calculate problems:" ))

if Number ==1:
   calculate_force() 
if Number==2:
    calculate_first_linear_equation()
if Number==3:
    calculate_second_linear_equation()
if Number==4:
   calculate_third_linear_equation()
if Number==5:
   calculate_potential_difference()
