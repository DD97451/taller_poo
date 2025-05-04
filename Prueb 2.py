import random
import os
import time
from datetime import datetime


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def mover_tractor(lista_objetos):
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
    def eleccion():
        acciones=None
        acciones2=None
        acciones3=None
        for l in lista_objetos:
            if isinstance(l, Tractor):
                objeto_1=l
                funcionando_1 = tractor_funcionando
                reversa_1 = tractor_funcionando_reversa
                exito_1 = tractor_estatico_exitoso
                fallo_1 = tractor_danado
                acciones=[objeto_1,funcionando_1,reversa_1,exito_1,fallo_1]
            elif isinstance(l, Fumigador):
                objeto_2 = l
                funcionando_2 = tractor_fumigador_funcionando
                reversa_2 = tractor_fumigador_funcionando_reversa
                exito_2 = tractor_fumigador_estatico_exitoso
                fallo_2 = tractor_fumigador_danado
                acciones2=[objeto_2,funcionando_2,reversa_2,exito_2,fallo_2]
            elif isinstance(l, Cosechador):
                objeto_3 = l
                funcionando_3 = tractor_podadora_funcionando
                reversa_3 = tractor_podadora_funcionando_reversa
                exito_3 = tractor_podadora_estatico_exitoso
                fallo_3 = tractor_podadora_danado
                acciones3=[objeto_3,funcionando_3,reversa_3,exito_3,fallo_3]

        return acciones,acciones2,acciones3
    (accion,accion2,accion3)=eleccion()
    if not accion is None:#revisanado si mandaron el objeto 1
        objeto1=accion[0]
        funcionando1=accion[1]
        reversa1=accion[2]
        exito1=accion[3]
        fallo1=accion[4]
    else:
        objeto1 = None
        funcionando1= None
        reversa1 = None
        exito1 = None
        fallo1= None
    if not accion2 is None:#revisanado si mandaron el objeto 2
        objeto2=accion2[0]
        funcionando2=accion2[1]
        reversa2=accion2[2]
        exito2=accion2[3]
        fallo2=accion2[4]
    else:
        objeto2 = None
        funcionando2 = None
        reversa2 = None
        exito2 = None
        fallo2 = None
    if not accion3 is None:#revisanado si mandaron el objeto 3
        objeto3=accion3[0]
        funcionando3=accion3[1]
        reversa3=accion3[2]
        exito3=accion3[3]
        fallo3=accion3[4]
    else:
        objeto3 = None
        funcionando3 = None
        reversa3 = None
        exito3 = None
        fallo3 = None

    for i in range(0, 40, 2):
        limpiar()
        if not funcionando1 is None:
            print(funcionando1(i))
        if not funcionando2 is None:
            print(funcionando2(i))
        if not funcionando3 is None:
            print(funcionando3(i))
        time.sleep(0.1)
    time.sleep(0.5)
    for i in range(40, -1, -2):
        limpiar()
        if not reversa1 is None:
            print(reversa1(i))
        if not reversa2 is None:
            print(reversa2(i))
        if not reversa3 is None:
            print(reversa3(i))
        time.sleep(0.1)
    time.sleep(0.5)
    limpiar()
    if not objeto1 is None:
        objeto1.trabajar()
    if not objeto2 is None:
        objeto2.trabajar()
    if not objeto3 is None:
        objeto3.trabajar()
    if [objeto1, objeto2, objeto3]== [None,None,None] and [objeto1.mantenimiento, objeto2.mantenimiento, objeto3.mantenimiento] == [0, 0, 0]:
        for i in range(6):
            limpiar()
            print(fallo1(i))
            print(fallo2(i))
            print(fallo3(i))
            time.sleep(0.5)
    else:
        for i in range(6):
            limpiar()
            if  not objeto1 is None:
                if objeto1.mantenimiento == 0 :
                    print(fallo1(i))
                else:
                    print(exito1())
            if not objeto2 is None:
                if objeto2.mantenimiento == 0:
                    print(fallo2(i))
                else:
                    print(exito2())
            if not objeto3 is None:
                if objeto3.mantenimiento == 0:
                    print(fallo3(i))
                else:
                    print(exito3())
            time.sleep(0.5)


def azar(multiplicador):
    eleccion = random.randrange(0, 2)
    if eleccion == 1:
        return True
    else:
        return False


def seleccionar_tecnico(tipo):
    for i in lista_tecnicos:
        if i.maquinaria == tipo and not i.get_laborando():  # Busca técnicos LIBRES
            return i
    print(f"No hay técnicos disponibles para el tipo {tipo}")
    return None

