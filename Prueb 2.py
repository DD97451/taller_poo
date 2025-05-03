import random
import os
import time
from time import sleep

def tuerca_lateral_animada(frame):
    tuerca_frames = [
        "    _____\n   /       \\\n  |   o o   |\n   \\_______/",
        "    _____\n   /   o   \\\n  |    o    |\n   \\_______/",
        "    _____\n   /    o  \\\n  |   o     |\n   \\_______/",
        "    _____\n   /   o   \\\n  |     o   |\n   \\_______/",
    ]
    return tuerca_frames[frame % len(tuerca_frames)]
h

def tractor_reparacion(frame):
    tuerca = tuerca_lateral_animada(frame)
    return f"""{tuerca}

        ______
  ____|__|__\\___
 |   _   ___   `|
/|__|_|_|___|___|
( o )         ( o )

     🔧 EN REPARACIÓN 🔧"""

def tractor_podadora_reparacion(frame):
    base = tractor_reparacion(frame)
    return base.replace("EN REPARACIÓN", "EN REPARACIÓN (podadora)")


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def tractor_fumigador_reparacion(frame):
    base = tractor_reparacion(frame)
    return base.replace("EN REPARACIÓN", "EN REPARACIÓN (fumigador)")
def mover_tractor(objeto1,objeto2,objeto3):

    # ---------------- TRACTOR NORMAL ----------------

    def tractor_funcionando(pos):
        espacio = " " * pos
        return f"""{espacio}        ______
    {espacio}   ____|__|__\\___
    {espacio}  |    _   ___   `|
    {espacio} /|___|_|_|___|___|
    {espacio}( o )         ( o )  →→→ Arando..."""

    def tractor_funcionando_reversa(pos):
        espacio = " " * pos
        return f"""{espacio}  ______        
    {espacio}___/__/__|__|____   
    {espacio}|`   ___   _    |  
    {espacio}|___|___|_|_|_|\\|
    {espacio}( o )         ( o )  ←←← Arando..."""

    def tractor_estatico_exitoso():
        return """        ______
       ____|__|__\\___
      |    _   ___   `|
     /|___|_|_|___|___|
    ( o )         ( o )  
    Terminó de arar exitosamente ✅"""

    def tractor_danado(frame):
        humo_frames = [
            ["     (  )", "    (    )", "   (      )"],
            ["    (    )", "   (      )", "     (  )"],
            ["   (      )", "     (  )", "    (    )"],
        ]
        humo = humo_frames[frame % len(humo_frames)]
        return f"""{humo[0]}
    {humo[1]}
    {humo[2]}
            ______
      ____|__|__\\___        
     |   _  x  ___  `|     
    /|__|_|_|___|___|     
    ( x )         (   )     ¡FALLÓ!"""

    # ---------------- TRACTOR PODADORA ----------------

    def tractor_podadora_funcionando(pos):
        espacio = " " * pos
        return f"""{espacio}        ______
    {espacio}   ____|__|__\\___
    {espacio}  |    _   ___   `|_________
    {espacio} /|___|_|_|___|___|#######|
    {espacio}( o )         ( o )   →→→ cortando..."""

    def tractor_podadora_funcionando_reversa(pos):
        espacio = " " * pos
        return f"""{espacio}              ______
    {espacio}          ___//__|__|___
    {espacio} _________|`  ___   _    |
    {espacio} |#######|___|___|_|_|___\\|
    {espacio}         ( o )         ( o )   ←←←  cortando..."""

    def tractor_podadora_estatico_exitoso():
        return """        ______
       ____|__|__\\___
      |    _   ___   `|_________
     /|___|_|_|___|___|#######|
    ( o )         ( o )  
    Terminó el corte exitosamente ✅"""

    def tractor_podadora_danado(frame):
        humo = tractor_danado(frame).split("\n")[:3]
        return f"""{humo[0]}
    {humo[1]}
    {humo[2]}
            ______
      ____|__|__\\___        
     |   _  x  ___  `|_________
    /|___|_|_|___|___|#######|
    ( x )         (   )     ¡FALLÓ cortando!"""

    # ---------------- TRACTOR FUMIGADOR ----------------

    def tractor_fumigador_funcionando(pos):
        espacio = " " * pos
        return f"""{espacio}        ______
    {espacio}   ____|__|__\\___
    {espacio}  |    _   ___   `|─────╭
    {espacio} /|___|_|_|___|___|     ╰═💨
    {espacio}( o )         ( o )   →→→ fumigando..."""

    def tractor_fumigador_funcionando_reversa(pos):
        espacio = " " * pos
        return f"""{espacio}              ______
    {espacio}          ___//__|__|___
    {espacio}     ╭───|`  ___   _    |
    {espacio} 💨═╯   |___|___|_|_|___\\|
    {espacio}         ( o )         ( o )   ←←←  fumigando..."""

    def tractor_fumigador_estatico_exitoso():
        return """        ______
       ____|__|__\\___
      |    _   ___   `|─────╭
     /|___|_|_|___|___|     ╰═💨
    ( o )         ( o )  
    Terminó de fumigar exitosamente ✅"""

    def tractor_fumigador_danado(frame):
        humo = tractor_danado(frame).split("\n")[:3]
        return f"""{humo[0]}
    {humo[1]}
    {humo[2]}
            ______
      ____|__|__\\___        
     |   _  x  ___  `|─────╭
    /|___|_|_|___|___|     ╰═💨
    ( x )         (   )     ¡FALLÓ fumigando!"""

    # ---------------- MOVIMIENTO ----------------
    for l in [objeto1,objeto2,objeto3]:
        if isinstance(l,Tractor):
            funcionando1 = tractor_funcionando
            reversa1 = tractor_funcionando_reversa
            exito1 = tractor_estatico_exitoso
            fallo1 = tractor_danado
        elif isinstance(l,Fumigador):
            funcionando2 = tractor_fumigador_funcionando
            reversa2 = tractor_fumigador_funcionando_reversa
            exito2 = tractor_fumigador_estatico_exitoso
            fallo2 = tractor_fumigador_danado
        elif isinstance(l,Cosechador):
            funcionando3 = tractor_podadora_funcionando
            reversa3 = tractor_podadora_funcionando_reversa
            exito3 = tractor_podadora_estatico_exitoso
            fallo3 = tractor_podadora_danado
    for i in range(0, 40, 2):
        limpiar()
        print(funcionando1(i))
        print(funcionando2(i))
        print(funcionando3(i))
        time.sleep(0.1)
    time.sleep(0.5)
    for i in range(40, -1, -2):
        limpiar()
        print(reversa1(i))
        print(reversa2(i))
        print(reversa3(i))
        time.sleep(0.1)
    time.sleep(0.5)
    limpiar()
    objeto1.trabajar()
    objeto2.trabajar()
    objeto3.trabajar()
    if [objeto1.mantenimiento,objeto2.mantenimiento,objeto3.mantenimiento]==[0,0,0] :
        for i in range(6):
            limpiar()
            print(fallo1(i))
            print(fallo2(i))
            print(fallo3(i))
            time.sleep(0.5)
    else:
        for i in range(6):
            limpiar()
            if objeto1.mantenimiento==0:
                print(fallo1(i))
            else:
                print(exito1())
            if objeto2.mantenimiento==0:
                print(fallo2(i))
            else:
                print(exito2())
            if objeto3.mantenimiento==0:
                print(fallo3(i))
            else:
                print(exito3())
            time.sleep(0.5)

