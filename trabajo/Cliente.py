class Cliente:

  def __init__(self, id, nombre, apellido, correo, direccion):
    self.id = id # Clave Primaria
    self.nombre = nombre
    self.apellido = apellido
    self.correo = correo
    self.direccion = direccion

  def toStr(self):
    return f"{self.id},{self.nombre},{self.apellido},{self.correo},{self.direccion}"