import Gestion
from tkinter import CENTER, StringVar, messagebox
import customtkinter as ctk
import os
from PIL import Image, ImageTk

colores = {"aguamarina": "#1B3337", "marron": "#593B29", "verdeclro": "#899D18", "verdeoscuro": "#4C5F0C",
           "crema": "#EBCF88"}
# ? Direcciones de las imagenes
carpeta_master = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_master, 'Imgen_interfaz')
ctk.set_appearance_mode('dark')


class Menu:
    def __init__(self):

        #contador de dias
        self.dia = 0

        self.__ventana = ctk.CTk()
        self._text_preview = StringVar()

        # Color de la ventana
        self.__ventana.configure(fg_color=colores["aguamarina"])
        # configuracíon de ventana principal
        self.__ventana.title('Sistema de Gestión de Maquinaria')
        self.__ventana.geometry('1350x900')  # Tamaño de la ventana

        # self.__ventana.iconbitmap(os.path.join('Imgen_interfaz', 'icono.ico'))
        # configuracion de previe

        # ? Titulo del menu
        titulo_imagen = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, 'TITULO x3.png')),
                                     size=(700, 350))
        titulo_ventana = ctk.CTkLabel(master=self.__ventana, image=titulo_imagen, text='', text_color=colores["crema"])
        titulo_ventana.place(relx=0.5, y=120, anchor=CENTER)
        #?Contador de dias
        self.label_dia = ctk.CTkLabel(
            self.__ventana,
            text=f"Día actual: {self.dia}",
            font=("Arial", 16),
            text_color=colores["crema"]
        )
        self.label_dia.place(relx=0.95, rely=0.05, anchor="ne")

        # ?Botones de elección
        scroll_menu = (ctk.CTkScrollableFrame(master=self.__ventana, width=600, height=600, ))

        scroll_menu.place(relx=0.5, rely=2.34 / 4, anchor=CENTER)
        scroll_menu.configure(fg_color=colores["marron"])
        # ??COLUMNA 1
        listado_maquina_imagen = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
                                              # ° imagen del titutlo de lista de maquinas
                                              size=(100, 100))

        lista_maquina = ctk.CTkButton(scroll_menu,
                                      image=listado_maquina_imagen,
                                      text='1', command=self.mostrar_ventana_lista, fg_color=colores["crema"],
                                      text_color=colores["aguamarina"], hover_color=colores["aguamarina"]
                                      ).pack(anchor=CENTER,pady=10,padx=10)


        self.btn_mantenimiento = ctk.CTkButton(
            scroll_menu,
            image=listado_maquina_imagen,
            text='5',
            command=self.abrir_mantenimiento,
            fg_color=colores["crema"],
            text_color=colores["aguamarina"]
        )
        self.btn_mantenimiento.pack(anchor=CENTER,pady=10,padx=10)

        self.btn_reparacion = ctk.CTkButton(scroll_menu,
                                            image=listado_maquina_imagen,
                                            text='4', fg_color=colores["crema"],
                                            text_color=colores["aguamarina"],
                                            command=self.abrir_reparacion
                                            )
        self.btn_reparacion.pack(anchor=CENTER,pady=10,padx=10)

        self.btn_avanzar_dia = ctk.CTkButton(
            scroll_menu,
            image=listado_maquina_imagen,
            text='Avanzar Día',
            command=self.iniciar_nuevo_dia,
            fg_color=colores["crema"],
            text_color=colores["aguamarina"],
            hover_color=colores["aguamarina"]
        )
        self.btn_avanzar_dia.pack(anchor=CENTER,pady=10,padx=10)

        ver_tecnicos_btn = ctk.CTkButton(
            scroll_menu,
            text="👨🔧 Ver Técnicos",
            command=self.mostrar_ventana_tecnicos
        )
        ver_tecnicos_btn.pack(anchor=CENTER,pady=10,padx=10)
        ver_tecnicos_btn.configure(fg_color=colores["verdeclro"])

        agregar_tecnico_btn = ctk.CTkButton(
            scroll_menu,
            text="➕ Agregar Técnico",
            command=self.mostrar_ventana_agregar_tecnico
        )
        agregar_tecnico_btn.pack(anchor=CENTER,pady=10,padx=10)
        agregar_tecnico_btn.configure(fg_color=colores["verdeclro"])


        agregar_maquina_btn = ctk.CTkButton(
            scroll_menu,
            text="➕ Agregar Máquina",
            command=self.mostrar_ventana_agregar
        )
        agregar_maquina_btn.pack(anchor=CENTER,pady=10,padx=10)
        agregar_maquina_btn.configure(fg_color=colores["verdeclro"])

        self.__ventana.mainloop()

    def mostrar_ventana_agregar(self):
        VentanaAgregarMaquina(self.__ventana)

    def mostrar_ventana_lista(self):
        VentanaLista()

    def mostrar_ventana_agregar_tecnico(self):
        VentanaAgregarTecnico(self.__ventana)

    def mostrar_ventana_tecnicos(self):
        VentanaTecnicos()

    def actualizar_preview_maquinas(self):
        pass

    def update_text(self):
        archivo = open('historial_C1.txt', 'r', encoding='utf-8')
        self._text_preview.set(archivo.read())

    def abrir_mantenimiento(self):
        VentanaMantenimiento(self.__ventana, tipo_accion="Mantenimiento")

    def abrir_reparacion(self):
        VentanaMantenimiento(self.__ventana, tipo_accion="Reparación")

    def iniciar_nuevo_dia(self):
        # Crear ventana de animación
        ventana_animacion = ctk.CTkToplevel(self.__ventana)
        ventana_animacion.title("Avanzando al nuevo día")
        ventana_animacion.geometry("400x400")
        ventana_animacion.attributes('-topmost', True)

        # Cargar GIF
        try:
            gif_path = os.path.join(carpeta_imagenes, 'Pasar dia x16.gif')
            gif = Image.open(gif_path)
            frames = []

            # Extraer todos los frames del GIF
            for frame in range(0, gif.n_frames):
                gif.seek(frame)
                frames.append(ctk.CTkImage(light_image=gif.copy(), size=(300, 300)))

            label_animacion = ctk.CTkLabel(ventana_animacion, text="")
            label_animacion.pack(pady=20)

            # Mostrar animación
            self.mostrar_animacion(frames, 0, label_animacion, ventana_animacion)

        except Exception as e:

            messagebox.showerror("Error", f"No se pudo cargar la animación: {str(e)}")
            ventana_animacion.destroy()


    def mostrar_animacion(self, frames, frame_actual, label, ventana):
        if frame_actual < len(frames):
            # Actualizar frame
            label.configure(image=frames[frame_actual])
            # Programar próximo frame después de 100ms
            self.__ventana.after(500, lambda: self.mostrar_animacion(frames, frame_actual + 1, label, ventana))
        else:
            # Finalizar animación
            ventana.destroy()
            self.dia += 1
            messagebox.showinfo("Nuevo día", f"¡Ahora es el día {self.dia}!")
            self.label_dia.configure(text=f"Día actual: {self.dia}")            # Aquí puedes agregar lógica adicional para actualizar estados

    def pl(self):
        pass


