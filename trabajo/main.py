import flet as ft
import pandas as pd
import matplotlib.pyplot  as plt
import numpy as np

from Libro import Libro
from Cliente import Cliente
from Venta import Venta

def main(page: ft.Page):
    rutaLibros = "C:/libsoftcsv/libros.csv"
    rutaClientes = "C:/libsoftcsv/clientes.csv"
    rutaVentas = "C:/libsoftcsv/ventas.csv"
    

    page.bgcolor = "#383838"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "LibSoft" 
    

    ####################### Seccion Bienvenida ##########################

    bienvenida = ft.Container(
        content=ft.Column([
            ft.Text("📚 ¡Bienvenido a LibSoft! 📚", 
                    size=30, 
                    weight="bold", 
                    color="black",
                    text_align=ft.TextAlign.CENTER),
            ft.Text("La mejor solución para gestionar libros, clientes y ventas.", 
                    size=18, 
                    italic=True, 
                    color="black",
                    text_align=ft.TextAlign.CENTER),
            ft.Divider(height=15, thickness=1, color="gray"),  # Línea divisoria sutil
            ft.Row([
                ft.Icon(name=ft.icons.BOOK, size=35, color="blue"),
                ft.Icon(name=ft.icons.PEOPLE, size=35, color="green"),
                ft.Icon(name=ft.icons.SELL, size=35, color="red"),
            ], alignment=ft.MainAxisAlignment.CENTER)
        ], 
        spacing=15, 
        alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=40,
        alignment=ft.alignment.center,
        border=ft.border.all(2, "black"),  # Borde elegante
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.GREY_600, spread_radius=3),
        width=500
    )

    #####################################################################

    ####################### Sección Libros ############################
    
    idField_libro = ft.TextField(hint_text="Ingrese el ID del libro")
    tituloField_libro = ft.TextField(hint_text="Ingrese el titulo del libro")
    autorField_libro = ft.TextField(hint_text="Ingrese el nombre del autor del libro")
    yearField_libro = ft.TextField(hint_text="Ingrese el año de publicación del libro")
    generoField_libro = ft.TextField(hint_text="Ingrese el género del libro")
    precioField_libro = ft.TextField(hint_text="Ingrese el precio del libro")
    textoAvisoLibroR = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    textoAvisoLibroM = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    textoAvisoLibroE = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    textoAvisoClienteR = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    textoAvisoClienteE = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    textoAvisoVentaR = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    textoAvisoVentaC = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    datos_libro = ft.Column([
        ft.Row([
            ft.Text("Titulo"),
            tituloField_libro
        ]),
        ft.Row([
            ft.Text("Autor"),
            autorField_libro
        ]),
        ft.Row([
            ft.Text("Año"),
            yearField_libro
        ]),
        ft.Row([
            ft.Text("Género"),
            generoField_libro
        ]),
        ft.Row([
            ft.Text("Precio"),
            precioField_libro
        ]),
        
    ])

    fieldsRegistro_libro = [
        tituloField_libro,
        autorField_libro,
        yearField_libro,
        generoField_libro,
        precioField_libro
    ]

    def vaciarFields(fields):
        for field in fields:
            field.value = ""
    
    # --------------------------- Registrar -----------------------------------------#
    datosRegistro_libro = ft.Column([
        ft.Text("Registrar libro", size=24),
        datos_libro,
        ft.FilledButton("Registrar libro", on_click=lambda _: registrar_libro()),
        textoAvisoLibroR
    ])

   
    def registrar_libro():
        dfLibros = pd.read_csv(rutaLibros)
        try:
            print("Ok")
            change = True
            for field in fieldsRegistro_libro:
                if not field.value.strip():
                    change = False
            idLibro = 1
            try:
                idLibro = dfLibros.iloc[-1, 0] + 1
            except:
                print("Primer libro")
            if change:
                libro = Libro(idLibro, 
                            tituloField_libro.value.strip(), 
                            autorField_libro.value.strip(), 
                            int(yearField_libro.value.strip()), 
                            generoField_libro.value.strip(), 
                            float(precioField_libro.value.strip()))
                
                vaciarFields(fieldsRegistro_libro)

                dfLibros.loc[len(dfLibros)] = libro.toStr().split(",")
                dfLibros.to_csv(rutaLibros, index=False)
                textoAvisoLibroR.value = "Libro registrado exitosamente"

                page.update()
            else:
                textoAvisoLibroR.value = "Por favor, rellene todos los campos"
                page.update()
        except:
            textoAvisoLibroR.value = "Por favor, rellene los campos correctamente"
            page.update()

    
                

    ####################################################################

    # ---------------------- Modificar ----------------------------#

    datosModificarLibro = ft.Column([  
        ft.Text("Modificar libro", size=24),
        ft.Row([
            ft.Text("ID"),
            idField_libro
        ]),
        ft.Text("Rellene los aspectos que quiera modificar", size=18),
        datos_libro, 
        ft.FilledButton("Guardar cambios", on_click=lambda _: modificar_libro(int(idField_libro.value))),
        textoAvisoLibroM
    ])  # Esto permite que tome todo el espacio disponible

    
    def modificar_libro(id):
        try:
            dfLibros = pd.read_csv(rutaLibros)
            change = False
            idExist = True
            for field in fieldsRegistro_libro:
                if field.value.strip():
                    change = True
            if id not in dfLibros["id"].tolist():
                idExist = False
                print(dfLibros["id"].tolist())

            if change and idExist:
                if len(tituloField_libro.value.strip()) != 0:
                    dfLibros.loc[dfLibros['id'] == id, "titulo"] = tituloField_libro.value
                if len(autorField_libro.value.strip()) != 0:
                    dfLibros.loc[dfLibros['id'] == id, "autor"] = autorField_libro.value 
                if len(yearField_libro.value.strip()) != 0:
                    dfLibros.loc[dfLibros['id'] == id, "año"] = yearField_libro.value
                if len(generoField_libro.value.strip()) != 0:
                    dfLibros.loc[dfLibros['id'] == id, "genero"] = generoField_libro.value
                if len(precioField_libro.value.strip()) != 0:
                    dfLibros.loc[dfLibros['id'] == id, "precio"] = precioField_libro.value
                dfLibros.to_csv(rutaLibros, index=False)
                textoAvisoLibroM.value = "Libro modificado correctamente"
                page.update()
            else:
                if not change and idExist:
                    textoAvisoLibroM.value = "No ha llenado ningún campo para modificar"
                elif not idExist and change:
                    textoAvisoLibroM.value = "El ID no existe"
                else:
                    textoAvisoLibroM.value = "No ha llenado ningún campo para modificar y el ID no existe"
                page.update()
        except:
            textoAvisoLibroM.value = "El ID del libro no existe"
            page.update()

    ####################################################################

    # ---------------------- Eliminar ----------------------------# 

    datosEliminar_libro = ft.Column([
        ft.Text("Eliminar libro", size=24),
        ft.Row([
            ft.Text("ID"),
            idField_libro
        ]),
        ft.FilledButton("Eliminar libro", on_click=lambda _: eliminar_libro()),
        textoAvisoLibroE
    ])

    def eliminar_libro():
        dfLibros = pd.read_csv(rutaLibros)
        idExist = int(idField_libro.value.strip()) in dfLibros["id"].tolist()
        if idExist:
            dfLibros.drop(dfLibros.loc[dfLibros['id'] == int(idField_libro.value.strip())].index, inplace=True)
            dfLibros.to_csv(rutaLibros, index=False)
            textoAvisoLibroE.value = "Libro eliminado exitosamente"
        else:
            textoAvisoLibroE.value = "El ID no existe"
        page.update()



    ####################################################################

    ####################### Sección Clientes ############################

    idField_cliente = ft.TextField(hint_text="Ingrese el id del cliente")
    nombreField_cliente = ft.TextField(hint_text="Ingrese el nombre del cliente")
    apellidoField_cliente = ft.TextField(hint_text="Ingrese el apellido del cliente")
    correoField_cliente = ft.TextField(hint_text="Ingrese el correo del cliente")
    direccionField_cliente = ft.TextField(hint_text="Ingrese la direccion del cliente")

    datos_cliente = ft.Column([
        ft.Row([
            ft.Text("Nombre"),
            nombreField_cliente
        ]),
        ft.Row([
            ft.Text("Apellido"),
            apellidoField_cliente
        ]),
        ft.Row([
            ft.Text("Correo"),
            correoField_cliente
        ]),
        ft.Row([
            ft.Text("Dirección"),
            direccionField_cliente
        ]),
    ])

    fieldsRegistro_cliente = [
        nombreField_cliente,
        apellidoField_cliente,
        correoField_cliente,
        direccionField_cliente
    ]

    # ---------------------- Registrar ----------------------------# 

    datosRegistro_cliente = ft.Column([
            ft.Text("Registrar cliente", size=24),
            datos_cliente,
            ft.FilledButton("Registrar cliente", on_click=lambda _: registrar_cliente()),
            textoAvisoClienteR
        ])

   
    def registrar_cliente():
        try:
            dfClientes = pd.read_csv(rutaClientes)
            change = True
            for field in fieldsRegistro_cliente:
                if not field.value.strip():
                    change = False
            
            idCliente = 1
            try:
                idCliente = dfClientes.iloc[-1, 0] + 1
            except:
                print("Primer cliente")

            if change:
                cliente = Cliente(idCliente, 
                            nombreField_cliente.value.strip(), 
                            apellidoField_cliente.value.strip(), 
                            correoField_cliente.value.strip(), 
                            direccionField_cliente.value.strip())
                print("Bien")
                vaciarFields(fieldsRegistro_cliente)
                
                dfClientes.loc[len(dfClientes)] = cliente.toStr().split(",")
                dfClientes.to_csv(rutaClientes, index=False)
                textoAvisoClienteR.value = "Cliente registrado exitosamente"
                page.update()
            else:
                textoAvisoClienteR.value = "Por favor, rellene todos los campos"
                page.update()
        except:
            textoAvisoClienteR.value = "Por favor, rellene los campos correctamente"
            page.update()


    # -----------------------------------------------------------------
    # ---------------------- Editar ----------------------------#

    datosModificarCliente = ft.Column([  
        ft.Text("Editar cliente", size=24),
        ft.Row([
            ft.Text("ID"),
            idField_cliente
        ]),
        ft.Text("Rellene los aspectos que quiera modificar", size=18),
        datos_cliente, 
        ft.FilledButton("Guardar cambios", on_click=lambda _: modificar_cliente(int(idField_cliente.value))),
        textoAvisoClienteE
    ], expand=False)  # Esto permite que tome todo el espacio disponible


    def modificar_cliente(id):
        try:
            dfClientes = pd.read_csv(rutaClientes)
            change = False
            idExist = True
            for field in fieldsRegistro_libro:
                if field.value.strip():
                    change = True
            if id not in dfClientes["id"].tolist():
                idExist = False

            if change and idExist:
                if len(tituloField_libro.value.strip()) != 0:
                    dfClientes.loc[dfClientes['id'] == id, "nombre"] = nombreField_cliente.value
                if len(autorField_libro.value.strip()) != 0:
                    dfClientes.loc[dfClientes['id'] == id, "apellido"] = apellidoField_cliente.value 
                if len(yearField_libro.value.strip()) != 0:
                    dfClientes.loc[dfClientes['id'] == id, "correo"] = correoField_cliente.value
                if len(generoField_libro.value.strip()) != 0:
                    dfClientes.loc[dfClientes['id'] == id, "direccion"] = direccionField_cliente.value
                dfClientes.to_csv(rutaLibros, index=False)
                textoAvisoClienteE.value = "Cliente editado correctamente"
                page.update()
            else:
                if not change and idExist:
                    textoAvisoClienteE.value = "No ha llenado ningún campo para modificar"
                elif not idExist and change:
                    textoAvisoClienteE.value = "El ID no existe"
                else:
                    textoAvisoClienteE.value = "No ha llenado ningún campo para modificar y el ID no existe"
                page.update()
        except:
            textoAvisoClienteE.value = "El ID del cliente no existe"
            page.update()
    #############################################################

    def verGraficaLibro():
        pass


    tabsLibro = ft.Tabs(
        selected_index=0, # Cuando se inicie la app, en que pestaña va a iniciarse
        animation_duration=100, # Al cambiar de pestaña, cuanto se tarda en cambiarla
        tabs=
        [
            ft.Tab(text = "Registrar libro", icon=ft.icons.APP_REGISTRATION, content=ft.Row([datosRegistro_libro],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Modificar libro", icon=ft.icons.DRAW, content=ft.Row([datosModificarLibro],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Eliminar libro", icon=ft.icons.DELETE, content=ft.Row([datosEliminar_libro],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Gráfico", icon=ft.icons.GRAPHIC_EQ, content=ft.Row([ft.Text("Libros más vendidos", size=24),ft.FilledButton("Ver gráfica", on_click=lambda _: verGraficaLibro())],alignment=ft.MainAxisAlignment.CENTER)),
        ],
        expand=1, # Contenedor ajustandose al ancho de su contenedor padre (en este caso, la página como tal)
    )

    def verGraficaCliente():


        pass

    tabsCliente = ft.Tabs(
        selected_index=0, # Cuando se inicie la app, en que pestaña va a iniciarse
        animation_duration=100, # Al cambiar de pestaña, cuanto se tarda en cambiarla
        tabs=
        [
            ft.Tab(text = "Registrar Cliente", icon=ft.icons.APP_REGISTRATION, content=ft.Row([datosRegistro_cliente],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Editar cliente", icon=ft.icons.DRAW, content=ft.Row([datosModificarCliente],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Gráfico", icon=ft.icons.GRAPHIC_EQ, content=ft.Row([ft.Text("Clientes con más compras realizadas"),ft.FilledButton("Ver gráfica", on_click=lambda _: verGraficaCliente())],alignment=ft.MainAxisAlignment.CENTER)),
        ],
        expand=1, # Contenedor ajustandose al ancho de su contenedor padre (en este caso, la página como tal)
    )

    

    ####################### Sección Ventas ############################

    idVField_venta = ft.TextField(hint_text="Ingrese el id de la venta")
    idCField_venta = ft.TextField(hint_text="Ingrese el id del cliente")
    idLField_venta = ft.TextField(hint_text="Ingrese el id del libro")
    fecha_venta = ft.TextField(hint_text="Ingrese la fecha de la venta")

    fieldsRegistro_venta = [
        idCField_venta,
        idLField_venta,
        fecha_venta
    ]

    datos_venta = ft.Column([
        ft.Row([
            ft.Text("ID Cliente"),
            idCField_venta
        ]),
        ft.Row([
            ft.Text("ID Libro"),
            idLField_venta
        ]),
        ft.Row([
            ft.Text("Fecha"),
            fecha_venta
        ]),
        
    ])
    # ----------------------- Registrar venta ----------------------- #

    def registrar_venta():
        try:
            dfVenta = pd.read_csv(rutaVentas)
            dfCliente = pd.read_csv(rutaClientes)
            dfLibro = pd.read_csv(rutaLibros)
            change = True
            for field in fieldsRegistro_venta:
                if not field.value.strip():
                    change = False
           
            if change:
                if int(idCField_venta.value.strip()) in dfCliente["id"].tolist() and int(idLField_venta.value.strip()) in dfLibro["id"].tolist():
                    
                    idVenta = 1
                    try:
                        idVenta = dfVenta.iloc[-1, 0] + 1
                    except:
                        print("Primera venta")

                    venta = Venta(idVenta, 
                                int(idCField_venta.value.strip()), 
                                int(idLField_venta.value.strip()), 
                                fecha_venta.value.strip())
                    print("Bien")
                    vaciarFields(fieldsRegistro_venta)
                    
                    dfVenta.loc[len(dfVenta)] = venta.toStr().split(",")
                    dfVenta.to_csv(rutaVentas, index=False)
                    textoAvisoVentaR.value = "Venta registrada exitosamente"
                    page.update()
                else:
                    if int(idCField_venta.value.strip()) not in dfCliente["id"].tolist():
                        textoAvisoVentaR.value = "El ID del cliente no existe"
                    else:
                        textoAvisoVentaR.value = "El ID del libro no existe"
                    page.update()
            else:
                textoAvisoVentaR.value = "Por favor, rellene todos los campos"
                page.update()
        except:
            textoAvisoVentaR.value = "Por favor, rellene los campos correctamente"
            page.update()

    datosRegistro_venta = ft.Column([
            ft.Text("Registrar venta", size=24),
            datos_venta,
            ft.FilledButton("Registrar venta", on_click=lambda _: registrar_venta()),
            textoAvisoVentaR
        ])

    
    ##################################################################################

    # ----------------------- Consultar venta ----------------------- #
    columnas = [
        ft.DataColumn(ft.Text("ID de venta")),
        ft.DataColumn(ft.Text("Nombre del vendedor")),
        ft.DataColumn(ft.Text("Apellido del vendedor")),
        ft.DataColumn(ft.Text("Titulo del libro")),
        ft.DataColumn(ft.Text("Precio del libro"))
    ]
    tabla = ft.DataTable(columns=columnas)

    datosConsultarVenta = ft.Column([  
        ft.Text("Consultar venta", size=24),
        ft.Row([
            ft.Text("ID"),
            idVField_venta
        ]),
        ft.FilledButton("Consultar", on_click=lambda _: consultarVenta(int(idVField_venta.value.strip()))),
        tabla,
        textoAvisoVentaC
    ])  # Esto permite que tome todo el espacio disponible

    
    def consultarVenta(id):
        try:
            dfVenta = pd.read_csv(rutaVentas)
            dfCliente = pd.read_csv(rutaClientes)
            dfLibro = pd.read_csv(rutaLibros)
            filas = []
            if id in dfVenta["IdVenta"]:
                idLibro = int(dfVenta.loc[dfVenta['IdVenta'] == id, "IdLibro"])
                idCliente = int(dfVenta.loc[dfVenta['IdVenta'] == id, "IdCliente"])

                filas.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(id)),
                    ft.DataCell(ft.Text(dfCliente.loc[dfCliente['id'] == idCliente, "nombre"].values[0])),
                    ft.DataCell(ft.Text(dfCliente.loc[dfCliente['id'] == idCliente, "apellido"].values[0])),
                    ft.DataCell(ft.Text(dfLibro.loc[dfLibro['id'] == idLibro, "titulo"].values[0])),
                    ft.DataCell(ft.Text(dfLibro.loc[dfLibro['id'] == idLibro, "precio"].values[0]))
                ]),)
                print("Bien")
                tabla.rows = filas
                page.update()
                #dfClientes.loc[dfClientes['id'] == id, "nombre"]
            else:
                textoAvisoVentaC.value = "No existe ese ID de venta"
                page.update()
        except:
            textoAvisoVentaC.value = "Digite un ID valido"
            page.update()
            


    ####################################################################

    def verGraficaVentas():
        # Crear valores de x desde 0 hasta 2π
        t = np.linspace(0, 2*np.pi, 100)

        # Calcular seno y coseno
        y1 = np.sin(t)
        y2 = np.cos(t)

        # Crear la gráfica
        plt.figure(figsize=(8, 5))
        plt.plot(t, y1, label='Seno', color='b', linestyle='-')
        plt.plot(t, y2, label='Coseno', color='r', linestyle='--')

        # Agregar etiquetas y título
        plt.xlabel('Ángulo (radianes)')
        plt.ylabel('Valor')
        plt.title('Funciones Seno y Coseno')
        plt.legend()
        plt.grid()

        # Mostrar la gráfica
        plt.show()



    tabsVenta = ft.Tabs(
        selected_index=0, # Cuando se inicie la app, en que pestaña va a iniciarse
        animation_duration=100, # Al cambiar de pestaña, cuanto se tarda en cambiarla
        tabs=
        [
            ft.Tab(text = "Registrar venta", icon=ft.icons.APP_REGISTRATION, content=ft.Row([datosRegistro_venta],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Consultar venta", icon=ft.icons.DRAW, content=ft.Row([datosConsultarVenta],alignment=ft.MainAxisAlignment.CENTER)),
            ft.Tab(text = "Gráfico", icon=ft.icons.GRAPHIC_EQ, content=ft.Row([ft.Text("Ventas según intervalos de tiempo"),ft.FilledButton("Ver gráfica", on_click=lambda _: verGraficaVentas())],alignment=ft.MainAxisAlignment.CENTER)),
        ],
        expand=1, # Contenedor ajustandose al ancho de su contenedor padre (en este caso, la página como tal)
    )

    ###################################################################

    tabsPrincipal = ft.Tabs(
        selected_index=0, # Cuando se inicie la app, en que pestaña va a iniciarse
        animation_duration=300, # Al cambiar de pestaña, cuanto se tarda en cambiarla
        tab_alignment=ft.TabAlignment.START,
        tabs=
        [
            ft.Tab(text = "Bienvenida", icon=ft.icons.LIBRARY_ADD, content=bienvenida),
            ft.Tab(text = "Libros", icon=ft.icons.BOOK, content=tabsLibro),
            ft.Tab(text = "Clientes", icon=ft.icons.PERSON, content=tabsCliente),
            ft.Tab(text = "Ventas", icon=ft.icons.SELL, content=tabsVenta)

        ],
        expand=1, # Contenedor ajustandose al ancho de su contenedor padre (en este caso, la página como tal)
    )

    page.add(tabsPrincipal)


ft.app(target=main)