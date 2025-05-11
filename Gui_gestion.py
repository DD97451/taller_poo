import Gestion
from tkinter import CENTER,StringVar
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

        programar_mantenimiento = ctk.CTkButton(scroll_menu,
                                        image=listado_maquina_imagen,
                                        text='5', command=self.pl
                                        ).grid(row=2, column=0, padx=10,pady=10)


        reparar_maquinas = ctk.CTkButton(scroll_menu,
                                        image=listado_maquina_imagen,
                                        text='4', command=self.pl
                                        ).grid(row=3, column=0, padx=10,pady=10)


        avanzar_dia=ctk.CTkButton(scroll_menu,
                                        image=listado_maquina_imagen,
                                        text='ppl',
                                        command=self.pl
                                        ).grid(row=4, column=0, padx=10,pady=10)


        #?? COLUMNA 2

        #/* previsualización del listado de maquinas

        listado_maquina_preview = ctk.CTkScrollableFrame(master=scroll_menu,
                                                width=300,
                                                height=100,
                                                fg_color='blue')
        listado_maquina_preview.grid(row=0, column=1, padx=10)
        texto_previw_maquinas=ctk.CTkLabel(listado_maquina_preview,textvariable=self._text_preview).pack()

        #/* previsualización de tipo de maquinas a enviar a trabajar

        opciones_enviar_trabajar=ctk.CTkFrame(master=scroll_menu,
                                                width=300,
                                                height=100,
                                                fg_color='red')
        opciones_enviar_trabajar.grid(row=1, column=1, padx=10)
        boton_tractor=ctk.CTkButton(opciones_enviar_trabajar,
                                        text='54515').place(relx=1/3)
        boton_fumigador=ctk.CTkButton(opciones_enviar_trabajar,
                                        text='papapapa',
                                        width=50,
                                        height=50).place(relx=2/3)
        boton_cosechador=ctk.CTkButton(opciones_enviar_trabajar,
                                        text='adaswasd',
                                        width=50,
                                        height=50).place(relx=1 / 3,y=30)

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
        self.__ventana.mainloop()
    def mostrar_ventana_lista(self):
        VentanaLista()


    def actualizar_preview_maquinas(self):
        pass
    def update_text(self):

        archivo = open('historial_C1.txt', 'r', encoding='utf-8')
        self._text_preview.set(archivo.read())
    def pl(self):
        pass
class VentanaLista:
    list_tractores = []
    list_fumigadores = []
    list_cosechadoras = []
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
            self.tractor.pack()
            self.fumigador.pack()
            self.cosechador.pack()
            self.scroll_listas.pack_forget()
            self.devolver.pack_forget()
        def ocultar():# Oculta botones principales
            self.tractor.pack_forget()
            self.fumigador.pack_forget()
            self.cosechador.pack_forget()


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

            # Crear nuevos elementos
            self.title_lisatado = ctk.CTkLabel(self.scroll_listas, text='Tractores registrados', font=('verdana', 15))
            self.title_lisatado.pack()

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


if __name__ == "__main__":
    Menu()