class VentanaLista:
    def __init__(self):
        # super().__init__(tipo_tractor)
        # ? Clasificar las máquinas
        self.list_tractores, self.list_fumigadores, self.list_cosechadoras = self.clasificar_tipo_maquina(
            Gestion.todas_las_maquinas)

        # ?Configuracioón ventana(lista de maquinas registradas)
        self.ventana_maquinas = ctk.CTkToplevel()
        self.ventana_maquinas.geometry('300x500')  # ° Tamaño 2 vemtana
        self.ventana_maquinas.resizable(False, False)
        self.ventana_maquinas.attributes('-topmost', True)

        # ?lista auxiliar

        # ? Funciones de segunda ventana
        def devolver():
            self.tractor.pack(pady=10)
            self.fumigador.pack(pady=10)
            self.cosechador.pack(pady=10)
            self.boton_enviar_trabajar.pack(pady=10)
            self.scroll_listas.pack_forget()
            self.devolver.pack_forget()
            self.devolver.configure(fg_color=colores["aguamarina"])

        def ocultar():  # Oculta botones principales
            self.tractor.pack_forget()
            self.fumigador.pack_forget()
            self.cosechador.pack_forget()
            self.boton_enviar_trabajar.pack_forget()

        def mostrar_botones():
            self.scroll_listas.pack(pady=5)
            self.scroll_listas.configure(fg_color=colores["aguamarina"])
            self.devolver.pack(pady=5)

        def mostrar_tractores(lista_maquinas):
                # Limpiar widgets anteriores
                if hasattr(self, 'title_lisatado'):
                    self.title_lisatado.destroy()
                if hasattr(self, 'labels_seriales'):
                    for label in self.labels_seriales:
                        label.destroy()

                # Crear nuevos elementos
                self.title_lisatado = ctk.CTkLabel(self.scroll_listas, text='Tractores registrados',
                                                   font=('verdana', 15))
                self.title_lisatado.pack()

                self.labels_seriales = []
                for n, tractor in enumerate(lista_maquinas, 1):
                    boton = ctk.CTkButton(
                        self.scroll_listas,
                        text=f'{n}) {tractor.get_serial()}',
                        command=lambda serial=tractor.get_serial(): self.mostrar_historial(serial)
                    )
                    boton.pack(pady=2)
                    self.labels_seriales.append(boton)

        def mostrar_cosechador(lista_maquinas):
            # Limpiar widgets anteriores
            if hasattr(self, 'title_lisatado'):
                self.title_lisatado.destroy()
            if hasattr(self, 'labels_seriales'):
                for label in self.labels_seriales:
                    label.destroy()

            # Crear nuevos elementos
            self.title_lisatado = ctk.CTkLabel(self.scroll_listas, text='Tractores registrados', font=('verdana', 15))
            self.title_lisatado.pack()

            self.labels_seriales = []
            for n, cosechador in enumerate(lista_maquinas, 1):
                boton = ctk.CTkButton(
                    self.scroll_listas,
                    text=f'{n}) {cosechador.get_serial()}',
                    command=lambda serial=cosechador.get_serial(): self.mostrar_historial(serial)
                )
                boton.pack(pady=2)
                self.labels_seriales.append(boton)
        def mostrar_fumigador(lista_maquinas):
            # Limpiar widgets anteriores
            if hasattr(self, 'title_lisatado'):
                self.title_lisatado.destroy()
            if hasattr(self, 'labels_seriales'):
                for label in self.labels_seriales:
                    label.destroy()

            self.title_lisatado = ctk.CTkLabel(self.scroll_listas, text='Tractores registrados', font=('verdana', 15))
            self.title_lisatado.pack()
            # creacion automatica del listado
            self.labels_seriales = []
            for n, fumigador in enumerate(lista_maquinas, 1):
                boton = ctk.CTkButton(
                    self.scroll_listas,
                    text=f'{n}) {fumigador.get_serial()}',
                    command=lambda serial=fumigador.get_serial(): self.mostrar_historial(serial)
                )
                boton.pack(pady=2)
                self.labels_seriales.append(boton)


        # ? Botones segunda ventana
        # ?? Deslizable de lista de tractores
        self.scroll_listas = ctk.CTkScrollableFrame(self.ventana_maquinas, fg_color=colores["crema"], height=400)
        self.scroll_listas.pack_forget()
        imagen_tractor = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, 'Tractor x1.png')),
                                      size=(150, 100))

        # ?? Tractor
        self.tractor = ctk.CTkButton(
            self.ventana_maquinas,
            text="Tractor",
            font=('verdana', 20),
            image=imagen_tractor,
            text_color=colores["aguamarina"],
            fg_color=colores["crema"],
            hover_color=colores["marron"],
            command=lambda: [mostrar_botones(), ocultar(), mostrar_tractores(self.list_tractores)]
        )
        self.tractor.pack(pady=5)

        imagen_fumigador = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'tractor fumigador x1.png')),
            size=(150, 100))
        # ??Fumigador
        self.fumigador = ctk.CTkButton(self.ventana_maquinas,
                                       text='Fumigador',
                                       font=('verdana', 20),
                                       image=imagen_fumigador,
                                       text_color=colores["aguamarina"],
                                       fg_color=colores["crema"],
                                       hover_color=colores["marron"],
                                       command=lambda: [mostrar_botones(), ocultar(),
                                                        mostrar_fumigador(self.list_fumigadores)],
                                       width=200
                                       )
        self.fumigador.pack(pady=5)

        impagen_cosechador = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'tractor recolector x1.png')),
            size=(150, 100))
        # ??Cosechador
        self.cosechador = ctk.CTkButton(
            self.ventana_maquinas,
            text='Cosechador',
            font=('verdana', 20),
            image=impagen_cosechador,
            text_color=colores["aguamarina"],
            fg_color=colores["crema"],
            hover_color=colores["marron"],
            command=lambda: [mostrar_botones(), ocultar(), mostrar_cosechador(self.list_cosechadoras)])
        self.cosechador.pack(pady=5)

        # ?? Enviar maquina a trabjar

        self.boton_enviar_trabajar = ctk.CTkButton(
            self.ventana_maquinas,
            text="Enviar a Trabajar",
            command=self.abrir_seleccion_maquinas
        )
        self.boton_enviar_trabajar.pack(pady=10)

        # ?? Devolver
        self.devolver = ctk.CTkButton(self.ventana_maquinas,
                                      text='devolver',
                                      command=devolver
                                      )
        self.devolver.pack_forget()

    @staticmethod
    def clasificar_tipo_maquina(lista_maquinas):
        tractores = []
        fumigadores = []
        cosechadoras = []

        for x in lista_maquinas:
            if isinstance(x, Gestion.Tractor):
                tractores.append(x)
            elif isinstance(x, Gestion.Fumigador):
                fumigadores.append(x)
            elif isinstance(x, Gestion.Cosechador):
                cosechadoras.append(x)
            else:
                print(f"Advertencia: Tipo de máquina no reconocido: {type(x)}")

        return tractores, fumigadores, cosechadoras

    def abrir_seleccion_maquinas(self):
        VentanaSeleccionMaquinas(self.ventana_maquinas)

    def mostrar_historial(self, serial):
        nombre_archivo = f"historial_{serial}.txt"
        contenido = ""

        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
        except FileNotFoundError:
            contenido = "No hay historial registrado"

        ventana_historial = ctk.CTkToplevel(self.ventana_maquinas)
        ventana_historial.title(f"Historial - {serial}")
        ventana_historial.geometry("400x600")
        ventana_historial.resizable(False, True)

        scroll_frame = ctk.CTkScrollableFrame(ventana_historial, width=380, height=480)
        scroll_frame.pack(padx=10, pady=10, fill="both", expand=True)

        texto = ctk.CTkLabel(
            scroll_frame,
            text=contenido,
            justify="left",
            font=('verdana',12),
            wraplength=800
        )
        texto.pack()

        ctk.CTkButton(
            ventana_historial,
            text="Cerrar",
            command=ventana_historial.destroy
        ).pack(pady=5)

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


