print("Go from lbs to kgs (and vice versa) in a sec :) ")
peso = int(input("How much do you weight? "))
unidad = input("(L)bs or (K)gs: ")

if unidad.upper() == "L":
   conversion = peso * 0.45
   print(f"You weigh {conversion} kilograms")
else:
    conversion = peso / 0.45
    print(f"You weigh {conversion} pounds")