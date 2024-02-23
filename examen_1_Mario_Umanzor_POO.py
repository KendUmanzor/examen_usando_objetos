

estados=["urgente","normal", "familiar"]
paquetes=[]
""""MARIO FERNANDO UMANZOR SANDOVAL 20191003366"""

class crear_paquete:
    def __init__(self, peso, sucursal1, sucursal2, estado, precio, proceso="registrado"):
        self.peso=peso
        self.sucursal1=sucursal1
        self.sucursal2=sucursal2
        self.estado=estado
        self.precio=precio
        self.proceso=proceso
        
    def cambiar(self, estado_nuevo):
        self.proceso=estado_nuevo
        
    def __str__(self):
        return f"peso: {self.peso}, sucursal origen: {self.sucursal1}, sucursal destino: {self.sucursal2}, envio tipo: {self.estado}, total a pagar: {self.precio}, proceso del paquete: {self.proceso}"
    

def agregar():
    
    peso=input("ingrese el peso del paquete:  ")
    entero=int(peso)
    sucursal1=input("ingrese la sucursal de origen:  ")
    sucursal2=input("ingrese la sucursal de destino:  ")
    print("en que estado entra el paquete: ")
    print(estados)
    try:
        seleccion=int(input())
        if seleccion==1:
            estado="urgente"
            pagar=(entero*180)
        elif seleccion==2:
            estado="normal"
            pagar=(entero*80)
        elif seleccion==3:
            estado="familiar"
            pagar=(entero*40)
    except:
        print("ingrese una opcion valida, 1 para urgente, 2 para normal, 3 para familiar")
        
    paquete=crear_paquete(peso,sucursal1,sucursal2,estado,pagar)
    paquetes.append(paquete)

def mostrar():
    for i, paquete in enumerate(paquetes, start=1):
        print(f"paquete # {i}, {paquete}")


def cambiar_proceso():
    estado_nuevo=(input("ingrese el estado nuevo del paquete registrado, enviado, recibido "))
    peso=input("ingrese el peso del paquete para buscarlo")
    
    for i, paquete in enumerate(paquetes,start=1):
        if peso==paquete.peso:
            paquete.cambiar(estado_nuevo)

def remove():
    peso=input("ingrese el peso del paquete para buscarlo")
    for i,paquete in enumerate(paquetes, start=1):
        if peso==paquete.peso:
                paquetes.remove(paquete)

seguir=True
while seguir:
    try:
        print("---------menu--------")
        print("1. agregar paquetes")
        print("2. mostrar todos los paquetes")
        print("3. borrar un paquete")
        print("4. cambiarle el estado a un paquete")
        print("5. salir")
        
        opcion=int(input("ingrese una opcion:   "))
        match opcion:
            case 1:
                agregar()
            case 2:
                mostrar()
            case 3:
                remove()
            case 4:
                cambiar_proceso()
            case 5:
                seguir=False
    except:
        print("error ingrese una opcion valida")