def azar(multiplicador):
    eleccion=random.randrange(0,2)
    if eleccion ==1:
        return True
    else:
        return False


class Maquinaria:
    def __init__(self,num_serial, tank_fuel, mantenimiento, en_uso=True):#la hora de mantenimiento es el tiempo de uso antes de un mantenimiento
        self._num_serial=num_serial
        self._tank_fuel=tank_fuel
        self.mantenimiento=mantenimiento#las horas de cada cuanto se hace el mantenimiento
        self._mantenimiento_privado = mantenimiento#las horas de referencia
        self.en_uso=en_uso
    def get_info(self):
        print(self._tank_fuel, self.mantenimiento, self.en_uso)
    def get_mantenimiento(self):
        return self._mantenimiento_privado
    def activar_desactivar(self):
        self.en_uso= not self.en_uso


class Tractor(Maquinaria):
    def __init__(self,num_serial, tank_fuel, mantenimiento, en_uso=True):
        super().__init__(num_serial,tank_fuel, mantenimiento, en_uso)
    def trabajar(self):
        tiempo_restante=self.mantenimiento
        result=azar(self.mantenimiento)
        if not result:
            tiempo_restado=random.randrange(0,tiempo_restante+1)
            self.mantenimiento = self.mantenimiento - tiempo_restado
        return result


