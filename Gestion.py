import random
import os
import time
horas_trabajada=24
maquinas_en_mantenimiento = []
maquinas_en_reparacion = []


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
        acciones = None
        acciones2 = None
        acciones3 = None
        for l in lista_objetos:
            if isinstance(l, Tractor):
                objeto_1 = l
                funcionando_1 = tractor_funcionando
                reversa_1 = tractor_funcionando_reversa
                exito_1 = tractor_estatico_exitoso
                fallo_1 = tractor_danado
                acciones = [objeto_1, funcionando_1, reversa_1, exito_1, fallo_1]
            elif isinstance(l, Fumigador):
                objeto_2 = l
                funcionando_2 = tractor_fumigador_funcionando
                reversa_2 = tractor_fumigador_funcionando_reversa
                exito_2 = tractor_fumigador_estatico_exitoso
                fallo_2 = tractor_fumigador_danado
                acciones2 = [objeto_2, funcionando_2, reversa_2, exito_2, fallo_2]
            elif isinstance(l, Cosechador):
                objeto_3 = l
                funcionando_3 = tractor_podadora_funcionando
                reversa_3 = tractor_podadora_funcionando_reversa
                exito_3 = tractor_podadora_estatico_exitoso
                fallo_3 = tractor_podadora_danado
                acciones3 = [objeto_3, funcionando_3, reversa_3, exito_3, fallo_3]

        return acciones, acciones2, acciones3

    (accion, accion2, accion3) = eleccion()
    if not accion is None:  # revisanado si mandaron el objeto 1
        objeto1 = accion[0]
        funcionando1 = accion[1]
        reversa1 = accion[2]
        exito1 = accion[3]
        fallo1 = accion[4]
    else:
        objeto1 = None
        funcionando1 = None
        reversa1 = None
        exito1 = None
        fallo1 = None
    if not accion2 is None:  # revisanado si mandaron el objeto 2
        objeto2 = accion2[0]
        funcionando2 = accion2[1]
        reversa2 = accion2[2]
        exito2 = accion2[3]
        fallo2 = accion2[4]
    else:
        objeto2 = None
        funcionando2 = None
        reversa2 = None
        exito2 = None
        fallo2 = None
    if not accion3 is None:  # revisanado si mandaron el objeto 3
        objeto3 = accion3[0]
        funcionando3 = accion3[1]
        reversa3 = accion3[2]
        exito3 = accion3[3]
        fallo3 = accion3[4]
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
    if all(obj is None for obj in [objeto1, objeto2, objeto3]):
        for i in range(6):
            limpiar()
            print("No hay máquinas trabajando.")
            time.sleep(0.5)
    else:

        for i in range(6):
            limpiar()
            if not objeto1 is None:
                if objeto1.mantenimiento == 0:
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
    lista_disponibles = []
    for i in lista_tecnicos:
        if i.maquinaria == tipo and not i.get_laborando():  # Busca técnicos LIBRES
            lista_disponibles.append(i)
            print("Seleccione un técnico:")
            for j in enumerate(lista_disponibles):
                print(f"{j[0] + 1}. {j[1].get_nombre()} (ID: {j[1].get_identificacion()})")
    if lista_disponibles:
        while True:
            try:
                seleccion = int(input("Seleccione el número del técnico: ")) - 1
                if seleccion < 0 or seleccion >= len(lista_disponibles):
                    raise ValueError("Selección no válida.")
                return lista_disponibles[seleccion]
            except ValueError:
                print("Selección no válida. Intente de nuevo.")
                continue
    else:        
        print(f"No hay técnicos disponibles para el tipo {tipo}")
        return None


def nuevo_dia(maquinas_trabajar=None):
    global dia
    dia += 1
    print(f"\n--- DÍA {dia} ---")

    # Restar 1 hora de mantenimiento por dia trabajado a las máquinas activas
    if maquinas_trabajar:
        mover_tractor(maquinas_trabajar)
        for maquina in maquinas_trabajar:
            if maquina.mantenimiento > 0:
                maquina.mantenimiento -= horas_trabajada
                if maquina.mantenimiento >0:
                    print(
                        f"{maquina.__class__.__name__} #{maquina.get_serial()} trabajó{horas_trabajada}. Horas restantes: {maquina.mantenimiento}")
                else:
                    print(
                        f"¡Atención! {maquina.__class__.__name__} #{maquina.get_serial()} necesita mantenimiento urgente.")

            else:
                print(
                    f"¡Atención! {maquina.__class__.__name__} #{maquina.get_serial()} necesita mantenimiento urgente.")
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