class VentanaSeleccionMaquinas(ctk.CTkToplevel):
    carpeta_master = os.path.dirname(__file__)
    carpeta_imagenes = os.path.join(carpeta_master, 'Imgen_interfaz')

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Seleccionar Máquinas para Trabajar")
        self.selecciones = []
        self.resizable(False, False)
        self.attributes('-topmost', True)
        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.configure(fg_color=colores["aguamarina"])

        # Frame deslizable
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=260, height=500)
        self.scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Cargar imágenes
        self.imagen_tractor = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(100, 100))
        self.imagen_fumigador = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(150, 100))
        self.imagen_cosechador = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(150, 100))  # !imagenes auxiliares, montar finales

        self.construir_listado()

    def obtener_estado_maquina(self, maquina):
        # Verificar si está en mantenimiento o reparación
        en_mantenimiento = any(m.maquina.get_serial() == maquina.get_serial()
                               for m in Gestion.maquinas_en_mantenimiento)
        en_reparacion = any(m.maquina.get_serial() == maquina.get_serial()
                            for m in Gestion.maquinas_en_reparacion)
        return not (en_mantenimiento or en_reparacion)

    def construir_listado(self):
        # Obtener y clasificar máquinas
        tractores = [m for m in Gestion.todas_las_maquinas if isinstance(m, Gestion.Tractor)]
        fumigadores = [m for m in Gestion.todas_las_maquinas if isinstance(m, Gestion.Fumigador)]
        cosechadoras = [m for m in Gestion.todas_las_maquinas if isinstance(m, Gestion.Cosechador)]

        # Crear tarjetas
        row = 0
        for tipo, maquinas, imagen in [
            ("Tractor", tractores, self.imagen_tractor),
            ("Fumigador", fumigadores, self.imagen_fumigador),
            ("Cosechador", cosechadoras, self.imagen_cosechador)
        ]:
            if maquinas:
                ctk.CTkLabel(self.scroll_frame, text=tipo,
                             font=("Arial", 14, "bold"), text_color=colores["crema"], ).grid(row=row, column=0, pady=10,
                                                                                             sticky="n")
                row += 1

                for maquina in maquinas:
                    frame = ctk.CTkFrame(self.scroll_frame, fg_color=colores["crema"])  # !quitar color de fondo
                    frame.grid(row=row, column=0, pady=5, padx=5, sticky="ew")

                    # Estado
                    disponible = self.obtener_estado_maquina(maquina)

                    # Imagen
                    ctk.CTkLabel(frame, image=imagen, text="", text_color=colores["aguamarina"]).grid(row=0, column=0,
                                                                                                      padx=10)

                    # Serial
                    ctk.CTkLabel(frame, text=maquina.get_serial(), text_color=colores["aguamarina"]).grid(row=1,
                                                                                                          column=0)

                    # Checkbox
                    var = ctk.BooleanVar()
                    chk = ctk.CTkCheckBox(frame, text="", variable=var)
                    chk.grid(row=0, column=1, padx=10)

                    if not disponible:
                        chk.configure(state="disabled")
                        frame.configure(fg_color="#3a3a3a")  # Color diferente para no disponibles

                    self.selecciones.append((maquina, var))
                    row += 1

        # Botón de confirmar
        btn_confirmar = ctk.CTkButton(self.scroll_frame, text="Confirmar Selección",
                                      command=self.confirmar_seleccion)
        btn_confirmar.grid(row=row, column=0, pady=20)
        btn_confirmar.configure(fg_color=colores["verdeclro"])

    def confirmar_seleccion(self):
        seleccionadas = [maquina for maquina, var in self.selecciones if var.get()]
        # Aquí llamarías a la lógica de Gestion para enviar a trabajar
        print("Máquinas seleccionadas:", [m.get_serial() for m in seleccionadas])

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
                Gestion.Mantenimiento.iniciar_mantenimiento(maquina)
            else:
                Gestion.Mantenimiento.reparar(maquina)

        messagebox.showinfo("Éxito", f"{len(seleccionados)} máquinas programadas para {self.tipo_accion.lower()}")
        self.destroy()


if __name__ == "__main__":
    Menu()