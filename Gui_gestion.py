import Gestion
import customtkinter as ctk
import os
from PIL import Image
from tkinter import messagebox

colores = {
    "aguamarina": "#1B3337",
    "marron": "#593B29",
    "verdeclro": "#899D18",
    "verdeoscuro": "#4C5F0C",
    "crema": "#EBCF88"
}
carpeta_imagenes = os.path.join(os.path.dirname(__file__), 'Imgen_interfaz')
ctk.set_appearance_mode('dark')


class Menu:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Gestión de Maquinaria Agrícola")
        self.ventana.geometry("1200x800")
        self.ventana.configure(fg_color=colores["aguamarina"])

        self._configurar_ui()
        self.ventana.mainloop()

    def _configurar_ui(self):
        # Marco principal
        frame_principal = ctk.CTkFrame(self.ventana, fg_color=colores["aguamarina"])
        frame_principal.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        titulo_img = ctk.CTkImage(Image.open(os.path.join(carpeta_imagenes, 'TITULO x3.png')), size=(600, 200))
        ctk.CTkLabel(frame_principal, image=titulo_img, text="").pack(pady=10)

        # Contador de días
        self.label_dia = ctk.CTkLabel(
            frame_principal,
            text=f"DÍA ACTUAL: {Gestion.dia}",
            font=("Arial", 18, "bold"),
            text_color=colores["crema"]
        )
        self.label_dia.pack(pady=10)

        # Botones principales
        opciones = [
            ("📋 Lista de Máquinas", self.abrir_lista_maquinas),
            ("🛠️ Programar Mantenimiento", lambda: VentanaMantenimiento(self.ventana, "Mantenimiento")),
            ("🔧 Programar Reparación", lambda: VentanaMantenimiento(self.ventana, "Reparación")),
            ("🌅 Avanzar Día", self.avanzar_dia),
            ("👨🔧 Ver Técnicos", self.abrir_tecnicos),
            ("➕ Agregar Máquina", self.abrir_agregar_maquina),
            ("➕ Agregar Técnico", self.abrir_agregar_tecnico)
        ]

        for texto, comando in opciones:
            btn = ctk.CTkButton(
                frame_principal,
                text=texto,
                command=comando,
                fg_color=colores["verdeclro"],
                text_color=colores["crema"],
                hover_color=colores["verdeoscuro"],
                font=("Arial", 14),
                height=40,
                width=300
            )
            btn.pack(pady=8)

    def abrir_lista_maquinas(self):
        VentanaListaMaquinas(self.ventana)

    def abrir_tecnicos(self):
        VentanaTecnicos()

    def abrir_agregar_maquina(self):
        VentanaAgregarMaquina(self.ventana)

    def abrir_agregar_tecnico(self):
        VentanaAgregarTecnico(self.ventana)

    def avanzar_dia(self):
        if not Gestion.maquinas_trabajar:
            messagebox.showwarning("Advertencia", "¡No hay máquinas seleccionadas para trabajar!")
            return

        mensajes = Gestion.procesar_nuevo_dia()
        self.label_dia.configure(text=f"DÍA ACTUAL: {Gestion.dia}")

        if mensajes:
            ventana_mensajes = ctk.CTkToplevel(self.ventana)
            ventana_mensajes.title("Atención Requerida")
            ctk.CTkLabel(ventana_mensajes, text="\n".join(mensajes)).pack(pady=20, padx=20)
            ctk.CTkButton(ventana_mensajes, text="Cerrar", command=ventana_mensajes.destroy).pack(pady=10)