def eliminar_memoria():
    try:
        # Eliminar archivos de texto en el directorio actual
        current_directory = os.getcwd()
        entries = os.listdir(current_directory)
        for c in entries:
            if c.split('.')[1] == 'txt':
                os.remove(c)  # eliminamos todos los archivos de texto que son la memoria del programa
    except:
        print("GRACIAS POR USAR EL PROGRAMA")


def tractor_reparacion(frame, accion):
    tuerca = tuerca_lateral_animada(frame)
    return f"""{tuerca}

                   ______
             ____|__|__\\___
            |   _   ___   `|
           /|__|_|_|___|___|
           ( o )         ( o )

                🔧 EN {accion} 🔧"""


def tractor_podadora_reparacion(frame, accion):
    base = tractor_reparacion(frame, accion)
    return base.replace(f"EN {accion}", f"EN {accion} (podadora)")


def tractor_fumigador_reparacion(frame, accion):
    base = tractor_reparacion(frame, accion)
    return base.replace(f"EN {accion}", f"EN {accion} (fumigador)")


def tuerca_lateral_animada(frame):
    tuerca_frames = [
        "    _____\n   /       \\\n  |   o o   |\n   \\_______/",
        "    _____\n   /   o   \\\n  |    o    |\n   \\_______/",
        "    _____\n   /    o  \\\n  |   o     |\n   \\_______/",
        "    _____\n   /   o   \\\n  |     o   |\n   \\_______/",
    ]
    return tuerca_frames[frame % len(tuerca_frames)]

contrasena = "1234"

