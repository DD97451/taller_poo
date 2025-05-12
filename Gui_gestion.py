import Gestion
from tkinter import CENTER,StringVar,messagebox
import customtkinter as ctk
import os
from PIL import Image,ImageTk



#? Direcciones de las imagenes
carpeta_master = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_master, 'Imgen_interfaz')
ctk.set_appearance_mode('dark')

class Menu:
    def __init__(self):
        #self.tipo_tractor=tipo_tractor
        self.__ventana=ctk.CTk()
        self._text_preview = StringVar()



        #configuracíon de ventana principal
        self.__ventana.title('Sistema de Gestión de Maquinaria')
        self.__ventana.geometry('500x800')
        #self.__ventana.iconbitmap(os.path.join('Imgen_interfaz', 'icono.ico'))
        #configuracion de previe

        #? Titulo del menu
        titulo_imagen = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
                                    size=(100, 100))
        titulo_ventana = ctk.CTkLabel(master=self.__ventana,  text='titulo')

        #?Botones de elección
        scroll_menu=(ctk.CTkScrollableFrame(master=self.__ventana, width=600, height=600))
        scroll_menu.place(relx=0.5,rely=2.34/4,anchor=CENTER)
        #??COLUMNA 1
        listado_maquina_imagen=ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),#° imagen del titutlo de lista de maquinas
                                    size=(100, 100))
        lista_maquina=ctk.CTkButton(scroll_menu,
                                        image=listado_maquina_imagen,
                                        text='1',command=self.mostrar_ventana_lista
                                        ).grid(row=0,column=0,padx=10,pady=10)#!trabajando aqui
        titulo_ventana.pack()


        self.enviar_maquinas=(ctk.CTkButton(scroll_menu,
                                        image=listado_maquina_imagen,
                                        text='6',command=self.update_text()
                                        ))
        self.enviar_maquinas.grid(row=1,column=0,padx=10,pady=10)

        self.btn_mantenimiento = ctk.CTkButton(
            scroll_menu,
            image=listado_maquina_imagen,
            text="Programar Mantenimiento",
            command=self.abrir_mantenimiento
        )
        self.btn_mantenimiento.grid(row=2, column=0, padx=10, pady=10)

        self.btn_reparacion = ctk.CTkButton(
            scroll_menu,
            image=listado_maquina_imagen,
            text="Reparar Máquinas",
            command=self.abrir_reparacion
        )
        self.btn_reparacion.grid(row=3, column=0, padx=10, pady=10)



        avanzar_dia=ctk.CTkButton(scroll_menu,
                                        image=listado_maquina_imagen,
                                        text='ppl',
                                        command=self.pl
                                        ).grid(row=4, column=0, padx=10,pady=10)

        ver_tecnicos_btn = ctk.CTkButton(
            scroll_menu,
            text="👨🔧 Ver Técnicos",
            command=self.mostrar_ventana_tecnicos
        )
        ver_tecnicos_btn.grid(row=5, column=0, padx=10, pady=10)

        agregar_tecnico_btn = ctk.CTkButton(
            scroll_menu,
            text="➕ Agregar Técnico",
            command=self.mostrar_ventana_agregar_tecnico
        )
        agregar_tecnico_btn.grid(row=6, column=0, padx=10, pady=10)


        #?? COLUMNA 2

        #/* previsualización del listado de maquinas

        listado_maquina_preview = ctk.CTkScrollableFrame(master=scroll_menu,
                                                width=300,
                                                height=100,
                                                fg_color='blue')
        listado_maquina_preview.grid(row=0, column=1, padx=10)
        texto_previw_maquinas=ctk.CTkLabel(listado_maquina_preview,textvariable=self._text_preview).pack()

        #/* previsualización de programar mantenimiento

        opciones_mantenimiento = ctk.CTkFrame(master=scroll_menu,
                                                width=300,
                                                height=100,
                                                fg_color='red')
        opciones_mantenimiento.grid(row=2, column=1, padx=10)

        boton_tractor_mantenimieto = ctk.CTkButton(opciones_mantenimiento,
                                                    text='54515').place(relx=1 / 3)
        boton_fumigador_mantenimiento = ctk.CTkButton(opciones_mantenimiento,
                                                        text='papapapa',
                                                        width=50,
                                                        height=50).place(
            relx=2 / 3)
        boton_cosechador_mantenimiento = ctk.CTkButton(opciones_mantenimiento,
                                                        text='adaswasd',
                                                        width=50,
                                                        height=50).place(
            relx=1 / 3, y=30)

        # /* previsualización de reparar

        opciones_repar = ctk.CTkFrame(master=scroll_menu,
                                        width=300,
                                        height=100,
                                        fg_color='red')

        opciones_repar.grid(row=3, column=1, padx=10)

        tractor_reparar = ctk.CTkButton(opciones_repar,
                                                text='54515').place(relx=1 / 3)

        fumigador_reparar = ctk.CTkButton(opciones_repar,
                                                text='papapapa',
                                                width=50,
                                                height=50).place(relx=2 / 3)

        cosechador_reparar = ctk.CTkButton(opciones_repar,
                                                    text='adaswasd',
                                                    width=50,
                                                    height=50).place(relx=1 / 3, y=30)



        # /* previsualización de avanzar dia
        apartado_avanzar_dia = ctk.CTkFrame(master=scroll_menu,
                                        width=300,
                                        height=100,
                                        fg_color='red')

        apartado_avanzar_dia.grid(row=4, column=1, padx=10)

        boton_tractor_reparar = ctk.CTkLabel(apartado_avanzar_dia,
                                                text='54515').place(relx=1 / 3)

        agregar_maquina_btn = ctk.CTkButton(
            scroll_menu,
            text="➕ Agregar Máquina",
            command=self.mostrar_ventana_agregar
        )
        agregar_maquina_btn.grid(row=6, column=1, padx=10, pady=10)










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

    def pl(self):
        pass