class VentanaListaMaquinas(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Listado de Máquinas")
        self.geometry("800x600")
        self._configurar_ui()

    def _configurar_ui(self):
        frame_scroll = ctk.CTkScrollableFrame(self, width=750, height=550)
        frame_scroll.pack(pady=10, padx=10, fill="both", expand=True)

        # Botón para seleccionar máquinas
        ctk.CTkButton(
            frame_scroll,
            text="🚜 Seleccionar Máquinas para Trabajar",
            command=self.abrir_seleccion,
            fg_color=colores["marron"],
            hover_color=colores["verdeclro"]
        ).pack(pady=15)

        # Lista de máquinas
        for maquina in Gestion.todas_las_maquinas:
            estado = self._obtener_estado(maquina)
            frame = ctk.CTkFrame(frame_scroll, fg_color=colores["crema"])
            frame.pack(pady=5, fill="x")

            ctk.CTkLabel(frame, text=f"{maquina.get_serial()} - {estado}",
                         text_color=colores["aguamarina"]).pack(side="left", padx=10)

            ctk.CTkButton(frame, text="Ver Historial",
                          command=lambda m=maquina: self.mostrar_historial(m),
                          width=100).pack(side="right", padx=5)

    def _obtener_estado(self, maquina):
        if maquina.bloqueo == 1:
            return "🔧 En Mantenimiento"
        elif maquina.bloqueo == 2:
            return "⚠️ En Reparación"
        return "✅ Disponible" if maquina.puede_trabajar() else "⛔ No Disponible"

    def mostrar_historial(self, maquina):
        try:
            with open(f"historial_{maquina.get_serial()}.txt", "r", encoding="utf-8") as f:
                contenido = f.read()
        except FileNotFoundError:
            contenido = "No hay historial registrado"

        ventana = ctk.CTkToplevel(self)
        ventana.title(f"Historial - {maquina.get_serial()}")
        ventana.geometry("500x400")

        texto = ctk.CTkTextbox(ventana, wrap="word")
        texto.insert("1.0", contenido)
        texto.pack(pady=10, padx=10, fill="both", expand=True)

    def abrir_seleccion(self):
        venta=ctk.CTk()
        VentanaSeleccionMaquinas(venta)
        self.destroy()


class VentanaSeleccionMaquinas(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Seleccionar Máquinas")
        self.geometry("900x600")
        self._configurar_ui()

    def _configurar_ui(self):
        frame_scroll = ctk.CTkScrollableFrame(self, width=880, height=580)
        frame_scroll.pack(pady=10, padx=10, fill="both", expand=True)

        # Organizar por tipo
        tipos = {
            "Tractor": [],
            "Fumigador": [],
            "Cosechador": []
        }

        for maquina in Gestion.todas_las_maquinas:
            tipos[maquina.__class__.__name__].append(maquina)

        # Crear secciones
        for tipo, maquinas in tipos.items():
            if maquinas:
                ctk.CTkLabel(frame_scroll, text=tipo, font=("Arial", 16, "bold")).pack(pady=10, anchor="w")

                for maquina in maquinas:
                    disponible = maquina.puede_trabajar()
                    frame = ctk.CTkFrame(frame_scroll)
                    frame.pack(pady=3, fill="x")

                    ctk.CTkLabel(frame, text=maquina.get_serial(), width=150).pack(side="left", padx=10)
                    ctk.CTkLabel(frame, text=f"Horas: {maquina.mantenimiento}").pack(side="left", padx=10)
                    var = ctk.BooleanVar()
                    ctk.CTkCheckBox(frame, text="Seleccionar", variable=var,
                                    state="normal" if disponible else "disabled").pack(side="right", padx=10)

                    Gestion.maquinas_trabajar.append(maquina) if maquina.bloqueo == 1 or not maquina.bloqueo == 2 else None

        # Botón confirmar
        ctk.CTkButton(frame_scroll, text="Confirmar Selección",
                      command=self.guardar_seleccion).pack(pady=20)

    def guardar_seleccion(self):
        messagebox.showinfo("Éxito", "Máquinas seleccionadas para trabajar")
        self.destroy()


# ... (Clases VentanaAgregarMaquina, VentanaTecnicos, VentanaAgregarTecnico y VentanaMantenimiento similares al anterior)
class VentanaAgregarMaquina(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.acortadores = ["Tractor", "Fumigador", "Cosechador"]

        self.attributes('-topmost', True)

        # ? configuración ventana
        self.title("Agregar Nueva Máquina")
        self.geometry("400x300")
        self.configure(fg_color=colores["aguamarina"])
        # Configuración de widgets
        self.tipo_var = ctk.StringVar(value="Tractor")
        self.serial_var = ctk.StringVar()
        self.horas_var = ctk.StringVar()

        # Tipo de máquina
        ctk.CTkLabel(self, text="Tipo de Máquina:").pack(pady=5)
        tipo_options = ctk.CTkComboBox(self, variable=self.tipo_var,
                                       values=self.acortadores)
        tipo_options.pack(pady=5)

        # Número de serie
        ctk.CTkLabel(self, text="Número de Serie:").pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.serial_var).pack(pady=5)

        # Horas de mantenimiento
        ctk.CTkLabel(self, text="Horas de Mantenimiento:").pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.horas_var).pack(pady=5)

        # Botón de enviar
        ctk.CTkButton(self, text="Registrar Máquina", fg_color=colores["verdeclro"], command=self.validar_maquina).pack(
            pady=15)

    def validar_maquina(self):
        tipo = self.tipo_var.get()
        serial = self.serial_var.get().strip()
        horas = self.horas_var.get().strip()

        # Validación de datos
        if not serial:
            messagebox.showerror("Error", "El número de serie es obligatorio")
            return

        if not horas.isdigit() or int(horas) <= 0:
            messagebox.showerror("Error", "Horas de mantenimiento inválidas")
            return

        # Verificar serial único
        if any(m.get_serial() == serial for m in Gestion.todas_las_maquinas):
            messagebox.showerror("Error", "¡El número de serie ya existe!")
            return

        # Crear la máquina
        horas_int = int(horas)
        if tipo == "Tractor":
            nueva_maquina = Gestion.Tractor(serial, 100, horas_int)
        elif tipo == "Fumigador":
            nueva_maquina = Gestion.Fumigador(serial, 100, horas_int)
        elif tipo == "Cosechador":
            nueva_maquina = Gestion.Cosechador(serial, 100, horas_int)

        Gestion.todas_las_maquinas.append(nueva_maquina)
        messagebox.showinfo("Éxito", "Máquina registrada correctamente")
        self.destroy()


class VentanaTecnicos(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Listado de Técnicos")
        self.geometry("400x500")
        self.configure(fg_color=colores["aguamarina"])
        self.attributes('-topmost', True)
        # Frame deslizable
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=380, height=450)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.actualizar_lista()

    def actualizar_lista(self):
        # Limpiar frame
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # Título
        ctk.CTkLabel(self.scroll_frame,
                     text="Técnicos Registrados",
                     font=("Arial", 14, "bold")).pack(pady=5)

        # Mostrar técnicos
        if not Gestion.lista_tecnicos:
            ctk.CTkLabel(self.scroll_frame,
                         text="No hay técnicos registrados",
                         text_color="gray").pack(pady=10)
            return

        for i, tecnico in enumerate(Gestion.lista_tecnicos, 1):
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(fill="x", pady=3, padx=5)

            estado = "🟢 Libre" if not tecnico.get_laborando() else "🔴 Ocupado"
            texto = (f"{i}. {tecnico.get_nombre()} | ID: {tecnico.get_identificacion()}\n"
                     f"Especialidad: {tecnico.maquinaria} | Estado: {estado}")

            ctk.CTkLabel(frame, text=texto, anchor="w").pack(side="left", padx=10)


class VentanaAgregarTecnico(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Agregar Nuevo Técnico")
        self.geometry("400x300")
        self.configure(fg_color=colores["aguamarina"])
        self.attributes('-topmost', True)
        # Variables
        self.nombre_var = ctk.StringVar()
        self.id_var = ctk.StringVar()
        self.tipo_var = ctk.StringVar(value="Tractor")

        # Widgets
        ctk.CTkLabel(self, text="Nombre:").pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.nombre_var).pack(pady=5)

        ctk.CTkLabel(self, text="ID:").pack(pady=5)
        ctk.CTkEntry(self, textvariable=self.id_var).pack(pady=5)

        ctk.CTkLabel(self, text="Especialidad:").pack(pady=5)
        ctk.CTkComboBox(self, variable=self.tipo_var,
                        values=["Tractor", "Fumigador", "Cosechador"]).pack(pady=5)

        ctk.CTkButton(self, text="Registrar Técnico", fg_color=colores["verdeclro"], command=self.validar_tecnico).pack(
            pady=15)

    def validar_tecnico(self):
        nombre = self.nombre_var.get().strip()
        id_tecnico = self.id_var.get().strip()
        tipo = self.tipo_var.get()

        # Validaciones
        if not nombre:
            messagebox.showerror("Error", "El nombre es obligatorio")
            return

        if not id_tecnico.isdigit():
            messagebox.showerror("Error", "El ID debe ser numérico")
            return

        # Verificar ID único
        if any(t.get_identificacion() == int(id_tecnico) for t in Gestion.lista_tecnicos):
            messagebox.showerror("Error", "¡El ID ya está registrado!")
            return

        # Crear técnico
        nuevo_tecnico = Gestion.Serviciotecnico(
            nombre=nombre,
            identificacion=int(id_tecnico),
            maquinaria=tipo
        )

        Gestion.lista_tecnicos.append(nuevo_tecnico)
        messagebox.showinfo("Éxito", "Técnico registrado correctamente")
        self.destroy()

class VentanaMantenimiento(ctk.CTkToplevel):
    def __init__(self, parent, tipo_accion):
        super().__init__(parent)
        self.title(f"Programar {tipo_accion}")
        self.geometry("800x600")
        self.attributes('-topmost', True)
        self.tipo_accion = tipo_accion

        # Configurar grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame deslizable
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=780, height=500)
        self.scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


        self.construir_interfaz()

    def construir_interfaz(self):
        # Obtener máquinas según el tipo de acción
        if self.tipo_accion == "Mantenimiento":
            maquinas = [m for m in Gestion.todas_las_maquinas if m.mantenimiento > 0]
        else:
            maquinas = [m for m in Gestion.todas_las_maquinas if m.mantenimiento == 0]

        if not maquinas:
            ctk.CTkLabel(self.scroll_frame,
                         text=f"No hay máquinas necesitando {self.tipo_accion.lower()}",
                         text_color="gray40").pack(pady=20)
            return

        # Crear tarjetas para cada máquina
        self.selecciones = []
        for maquina in maquinas:
            frame = ctk.CTkFrame(self.scroll_frame)
            frame.pack(fill="x", pady=5, padx=5)

            # Estado de disponibilidad
            disponible = self.verificar_disponibilidad(maquina)

            # Imagen representativa
            if maquina.__class__.__name__=='Tractor':
                if not maquina.mantenimiento==0:
                    imagen_accion = ctk.CTkImage(
                        light_image=Image.open(os.path.join(carpeta_imagenes, 'Tractor x16.png')),
                        size=(120, 100))
                else:
                    imagen_accion = ctk.CTkImage(
                        light_image=Image.open(os.path.join(carpeta_imagenes, 'tractor Daño x16.png')),
                        size=(120, 100))
            elif maquina.__class__.__name__=='Cosechador':
                if not maquina.mantenimiento == 0:
                    imagen_accion = ctk.CTkImage(
                        light_image=Image.open(os.path.join(carpeta_imagenes, 'tractor recolector x16.png')),
                        size=(120, 100))
                else:
                    imagen_accion = ctk.CTkImage(
                        light_image=Image.open(os.path.join(carpeta_imagenes, 'Recolector Dañado x16.png')),
                        size=(120, 100))
            elif maquina.__class__.__name__=='Fumigador':
                if not maquina.mantenimiento == 0:
                    imagen_accion = ctk.CTkImage(
                        light_image=Image.open(os.path.join(carpeta_imagenes, 'tractor fumigador x16.png')),
                        size=(120, 100))
                else:
                    imagen_accion = ctk.CTkImage(
                        light_image=Image.open(os.path.join(carpeta_imagenes, 'Fumigador Dañado x16.png')),
                        size=(120, 100))
            ctk.CTkLabel(frame, image=imagen_accion, text="").grid(row=0, column=0, padx=10)

            # Información de la máquina
            info_text = f"{maquina.__class__.__name__}\nSerial: {maquina.get_serial()}\nHoras de mantenimiento: {maquina.get_mantenimiento()}"
            ctk.CTkLabel(frame, text=info_text, justify="left").grid(row=0, column=1, sticky="w")

            # Checkbox de selección
            var = ctk.BooleanVar()
            chk = ctk.CTkCheckBox(frame, text="Seleccionar", variable=var, state="normal" if disponible else "disabled")
            chk.grid(row=0, column=2, padx=10)

            # Lista de técnicos disponibles
            tecnicos_disponibles = self.obtener_tecnicos(maquina)
            combo = ctk.CTkComboBox(frame, values=[t.get_nombre() for t in tecnicos_disponibles])
            combo.set("Seleccione técnico" if tecnicos_disponibles else "Sin técnicos disponibles")
            combo.grid(row=0, column=3, padx=10)

            if not tecnicos_disponibles:
                combo.configure(state="disabled")
                chk.configure(state="disabled")

            self.selecciones.append((maquina, var, combo, tecnicos_disponibles))

        # Botón de confirmación
        btn_confirmar = ctk.CTkButton(
            self,
            text=f"Confirmar {self.tipo_accion}",
            command=self.procesar_seleccion
        )
        btn_confirmar.grid(row=1, column=0, pady=10)

    def verificar_disponibilidad(self, maquina):
        if self.tipo_accion == "Mantenimiento":
            return not any(m.maquina.get_serial() == maquina.get_serial()
                            for m in Gestion.maquinas_en_mantenimiento)
        else:
            return True  # Para reparación siempre disponible si está en la lista

    def obtener_tecnicos(self, maquina):
        tipo = maquina.__class__.__name__
        return [t for t in Gestion.lista_tecnicos
                if t.maquinaria == tipo and not t.get_laborando()]

    def procesar_seleccion(self):
        seleccionados = []
        tecnicos_asignados = set()

        for maquina, var, combo, tecnicos in self.selecciones:
            if var.get():
                if combo.get() == "Seleccione técnico":
                    messagebox.showerror("Error", f"Seleccione un técnico para {maquina.get_serial()}")
                    return

                # Obtener técnico seleccionado
                idx = combo._values.index(combo.get())
                tecnico = tecnicos[idx]

                if tecnico in tecnicos_asignados:
                    messagebox.showerror("Error", "Un técnico no puede atender múltiples máquinas")
                    return

                seleccionados.append((maquina, tecnico))
                tecnicos_asignados.add(tecnico)

        # Validar cantidad de técnicos
        if len(seleccionados) > len([t for t in Gestion.lista_tecnicos if not t.get_laborando()]):
            messagebox.showerror("Error", "No hay suficientes técnicos disponibles")
            return

        # Ejecutar la acción correspondiente
        for maquina, tecnico in seleccionados:
            if self.tipo_accion == "Mantenimiento":
                Gestion.Mantenimiento.iniciar_mantenimiento(maquina,tecnico)
            else:
                Gestion.Mantenimiento.reparar(maquina,tecnico)

        messagebox.showinfo("Éxito", f"{len(seleccionados)} máquinas programadas para {self.tipo_accion.lower()}")
        self.destroy()

if __name__ == "__main__":
    # Configuración inicial de ejemplo
    Gestion.lista_tecnicos = [
        Gestion.Serviciotecnico("Juan Pérez", 1001, "Tractor"),
        Gestion.Serviciotecnico("María García", 1002, "Fumigador"),
        Gestion.Serviciotecnico("Carlos López", 1003, "Cosechador")
    ]

    Gestion.todas_las_maquinas = [
        Gestion.Tractor("TR-001", 100, 50),
        Gestion.Fumigador("FUM-001", 100, 40),
        Gestion.Cosechador("COS-001", 100, 60)
    ]

    Menu()