def CalculatingArea(a, b): # Area retangular = floorXwall
    area = a * b
    print(f'The Area of {a}m X {b}m results in {area}m²')

#main program
print("Let's calcualting the area\n")
base = float(input("Input the ground's value (m): "))
tall = float(input("Now I want the height value (m): "))  
CalculatingArea(base, tall)