def menu(maquinas):
    maquinas_trabajando = []

    while True:
        input
        time.sleep(1)
        limpiar()
        time.sleep(0.5)

        print("\n" + "-" * 40)
        print(f"Sistema de Gestión de Maquinaria\n DÍA {dia}")
        print("-" * 40)
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver listado de máquinas")
        print("2. Enviar máquinas a trabajar")
        print("3. Programar mantenimiento preventivo")
        print("4. Reparar máquina averiada")
        print("5. Avanzar al siguiente dia")
        print("6. Ver historial de una máquina")
        print("7. Agregar Máquina")
        print("8. Agregar Técnico")
        print("9. Ver técnicos")
        print("10. Salir del sistema")
        print("-" * 40)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- LISTADO DE MÁQUINAS ---")
            for i, maquina in enumerate(maquinas):
                # Verificar si está en mantenimiento (por serial)
                en_mantenimiento = any(
                    m.maquina.get_serial() == maquina.get_serial()
                    for m in maquinas_en_mantenimiento
                )
                # Verificar si está en reparación (por serial)
                en_reparacion = any(
                    m.maquina.get_serial() == maquina.get_serial()
                    for m in maquinas_en_reparacion
                )
                estado = "🔧 Mantenimiento" if en_mantenimiento else "⚠️ Reparación" if en_reparacion else "✅ Disponible"
                print(f"{i + 1}. {maquina.__class__.__name__} #{maquina.get_serial()} - Estado: {estado}")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("\n--- ENVIAR MÁQUINAS A TRABAJAR ---")
            for i, maquina in enumerate(maquinas):
                print(f"{i + 1}. {maquina.get_serial()}")
            indices = input("Ingrese los números de las máquinas a trabajar separados por coma: ")
            maquinas_trabajando = []
            for i in indices.split(","):
                idx = int(i) - 1
                # Verificar si está en mantenimiento (por serial)
                en_mantenimiento = any(
                    m.maquina.get_serial() == maquinas[idx].get_serial()
                    for m in maquinas_en_mantenimiento
                )
                # Verificar si está en reparación (por serial)
                en_reparacion = any(
                    m.maquina.get_serial() == maquinas[idx].get_serial()
                    for m in maquinas_en_reparacion
                )
                if 0 <= idx < len(maquinas):
                    if en_mantenimiento:
                        print(f"⚠️ La máquina {maquinas[idx].get_serial()} está en mantenimiento.")
                    elif en_reparacion:
                        print(f"⚠️ La máquina {maquinas[idx].get_serial()} está en reparación.")
                    else:
                        maquinas_trabajando.append(maquinas[idx])
                        print(f"{maquinas[idx].get_serial()} enviada a trabajar.")

        elif opcion == "3":
            print("\n--- PROGRAMAR MANTENIMIENTO PREVENTIVO ---")
            for i, maquina in enumerate(maquinas):
                print(f"{i + 1}. {maquina.get_serial()}")
            while True:
                try: 
                    idx = int(input("Seleccione el número de la máquina: ")) - 1
                    if 0 <= idx < len(maquinas):
                        Mantenimiento.iniciar_mantenimiento(maquinas[idx])
                        print(f"{maquinas[idx].get_serial()} está en mantenimiento prentivo.")
                        break
                except ValueError:
                    print("Opción no válida. Intente de nuevo.")
                    continue

        elif opcion == "4":
            print("\n--- REPARAR MÁQUINA AVERIADA ---")
            for i, maquina in enumerate(maquinas):
                print(f"{i + 1}. {maquina.get_serial()}")
            idx = int(input("Seleccione el número de la máquina: ")) - 1
            if 0 <= idx < len(maquinas):
                Mantenimiento.reparar(maquinas[idx])

        elif opcion == "5":
            print("\n--- AVANZAR AL SIGUIENTE DÍA ---")
            nuevo_dia(maquinas_trabajando)
            print("Nuevo dia procesado.")
            maquinas_trabajando = []

        elif opcion == "6":
            print("\n--- HISTORIAL DE UNA MÁQUINA ---")
            for i, maquina in enumerate(maquinas):
                print(f"{i + 1}. {maquina.get_serial()}")
            idx = int(input("Seleccione el número de la máquina: ")) - 1
            if 0 <= idx < len(maquinas):
                maquinas[idx].mostrar_historial()
            input("Presione Enter para continuar...")
        elif opcion == "7":
            print("\n--- AGREGAR MÁQUINA ---")
            agregar_maquina()
            print("Máquina agregada exitosamente.")
        elif opcion == "8":
            print("\n--- AGREGAR TÉCNICO ---")
            agregar_tecnico()
            print("Técnico agregado exitosamente.") 
        elif opcion == "9":
            print("\n--- VER TÉCNICOS ---")
            ver_tecnicos()   
        elif opcion == "10":
            verificar = input("¿Está seguro de que desea salir? (s/n): ")
            if verificar.lower() == "s":
                password = input("Ingrese la contraseña para salir: ")
                if password == contrasena:
                    print("Contraseña correcta. Saliendo del sistema...")
                    eliminar_memoria()
                    break
                else:
                    print("Contraseña incorrecta. No se puede salir del sistema.")
                    continue
            elif verificar.lower() == "n":
                print("Regresando al menú principal...")
                continue    
            else:
                print("Opción no válida. Regresando al menú principal...")
                continue
        else:
            print("Opción no válida. Intente de nuevo.")


def agregar_maquina():
    while True:
        try:
            eleccion = input(f"¿Qué tipo de máquina desea agregar?\n1. Cosechador\n2. Fumigador\n3. Tractor: \n")
        except ValueError:
            print("Opción no válida. Intente de nuevo.")
            continue
        while True:
            try:
                serial = input("Ingrese el número de serie de la máquina: ")
                if not serial:
                    raise ValueError("El número de serie no puede estar vacío.")
                for i in todas_las_maquinas:
                    if i.get_serial() == serial:
                        raise ValueError("El número de serie ya existe.")

                break
            except ValueError as e:
                print("Error: debe ingresar un número de serie válido.")
                continue
        while True:
            try:
                horas_mantenimiento = int(input("Ingrese las horas de mantenimiento: "))
                if horas_mantenimiento <= 0:
                    raise ValueError("Las horas de mantenimiento deben ser un número positivo.")
                break
            except ValueError as e:
                print("Error: debe ingresar un número positivo.")
                continue

        if eleccion == "1":
            nueva_maquina = Cosechador(serial, 100, horas_mantenimiento)

        elif eleccion == "2":
            nueva_maquina = Fumigador(serial, 100, horas_mantenimiento)

        elif eleccion == "3":
            nueva_maquina = Tractor(serial, 100, horas_mantenimiento)

        else:
            print("Opción no válida. Intente de nuevo.")
            continue
        # Agregar la nueva máquina a la lista de máquinas
        todas_las_maquinas.append(nueva_maquina)
        break