def nuevo_dia(maquinas_trabajar=None):#lista de maquinas escogidas para trabajar

    global dia
    dia += 1
    print(f"Hoy es el día {dia}.")
    #Animación de maquinas trabajando
    if maquinas_trabajar is None:
        print('No se mandaron a trabajar ninguna maquina')
    else:
        mover_tractor(maquinas_trabajar)
    # Procesar mantenimientos
    for i in maquinas_en_mantenimiento.copy():
        if i.maquina.mantenimiento > 0:
            i.maquina.mantenimiento -= 1
            if i.maquina.mantenimiento == 0:
                print(f"El {i.maquina.__class__.__name__} {i.maquina.get_serial()} ha completado su mantenimiento.")
                i.tecnico.cambiar_estado()  # Liberar técnico
                maquinas_en_mantenimiento.remove(i)
    for j in maquinas_en_reparacion:
        if j.maquina.mantenimiento > 0:
            j.maquina.mantenimiento -= 1
        if j.maquina.mantenimiento == 0:
            print(f"El {j.maquina.__class__.__name__} {j.maquina.get_serial()} ha sido reparado.")
            j.tecnico.cambiar_estado()
            maquinas_en_reparacion.remove(j)

    #Resta del tiempo por el paso del dia
    """for x in maquinas_trabajar:
        x."""


def eliminar_memoria():
    current_directory = os.getcwd()
    entries = os.listdir(current_directory)
    for c in entries:
        if c.split('.')[1] == 'txt':
            os.remove(c)#eliminamos todos los archivos de texto que son la memoria del programa


maquinas_en_mantenimiento = []


maquinas_en_reparacion = []


class Maquinaria:
    def __init__(self, num_serial, tank_fuel, mantenimiento,en_uso=True):  # la hora de mantenimiento es el tiempo de uso antes de un mantenimiento
        self._num_serial = num_serial
        self._tank_fuel = tank_fuel
        self.mantenimiento = mantenimiento  # las horas de cada cuanto se hace el mantenimiento
        self._mantenimiento_privado = mantenimiento  # las horas de referencia
        self.en_uso = en_uso

    def get_info(self):
        print(self._tank_fuel, self.mantenimiento, self.en_uso)

    def get_serial(self):
        return self._num_serial

    def get_mantenimiento(self):
        return self._mantenimiento_privado

    def get_mantenimiento_privado(self):
        return self._mantenimiento_privado

    def activar_desactivar(self):
        self.en_uso = not self.en_uso

    def subir_historial(self, accion, tecnico_nombre, dia):
        """Registra un evento en el historial de la máquina."""
        nombre_archivo = f"historial_{self._num_serial}.txt"
        # fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"Día {dia} | {accion} | Técnico: {tecnico_nombre}\n"

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
    def __init__(self, num_serial, tank_fuel, mantenimiento, en_uso=True):
        super().__init__(num_serial, tank_fuel, mantenimiento, en_uso)

    def trabajar(self):
        tiempo_restante = self.mantenimiento
        result = azar(self.mantenimiento)
        if not result:
            tiempo_restado = random.randrange(0, tiempo_restante + 1)
            self.mantenimiento = self.mantenimiento - tiempo_restado
        return result


class Fumigador(Maquinaria):
    def __init__(self, num_serial, tank_fuel, mantenimiento, en_uso=True):
        super().__init__(num_serial, tank_fuel, mantenimiento, en_uso)

    def trabajar(self):
        tiempo_restante = self.mantenimiento
        result = azar(self.mantenimiento)
        if not result:
            tiempo_restado = random.randrange(0, tiempo_restante + 1)
            self.mantenimiento = self.mantenimiento - tiempo_restado
        return result


class Cosechador(Maquinaria):
    def __init__(self, num_serial, tank_fuel, mantenimiento, en_uso=True):
        super().__init__(num_serial, tank_fuel, mantenimiento, en_uso)

    def trabajar(self):
        tiempo_restante = self.mantenimiento
        result = azar(self.mantenimiento)
        if not result:
            tiempo_restado = random.randrange(0, tiempo_restante + 1)
            self.mantenimiento = self.mantenimiento - tiempo_restado
        return result


class Serviciotecnico:
    def __init__(self, nombre, identificacion, maquinaria, laborando=False):
        self._nombre = nombre
        self._identificacion = identificacion
        self.maquinaria = maquinaria
        self._laborando = laborando  # False: Libre, True: Ocupado

    def get_laborando(self):
        return self._laborando  # Nota el guión bajo en "_laborando"

    def get_nombre(self):
        return self._nombre

    def get_identificacion(self):
        return self._identificacion

    def cambiar_estado(self):
        self._laborando = not self._laborando  # Alterna entre libre/ocupado


