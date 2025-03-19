class Venta:

  def __init__(self, IDVenta, IDCliente, IDLibro, fechaVenta):
    self.IDCliente = IDCliente
    self.IDVenta = IDVenta #Clave Primaria
    self.IDLibro = IDLibro
    self.fechaVenta = fechaVenta

  def toStr(self):
    return f"{self.IDVenta},{self.IDCliente},{self.IDLibro},{self.fechaVenta}"