

class Productos:
    def __init__(self,name,descr):
        self.name=name
        self.descr=descr
        print(f"Producto {name} Creado!")
    
    def llamar(self):
        print(self.descr)
num=int(input("¿Cuantos productos ingresará?"))
if num<=0:
    print("Debe ingresar un número mayor a 0!")
else :
    while num >0:
        nom=input("Ingrese el nombre del producto: ")
        dscr=input("Ingrese la descripcion del producto: ")
        Productos(nom,dscr)
        num=num-1
    continuacion = input("Si desea ver la descripcion de un producto ingrese su nombres, si no ingrese 'no' ")
    if continuacion != 'no':
        
    else:  
        print("Gracias!")
