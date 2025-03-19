import pandas as pd
from Libro import Libro
from Cliente import Cliente
from Venta import Venta

class LibSoft:

  def __init__(self, rutaLibros, rutaClientes, rutaVentas):
    self.rutaLibros = rutaLibros
    self.rutaClientes = rutaClientes
    self.rutaVentas = rutaVentas

    def registrarLibro():
      try:
        df = pd.read_csv(self.rutaLibros)
        id = input("Digite el id del libro: ")
        titulo = input("Digite el titulo del libro:")
        autor = input("Digite el autor del libro: ")
        year = input("Digite el año del libro: ")
        genero = input("Digite el genero del libro: ")
        precio = input("Digite el precio del libro: ")

        libro = Libro(id, titulo, autor, year, genero, precio)
        df.loc[len(df)] = libro.toStr()
        df.to_csv(self.rutaLibros, index=False)
        print("Libro registrado exitosamente")
      except:
        print("Error al registrar el libro")

    def modificarInfoLibro():
      try:
        op = 0
        change = False
        lista = ["titulo", "autor", "año", "genero", "precio"]
        df = pd.read_csv(self.rutaLibros)
        id = input("Digite el id del libro que desea modificar: ")

        if df.loc[df['id'] == id].empty:
          print("El libro no existe")
          return

        while op != 6:
          print("1. Modificar titulo")
          print("2. Modificar autor")
          print("3. Modificar año")
          print("4. Modificar genero")
          print("5. Modificar precio")
          print("6. Salir")
          op = int(input("Digite la opcion que desea modificar: "))

          if op in range(1,6):
            df.loc[df['id'] == id, lista[op-1]] = input(f"Digite el nuevo {lista[op-1]}: ")
            change = True

          elif op == 6:
            if change:
              df.to_csv(self.rutaLibros, index=False)
              print("Libro modificado exitosamente")
            return
          else:
            print("Opcion invalida")
      except:
        print("Error al modificar el libro")

    def eliminarLibro():
      try:
        df = pd.read_csv(self.rutaLibros)
        id = input("Digite el id del libro que desea eliminar: ")

        if df.loc[df['id'] == id].empty:
          print("El libro no existe")
          return
        df.drop(df.loc[df['id'] == id].index, inplace=True)
        df.to_csv(self.rutaLibros, index=False)
        print("Libro eliminado exitosamente")
      except:
        print("Error al eliminar el libro")


    def registrarCliente():
      try:
        df = pd.read_csv(self.rutaClientes)
        id = input("Digite el id del cliente: ")
        nombre = input("Digite el nombre del cliente: ")
        apellido = input("Digite el apellido del cliente: ")
        correo = input("Digite el correo del cliente: ")
        direccion = input("Digite la direccion del cliente: ")

        cliente = Cliente(id, nombre, apellido, correo, direccion)
        df.loc[len(df)] = cliente.toStr()
        df.to_csv(self.rutaClientes, index=False)
        print("Cliente registrado exitosamente")
      except:
        print("Error al registrar el cliente")

    def modificarInfoCliente():
      try:
        op = 0
        change = False
        lista = ["nombre", "apellido", "correo", "direccion"]
        df = pd.read_csv(self.rutaClientes)
        id = input("Digite el id del cliente que desea modificar: ")

        if df.loc[df['id'] == id].empty:
          print("El cliente no existe")
          return

        while op != 5:
          print("1. Modificar nombre")
          print("2. Modificar apellido")
          print("3. Modificar correo")
          print("4. Modificar direccion")
          print("5. Salir")
          op = int(input("Digite la opcion que desea modificar: "))

          if op in range(1,4):
            df.loc[df['id'] == id, lista[op-1]] = input(f"Digite el nuevo {lista[op-1]}: ")
            change = True
          elif op == 5:
            if change:
              df.to_csv(self.rutaLibros, index=False)
              print("Cliente editado exitosamente")
            return
          else:
            print("Opcion invalida")
      except:
        print("Error al modificar el cliente")

    def registrarVenta():
      try:
        df = pd.read_csv(self.rutaVentas)
        idVenta = input("Digite el id de la venta: ")
        idCliente = input("Digite el id del cliente: ")
        idLibro = input("Digite el id del libro: ")
        fechaVenta = input("Digite la fecha de la venta: ")

        venta = Venta(idVenta, idCliente, idLibro, fechaVenta)
        df.loc[len(df)] = venta.toStr()
        df.to_csv(self.rutaVentas, index=False)
        print("Venta registrada exitosamente")
      except:
        print("Error al registrar la venta")

    def consultarVentas():
      try:
        df = pd.read_csv(self.rutaVentas)
        idVenta = input("Digite el id de la venta: ")
        print(df.loc[df['idVenta'] == idVenta])
      except:
        print("Error al consultar las ventas")