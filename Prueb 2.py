import random
import os
import time
from datetime import datetime

from PIL.ImImagePlugin import split


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")
def tuerca_lateral_animada(frame):
    tuerca_frames = [
        "    _____\n   /       \\\n  |   o o   |\n   \\_______/",
        "    _____\n   /   o   \\\n  |    o    |\n   \\_______/",
        "    _____\n   /    o  \\\n  |   o     |\n   \\_______/",
        "    _____\n   /   o   \\\n  |     o   |\n   \\_______/",
    ]
    return tuerca_frames[frame % len(tuerca_frames)]

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


def seleccionar_tecnico(tipo):
    for i in lista_tecnicos:
        if i.maquinaria==tipo:
            if not i.get_laborando():
                print(f"No hay tecnicos disponibles para el tipo {tipo}")
                return None
            else:
                return i

maquinas_en_mantenimiento=[]
maquinas_en_reparacion=[]

class Maquinaria:
    def __init__(self,num_serial, tank_fuel, mantenimiento, en_uso=True):#la hora de mantenimiento es el tiempo de uso antes de un mantenimiento
        self._num_serial=num_serial
        self._tank_fuel=tank_fuel
        self.mantenimiento=mantenimiento#las horas de cada cuanto se hace el mantenimiento
        self._mantenimiento_privado = mantenimiento#las horas de referencia
        self.en_uso=en_uso
    def get_info(self):
        print(self._tank_fuel, self.mantenimiento, self.en_uso)
    def get_serial(self):
        return self._num_serial
    def get_mantenimiento(self):
        return self._mantenimiento_privado
    def get_mantenimiento_privado(self):
        return  self._mantenimiento_privado
    def activar_desactivar(self):
        self.en_uso= not self.en_uso

    def subir_historial(self, accion, tecnico_nombre):
        """Registra un evento en el historial de la máquina."""
        nombre_archivo = f"historial_{self._num_serial}.txt"
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"{fecha_hora} | {accion} | Técnico: {tecnico_nombre}\n"

        try:
            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(linea)
        except Exception as e:
            print(f"Error al guardar el historial: {e}")

    def mostrar_historial(self):
        nombre_archivo = f"historial_{self._num_serial}.txt"
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                print(f"\nHistorial de la máquina {self._num_serial}:")
                print(archivo.read())
        except FileNotFoundError:
            print("No hay historial registrado.")



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
        self.maquinaria=maquinaria
        self._laborando=laborando
    def cambiar_estado(self):
        self._laborando=not self._laborando
    def get_nombre(self):
        return self._nombre
    def get_laborando(self):
        return self._laborando




class Mantenimiento:
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

        if maquina.mantenimiento == 0:
            print(
                f"El tiempo de mantenimiento óptimo para el {tipo} {maquina.get_serial()} ha caducado. Intente hacer reparación.")
            return

        tecnico = seleccionar_tecnico(tipo)
        if tecnico is not None:
            tecnico.cambiar_estado()
            maquina.mantenimiento = maquina.get_mantenimiento_privado()
            maquinas_en_mantenimiento.append(maquina)
            maquina.subir_historial("Mantenimiento preventivo", tecnico.get_nombre())  # <-- Añade esto
            print(
                f"El técnico {tecnico._nombre} realizará el mantenimiento del {tipo} {maquina.get_serial()}. Estará disponible mañana.")
    @staticmethod
    def reparar(maquina):
        if isinstance(maquina, (Cosechador, Fumigador, Tractor)):
            tipo = maquina.__class__.__name__
            
            if maquina.mantenimiento > 0:
                print(f"El {tipo} {maquina.get_serial()} no necesita reparación.")
                return
            
            tecnico = seleccionar_tecnico(tipo)
            if tecnico:
                print(f"🔧 El técnico {tecnico.get_nombre()} comenzó la reparación del {tipo} {maquina.get_serial()}. estará disponible en dos díasj")
                maquina.mantenimiento = maquina.get_mantenimiento_privado()  # Restaura el mantenimiento
                maquinas_en_reparacion.append(maquina)
            else:
                print(f"⚠️ No hay técnicos disponibles para reparar el {tipo} {maquina.get_serial()}.")


ejempplo=Cosechador(1,1,110)
ej2=Fumigador(2,1,255)
eje3=Tractor(3,2,300)

tecnico1=Serviciotecnico("Juan",123456,"Cosechador")
tecnico2=Serviciotecnico("Sofía",987654,"Fumigador")
tecnico3=Serviciotecnico("Julio",147258,"Tractor")


lista_tecnicos=[tecnico1,tecnico2, tecnico3]
Mantenimiento.iniciar_mantenimiento(eje3)
Mantenimiento.iniciar_mantenimiento(ej2)
eje3.mostrar_historial()
ej2.mostrar_historial()
#mover_tractor(eje3,ej2,ejempplo)
#sleep(3)
def eliminar_memoria():
    current_directory = os.getcwd()
    entries = os.listdir(current_directory)
    print(entries) # Returns ['my_data, 'airbnb_data.csv']
    for c in entries:
        if c.split('.')[1]=='txt':
            os.remove(c)
        print(list(c))