def agregar_tecnico():
    while True:
        try:
            nombre = input("Ingrese el nombre del técnico: ")
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            else:
                break
        except ValueError:
            print("el nombre no puede estar vacío.")
            continue

    while True:
        try:
            identificacion = int(input("Ingrese la identificación del técnico: "))
            if identificacion <= 0:
                print("La identificación debe ser un número positivo.")
                continue
            for i in lista_tecnicos:
                if i.get_identificacion() == identificacion:
                    raise ValueError("La identificación ya existe.")
            break
                
        except ValueError:
            print("Error: La identificación debe ser un número positivo.")
            continue

    while True:
        try:
            maquinaria = int(input("Ingrese el tipo de maquinaria que repara \n1. Cosechador'\n2. Fumigador\n3. Tractor: "))
            if maquinaria not in [1, 2, 3]:
                raise ValueError("Tipo de maquinaria no válido.")
            else :
                if maquinaria == 1:
                    maquinaria = "Cosechador"
                elif maquinaria == 2:
                    maquinaria = "Fumigador"
                elif maquinaria == 3:
                    maquinaria = "Tractor"
            break
        except ValueError:
            print("Error: debe ingresar un número entre 1 y 3.")
            continue

    nuevo_tecnico = Serviciotecnico(nombre, identificacion, maquinaria)
    lista_tecnicos.append(nuevo_tecnico)


def ver_tecnicos():
    print("\n--- LISTADO DE TÉCNICOS ---")
    for i, tecnico in enumerate(lista_tecnicos):
        estado = "Libre" if not tecnico.get_laborando() else "Ocupado"
        print(f"{i + 1}. {tecnico.get_nombre()} (ID: {tecnico.get_identificacion()}) - Estado: {estado}")
    input("Presione Enter para continuar...")