class VentanaLista:
    def __init__(self):
        #super().__init__(tipo_tractor)
        #? Clasificar las máquinas
        self.list_tractores, self.list_fumigadores, self.list_cosechadoras = self.clasificar_tipo_maquina(Gestion.todas_las_maquinas)

        # ?Configuracioón ventana(lista de maquinas registradas)
        self.ventana_maquinas = ctk.CTkToplevel()
        self.ventana_maquinas.geometry('300x500')  # ° Tamaño 2 vemtana
        self.ventana_maquinas.attributes('-topmost', True)

        #?lista auxiliar


        # ? Funciones de segunda ventana
        def devolver():
            self.tractor.pack(pady=10)
            self.fumigador.pack(pady=10)
            self.cosechador.pack(pady=10)
            self.boton_enviar_trabajar.pack(pady=10)
            self.scroll_listas.pack_forget()
            self.devolver.pack_forget()

        def ocultar():# Oculta botones principales
            self.tractor.pack_forget()
            self.fumigador.pack_forget()
            self.cosechador.pack_forget()
            self.boton_enviar_trabajar.pack_forget()

        def mostrar_botones():
            self.scroll_listas.pack(pady=5)
            self.devolver.pack(pady=5)

        def mostrar_tractores(lista_maquinas):
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
            for n, tractor in enumerate(lista_maquinas, 1):
                label = ctk.CTkLabel(self.scroll_listas, text=f'{n}) {tractor.get_serial()}')
                label.pack()
                self.labels_seriales.append(label)

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
            for n, tractor in enumerate(lista_maquinas, 1):
                label = ctk.CTkLabel(self.scroll_listas, text=f'{n}) {tractor.get_serial()}')
                label.pack()
                self.labels_seriales.append(label)

        def mostrar_fumigador(lista_maquinas):
            # Limpiar widgets anteriores
            if hasattr(self, 'title_lisatado'):
                self.title_lisatado.destroy()
            if hasattr(self, 'labels_seriales'):
                for label in self.labels_seriales:
                    label.destroy()

            self.title_lisatado = ctk.CTkLabel(self.scroll_listas, text='Tractores registrados', font=('verdana', 15))
            self.title_lisatado.pack()
            #creacion automatica del listado
            self.labels_seriales = []
            for n, tractor in enumerate(lista_maquinas, 1):
                label = ctk.CTkLabel(self.scroll_listas, text=f'{n}) {tractor.get_serial()}')
                label.pack()
                self.labels_seriales.append(label)




        # ? Botones segunda ventana
        #?? Deslizable de lista de tractores
        self.scroll_listas = ctk.CTkScrollableFrame(self.ventana_maquinas, fg_color='purple',height=400)
        self.scroll_listas.pack_forget()
        # ?? Tractor
        self.tractor = ctk.CTkButton(
            self.ventana_maquinas,
            text='tractor',
            command=lambda: [mostrar_botones(), ocultar(), mostrar_tractores(self.list_tractores)]
        )
        self.tractor.pack(pady=5)

        # ??Fumigador
        self.fumigador = ctk.CTkButton(self.ventana_maquinas,
                                        text='fumigador',
                                        command=lambda :[mostrar_botones(),ocultar(),mostrar_fumigador(self.list_fumigadores)],
                                        width=200
                                        )
        self.fumigador.pack(pady=5)

        # ??Cosechador
        self.cosechador = ctk.CTkButton(
            self.ventana_maquinas,
            text='cosechador',
            command=lambda: [mostrar_botones(), ocultar(), mostrar_cosechador(self.list_cosechadoras)])
        self.cosechador.pack(pady=5)

        # ?? Enviar maquina a trabjar

        self.boton_enviar_trabajar = ctk.CTkButton(
            self.ventana_maquinas,
            text="Enviar a Trabajar",
            command=self.abrir_seleccion_maquinas
        )
        self.boton_enviar_trabajar.pack(pady=10)

        #?? Devolver
        self.devolver=ctk.CTkButton(self.ventana_maquinas,
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

class VentanaAgregarMaquina(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.acortadores=["Tractor", "Fumigador", "Cosechador"]

        #? configuración ventana
        self.title("Agregar Nueva Máquina")
        self.geometry("400x300")

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
        ctk.CTkButton(self, text="Registrar Máquina", command=self.validar_maquina).pack(pady=15)

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

        ctk.CTkButton(self, text="Registrar Técnico", command=self.validar_tecnico).pack(pady=15)

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
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Seleccionar Máquinas para Trabajar")
        self.selecciones = []

        # Configurar grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame deslizable
        self.scroll_frame = ctk.CTkScrollableFrame(self,width=260,height=500)
        self.scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Cargar imágenes
        self.imagen_tractor = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(100, 100))
        self.imagen_fumigador = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(100, 100))
        self.imagen_cosechador = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(100, 100))#!imagenes auxiliares, montar finales

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
                                font=("Arial", 14, "bold")).grid(row=row, column=0, pady=10, sticky="n")
                row += 1

                for maquina in maquinas:
                    frame = ctk.CTkFrame(self.scroll_frame,fg_color='red')#!quitar color de fondo
                    frame.grid(row=row, column=0, pady=5, padx=5, sticky="ew")

                    # Estado
                    disponible = self.obtener_estado_maquina(maquina)

                    # Imagen
                    ctk.CTkLabel(frame, image=imagen, text="").grid(row=0, column=0, padx=10)

                    # Serial
                    ctk.CTkLabel(frame, text=maquina.get_serial()).grid(row=1, column=0)

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
        self.tipo_accion = tipo_accion

        # Configurar grid principal
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame deslizable
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=780, height=500)
        self.scroll_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Configurar imágenes
        self.imagen_accion = ctk.CTkImage(
            light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
            size=(80, 80))

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
            ctk.CTkLabel(frame, image=self.imagen_accion, text="").grid(row=0, column=0, padx=10)

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