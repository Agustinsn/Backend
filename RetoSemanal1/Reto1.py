
import time
name=input("Ingrese su nombre: ")
age=int(input("Ingrese su edad: "))
hour=int(time.strftime("%H"))
print(hour)
if age>=18:
    print(f"No tienes ninguna responsabilidad {name}!")
else:
    if hour>17:
        print(f"{name} debes ir a dormir!")
    else:
        print(f"{name} debes hacer tus tareas!")
