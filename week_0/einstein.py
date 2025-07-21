# prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer

speed_of_light = 300000000 
mass = int(input("m: "))
energy = mass * (speed_of_light**2)
print("E: ", energy)
