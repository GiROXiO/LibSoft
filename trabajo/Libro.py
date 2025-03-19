class Libro:

  def __init__(self, id, titulo, autor, year, genero, precio):
    self.id = id # Clave Primaria
    self.titulo = titulo
    self.autor = autor
    self.year = year
    self.genero = genero
    self.precio = precio

  def toStr(self):
    return f"{self.id},{self.titulo},{self.autor},{self.year},{self.genero},{self.precio}"