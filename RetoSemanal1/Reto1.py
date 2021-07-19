
import time
name=input("Ingrese su nombre: ")
age=int(input("Ingrese su edad: "))
hour=int(time.strftime("%H"))
if age>=18:
    print(f"No tienes ninguna responsabilidad {name}!")
else:
    if hour>6:
        print(f"{name} debes ir a dormir!")
    else:
        print(f"{name} debes hacer tus tareas!")
