





from time import sleep
from tkinter import CENTER,StringVar
import customtkinter as ctk
import os
from PIL import Image,ImageTk

carpeta_master = os.path.dirname(__file__)
carpeta_imagenes = os.path.join(carpeta_master, 'Imgen_interfaz')
ctk.set_appearance_mode('dark')

class Menu:
    def __init__(self,):
        self.__ventana=ctk.CTk()
        self._text_preview = StringVar()
        #self.lista_maquinas=lista_maquina


        #configuracíon de ventana principal
        self.__ventana.title('Sistema de Gestión de Maquinaria')
        self.__ventana.geometry('500x800')
        self.__ventana.iconbitmap(os.path.join('Imgen_interfaz', 'icono.ico'))
        #configuracion de previe

        #? Titulo del menu
        titulo_imagen = ctk.CTkImage(light_image=Image.open(os.path.join(carpeta_imagenes, 'll.png')),
                                    size=(100, 100))
        titulo_ventana = ctk.CTkLabel(master=self.__ventana, image=titulo_imagen, text='titulo')

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
        Ventana2=Ventana_lista()


    def actualizar_preview_maquinas(self):
        pass
    def update_text(self):

        archivo = open('historial_C1.txt', 'r', encoding='utf-8')
        self._text_preview.set(archivo.read())
    def pl(self):
        pass
class Ventana_lista():
    def __init__(self,tipo_tractor):
        # ?Configuracioón ventana(lista de maquinas registradas)
        self.tipo_tractor=tipo_tractor
        self.ventana_maquinas = ctk.CTkToplevel()
        self.ventana_maquinas.geometry('300x400')  # ° Tamaño 2 vemtana
        self.ventana_maquinas.attributes('-topmost', True)

        # ? Funciones de segunda ventana
        def ocultar():# Oculta botones principales
            self.tractor.pack_forget()
            self.fumigador.pack_forget()
            self.cosechador.pack_forget()
        def mosrtrar_lista():
            self.devolver.pack_forget()
            self.tractor_lista.pack(pady=5)
            self.devolver.pack(pady=5)
        # ? Botones segunda ventana

        # ?? Tractor
        self.tractor= ctk.CTkButton(self.ventana_maquinas,
                                    text='prueba',
                                    command=lambda :[mosrtrar_lista(),ocultar()])
        self.tractor.pack(pady=5)

        #° lista de tractores

        self.tractor_lista=ctk.CTkScrollableFrame(self.ventana_maquinas,)
        self.tractor_lista.pack(pady=5)
        self.tractor_lista.pack_forget()
        self.tex_tractor=ctk.CTkLabel(self.tractor_lista,text='prueba',font=('Verdana',24))
        self.tex_tractor.pack(pady=5)

        # ??Fumigador
        self.fumigador = ctk.CTkButton(self.ventana_maquinas,
                                        text='prueba',
                                        command=ocultar,
                                        width=200
                                        )
        self.fumigador.pack(pady=5)


        # ??Cosechador
        self.cosechador = ctk.CTkButton(self.ventana_maquinas,
                                        text='prueba',
                                        command=ocultar)
        self.cosechador.pack(pady=5)


        #?? Devolver
        self.devolver=ctk.CTkButton(self.ventana_maquinas,
                                    text='devolver',
                                    )
        self.devolver.pack(pady=5)#° espaciado
if __name__ == "__main__":
    Menu()