class Fumigador(Maquinaria):
    def __init__(self, num_serial,tank_fuel, mantenimiento, en_uso=True):
        super().__init__(num_serial,tank_fuel, mantenimiento, en_uso)
    def trabajar(self):
        tiempo_restante=self.mantenimiento
        result=azar(self.mantenimiento)
        if not result:
            tiempo_restado=random.randrange(0,tiempo_restante+1)
            self.mantenimiento = self.mantenimiento - tiempo_restado
        return result


class Cosechador(Maquinaria):
    def __init__(self,num_serial, tank_fuel, mantenimiento, en_uso=True):
        super().__init__(num_serial,tank_fuel, mantenimiento, en_uso)

    def trabajar(self):
        tiempo_restante=self.mantenimiento
        result=azar(self.mantenimiento)
        if not result:
            tiempo_restado=random.randrange(0,tiempo_restante+1)
            self.mantenimiento = self.mantenimiento - tiempo_restado
        return result


class Serviciotecnico:
    def __init__(self,nombre,identificacion,maquinaria,laborando=True):
        self._nombre=nombre
        self._identificacion=identificacion
        self._maquinaria=maquinaria
        self._laborando=laborando
    def cambiar_estado(self):
        self._laborando=not self._laborando

def seleccionar_tecnico(tipo):
    for i in lista_tecnicos:
        if i._maquinaria==tipo:
            if i._laborando==False:
                print(f"No hay tecnicos disponibles para el tipo {tipo}")
                return None
            else:
                return i

class Mantenimiento(): 
    @staticmethod
    def iniciar_mantenimiento(maquina):
        if isinstance(maquina,Cosechador):
            tipo="Cosechador"
        elif isinstance(maquina,Fumigador):
            tipo="Fumigador"
        elif isinstance(maquina,Tractor):
            tipo="Tractor"
        else:
            print("hay un error")
        
        if maquina.mantenimiento==0:
            print(f"El tiempo de mantenimiento optimo para el {tipo} {maquina._num_serial} ha caducado, intente hacer reparación")
            pass
        else:
            tecnico=seleccionar_tecnico(tipo)
            if tecnico!=None:
                tecnico.cambiar_estado()
                maquina.mantenimiento=maquina._mantenimiento_privado
                maquinas_en_mantenimiento.append(maquina)
                print(maquinas_en_mantenimiento)
                print(f"El tecnico {tecnico._nombre} realizará el antenimiento del {tipo} {maquina._num_serial}, estará disponible mañana")
    @staticmethod
    def reparar(maquina):
        if isinstance(maquina, (Cosechador, Fumigador, Tractor)):
            tipo = maquina.__class__.__name__
            
            if maquina.mantenimiento > 0:
                print(f"El {tipo} {maquina._num_serial} no necesita reparación.")
                return
            
            tecnico = seleccionar_tecnico(tipo)
            if tecnico:
                print(f"🔧 El técnico {tecnico._nombre} comenzó la reparación del {tipo} {maquina._num_serial}. estará disponible en dos díasj")
                maquina.mantenimiento = maquina._mantenimiento_privado  # Restaura el mantenimiento
                maquinas_en_reparación.append(maquina)
            else:
                print(f"⚠️ No hay técnicos disponibles para reparar el {tipo} {maquina._num_serial}.")

maquinas_en_mantenimiento=[]
maquinas_en_reparación=[]
ejempplo=Cosechador(1,1,110)
ej2=Fumigador(1,1,255)
eje3=Tractor(1,2,300)

tecnico1=Serviciotecnico("Juan",123456,"Cosechador")
tecnico2=Serviciotecnico("Sofía",987654,"Fumigador")
tecnico3=Serviciotecnico("Julio",147258,"Tractor")


lista_tecnicos=[tecnico1,tecnico2, tecnico3]
Mantenimiento.iniciar_mantenimiento(eje3)
#mover_tractor(eje3,ej2,ejempplo)
#sleep(3)
