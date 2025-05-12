import random
import os

# Variables globales
horas_trabajada = 24
maquinas_en_mantenimiento = []
maquinas_en_reparacion = []
maquinas_trabajar = []
lista_tecnicos = []
todas_las_maquinas = []
dia = 0


class Maquinaria:
    def __init__(self, num_serial, tank_fuel, mantenimiento, en_uso=True):
        self._num_serial = num_serial
        self._tank_fuel = tank_fuel
        self.mantenimiento = mantenimiento
        self._mantenimiento_privado = mantenimiento
        self.en_uso = en_uso
        self.bloqueo = 0  # 0=disponible, 1=mantenimiento, 2=reparacion

    def puede_trabajar(self):
        return self.bloqueo == 0 and self.mantenimiento > 0

    def get_serial(self):
        return self._num_serial

    def get_mantenimiento(self):
        return self._mantenimiento_privado

    def subir_historial(self, accion, tecnico_nombre, dia):
        nombre_archivo = f"historial_{self._num_serial}.txt"
        titulo = f"╔════════════════════════════════════════════════════════╗\n║              🛠️ MANTENIMIENTOS REGISTRADOS -  {self._num_serial}  🚜    ║\n╚════════════════════════════════════════════════════════╝\n"

        try:
            archivo_nuevo = not os.path.exists(nombre_archivo)
            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                if archivo_nuevo:
                    archivo.write(titulo)
                archivo.write(f"📅 Día {dia} || 🔄 Actividad: {accion} || 👨🔧 Técnico: {tecnico_nombre}\n")
        except Exception as e:
            return f"Error: {str(e)}"
        return "Historial actualizado"


class Tractor(Maquinaria):
    def trabajar(self):
        if self.mantenimiento > 0:
            self.mantenimiento -= random.randint(0, self.mantenimiento)
        return self.mantenimiento > 0


class Fumigador(Maquinaria):
    def trabajar(self):
        if self.mantenimiento > 0:
            self.mantenimiento -= random.randint(0, self.mantenimiento)
        return self.mantenimiento > 0


class Cosechador(Maquinaria):
    def trabajar(self):
        if self.mantenimiento > 0:
            self.mantenimiento -= random.randint(0, self.mantenimiento)
        return self.mantenimiento > 0


class Serviciotecnico:
    def __init__(self, nombre, identificacion, maquinaria, laborando=False):
        self._nombre = nombre
        self._identificacion = identificacion
        self.maquinaria = maquinaria
        self._laborando = laborando

    def get_laborando(self):
        return self._laborando

    def get_nombre(self):
        return self._nombre

    def get_identificacion(self):
        return self._identificacion

    def cambiar_estado(self):
        self._laborando = not self._laborando


class Mantenimiento:
    @staticmethod
    def iniciar_mantenimiento(maquina, tecnico):
        maquina.bloqueo = 1
        maquina.mantenimiento = maquina.get_mantenimiento()
        maquina.subir_historial("Mantenimiento preventivo", tecnico.get_nombre(), dia)
        tecnico.cambiar_estado()
        maquinas_en_mantenimiento.append(maquina)

    @staticmethod
    def reparar(maquina, tecnico):
        maquina.bloqueo = 2
        maquina.mantenimiento = maquina.get_mantenimiento()
        maquina.subir_historial("Reparación", tecnico.get_nombre(), dia)
        tecnico.cambiar_estado()
        maquinas_en_reparacion.append(maquina)


def procesar_nuevo_dia():
    global dia
    dia += 1
    mensajes = []

    # Procesar máquinas trabajando
    for maquina in maquinas_trabajar:
        if maquina.puede_trabajar():
            maquina.trabajar()
            if maquina.mantenimiento <= 0:
                mensajes.append(f"¡{maquina.get_serial()} necesita mantenimiento urgente!")

    # Procesar mantenimientos
    for maquina in maquinas_en_mantenimiento.copy():
        maquina.mantenimiento -= 1
        if maquina.mantenimiento <= 0:
            maquina.bloqueo = 0
            maquinas_en_mantenimiento.remove(maquina)

    # Procesar reparaciones
    for maquina in maquinas_en_reparacion.copy():
        maquina.mantenimiento -= 1
        if maquina.mantenimiento <= 0:
            maquina.bloqueo = 0
            maquinas_en_reparacion.remove(maquina)

    maquinas_trabajar.clear()
    return mensajes


def obtener_tecnicos_disponibles(tipo):
    return [t for t in lista_tecnicos if t.maquinaria == tipo and not t.get_laborando()]