class Mantenimiento:
    def __init__(self, maquina, tecnico, día):
        self.maquina = maquina
        self.tecnico = tecnico
        self.día = día


    @staticmethod
    def iniciar_mantenimiento(maquina_seleccionada):
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

        def tuerca_lateral_animada(frame):
            tuerca_frames = [
                "    _____\n   /       \\\n  |   o o   |\n   \\_______/",
                "    _____\n   /   o   \\\n  |    o    |\n   \\_______/",
                "    _____\n   /    o  \\\n  |   o     |\n   \\_______/",
                "    _____\n   /   o   \\\n  |     o   |\n   \\_______/",
            ]
            return tuerca_frames[frame % len(tuerca_frames)]

        if isinstance(maquina_seleccionada, Cosechador):
            tipo = "Cosechador"
            for i in range(6):
                tractor_podadora_reparacion(i)
        elif isinstance(maquina_seleccionada, Fumigador):
            tipo = "Fumigador"
            for i in range(6):
                tractor_fumigador_reparacion(i)
        elif isinstance(maquina_seleccionada, Tractor):
            tipo = "Tractor"
            for i in range(6):
                tractor_reparacion(i)
        else:
            print("hay un error")

        if maquina_seleccionada.mantenimiento == 0:
            print(
                f"El tiempo de mantenimiento óptimo para el {tipo} {maquina_seleccionada.get_serial()} ha caducado. Intente hacer reparación.")
            return

        tecnico = seleccionar_tecnico(tipo)
        if tecnico is not None:
            tecnico.cambiar_estado()
            maquina_seleccionada.mantenimiento = maquina_seleccionada.get_mantenimiento_privado()
            maquina_agregar = Mantenimiento(maquina_seleccionada, tecnico, dia)
            maquinas_en_mantenimiento.append(maquina_agregar)
            maquina_seleccionada.subir_historial("Mantenimiento preventivo", tecnico.get_nombre(), dia)  # <-- Añade esto

            print(
                f"El técnico {tecnico._nombre} realizará el mantenimiento del {tipo} {maquina_seleccionada.get_serial()}. Estará disponible mañana.")


    @staticmethod
    def reparar(equipo):
        if isinstance(equipo, (Cosechador, Fumigador, Tractor)):
            tipo = equipo.__class__.__name__

            if equipo.mantenimiento > 0:
                print(f"El {tipo} {equipo.get_serial()} no necesita reparación.")
                return

            tecnico = seleccionar_tecnico(tipo)
            if tecnico:
                print(
                    f"🔧 El técnico {tecnico.get_nombre()} comenzó la reparación del {tipo} {equipo.get_serial()}. estará disponible en dos díasj")
                equipo.mantenimiento = equipo.get_mantenimiento_privado()  # Restaura el mantenimiento
                maquina_reparar = Mantenimiento(equipo, tecnico, dia)
                maquinas_en_reparacion.append(maquina_reparar)
            else:
                print(f"⚠️ No hay técnicos disponibles para reparar el {tipo} {equipo.get_serial()}.")


# Configuración inicial
dia =0
tecnico1 = Serviciotecnico("Juan", 123456, "Cosechador")
tecnico2 = Serviciotecnico("Sofía", 987654, "Fumigador")
tecnico3 = Serviciotecnico("Julio", 147258, "Tractor")
lista_tecnicos = [tecnico1, tecnico2, tecnico3]
maquina1 = Cosechador(8, 100, 1)  # Mantenimiento: 1 día
maquina2=Tractor(7,51,500)
maquinas_trabajan=[maquina1,maquina2]
nuevo_dia(maquinas_trabajan)
# Prueba paso a paso

print(f"Estado inicial de Juan: {lista_tecnicos[0].get_laborando()}")  # Correcto
# Asignar mantenimiento
j=Mantenimiento
j.iniciar_mantenimiento(maquina1)  # Juan debe estar ocupado ahora
print(f"Estado de Juan después de asignar: {lista_tecnicos[0].get_laborando()}")  # True (ocupado)

# Avanzar día
maquina1.mostrar_historial()
nuevo_dia()  # Completa el mantenimiento
print(f"Estado de Juan después de nuevo_dia(): {lista_tecnicos[0].get_laborando()}")  # False (liberado)
input("Presione Enter para continuar...")
eliminar_memoria()