class Maquinaria:
    def __init__(self, num_serial, tank_fuel, mantenimiento,
                 en_uso=True):  # la hora de mantenimiento es el tiempo de uso antes de un mantenimiento
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
        hoy = time.localtime()
        hoy = time.strftime("%Y-%m-%d", hoy)
        nombre_archivo = f"historial_{self._num_serial}.txt"
        linea = f"📅 {hoy}| Día {dia} ||\n🔄 Actividad: {accion} |\n👨‍🔧 Técnico: {tecnico_nombre}||\n"
        titulo =f"╔════════════════════════════════════════════════════════╗\n║              🛠️ MANTENIMIENTOS REGISTRADOS -  {self._num_serial}  🚜    ║\n╚════════════════════════════════════════════════════════╝\n"


        try:
        # Verificar si el archivo ya existe
            archivo_nuevo = not os.path.exists(nombre_archivo)

            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                if archivo_nuevo:
                    archivo.write(titulo)
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
    def __init__(self, maquina, tecnico, dia):
        self.maquina = maquina
        self.tecnico = tecnico
        self.dia = dia

    @staticmethod
    def iniciar_mantenimiento(maquina_seleccionada):
        accion = "Mantenimiento preventivo"
        if isinstance(maquina_seleccionada, (Cosechador, Fumigador, Tractor)):
            tipo = maquina_seleccionada.__class__.__name__

        if maquina_seleccionada.mantenimiento == 0:
            print(
                f"El tiempo de mantenimiento óptimo para el {tipo} {maquina_seleccionada.get_serial()} ha caducado. Intente hacer reparación.")
            return

        tecnico = seleccionar_tecnico(tipo)
        if tecnico is not None:
            tecnico.cambiar_estado()
            if tipo == "Cosechador":

                for i in range(6):
                    limpiar()
                    print(tractor_podadora_reparacion(i, accion))
                    time.sleep(0.5)
            elif tipo == "Fumigador":
                for i in range(6):
                    limpiar()
                    print(tractor_fumigador_reparacion(i, accion))
                    time.sleep(0.5)
            elif tipo == "Tractor":
                for i in range(6):
                    limpiar()
                    print(tractor_reparacion(i, accion))
                    time.sleep(0.5)
            else:
                print("hay un error")
                return
            maquina_seleccionada.mantenimiento = maquina_seleccionada.get_mantenimiento_privado()
            maquina_agregar = Mantenimiento(maquina_seleccionada, tecnico, dia)
            maquinas_en_mantenimiento.append(maquina_agregar)
            maquina_seleccionada.subir_historial("Mantenimiento preventivo", tecnico.get_nombre(),dia)  # <-- Añade esto

            print(
                f"El técnico {tecnico._nombre} realizará el mantenimiento del {tipo} {maquina_seleccionada.get_serial()}. Estará disponible mañana.")
        else:
            print(f"⚠️ No hay técnicos disponibles para el {tipo} {maquina_seleccionada.get_serial()}.")

    @staticmethod
    def reparar(maquina_seleccionada):
        accion = "Reparación"
        if isinstance(maquina_seleccionada, (Cosechador, Fumigador, Tractor)):
            tipo = maquina_seleccionada.__class__.__name__
        if maquina_seleccionada.mantenimiento > 0:
            print(f"El {tipo} {maquina_seleccionada.get_serial()} no necesita reparación.")
            return
        for i in maquinas_en_reparacion:
            if i.maquina.get_serial() == maquina_seleccionada.get_serial():
                print(f"El {tipo} {maquina_seleccionada.get_serial()} ya está en reparación.")
                return

        tecnico = seleccionar_tecnico(tipo)
        if tecnico:
            tecnico.cambiar_estado()
            if tipo == "Cosechador":

                for i in range(6):
                    limpiar()
                    print(tractor_podadora_reparacion(i, accion))
                    time.sleep(0.5)
            elif tipo == "Fumigador":
                for i in range(6):
                    limpiar()
                    print(tractor_fumigador_reparacion(i, accion))
                    time.sleep(0.5)
            elif tipo == "Tractor":
                for i in range(6):
                    limpiar()
                    print(tractor_reparacion(i, accion))
                    time.sleep(0.5)
            else:
                print("hay un error")
                return
            print(
                f"🔧 El técnico {tecnico.get_nombre()} comenzó la reparación del {tipo} {maquina_seleccionada.get_serial()}. estará disponible en dos díasj")
            maquina_seleccionada.mantenimiento = maquina_seleccionada.get_mantenimiento_privado()  # Restaura el mantenimiento
            maquina_reparar = Mantenimiento(maquina_seleccionada, tecnico, dia)
            maquinas_en_reparacion.append(maquina_reparar)
        else:
            print(f"⚠️ No hay técnicos disponibles para reparar el {tipo} {maquina_seleccionada.get_serial()}.")


# Configuración inicial
dia = 0

# Instancia de técnicos
tecnico1 = Serviciotecnico("Juan", 123456, "Cosechador")
tecnico2 = Serviciotecnico("Sofía", 987654, "Fumigador")
tecnico3 = Serviciotecnico("Julio", 147258, "Tractor")

# Instancia de máquinas
maquina1 = Cosechador("C1", 100, 13)
maquina2 = Fumigador("F1", 100, 5)
maquina3 = Tractor("T1", 100, 5)
maquina4 = Cosechador("C2", 100, 5)
maquina5 = Fumigador("F2", 100, 5)
maquina6 = Tractor("T2", 100, 5)

# Listas de técnicos y máquinas
lista_tecnicos = [tecnico1, tecnico2, tecnico3]
todas_las_maquinas = [maquina1, maquina2, maquina3, maquina4, maquina5, maquina6]

# Ejecución del programa
if __name__ == "__main__":
    menu(todas_las_maquinas)
