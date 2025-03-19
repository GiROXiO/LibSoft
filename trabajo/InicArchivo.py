import os
import pandas as pd

def verifArchivo(nombreArchivo, columnas):
    carpeta = "data"
    ruta = os.path.join(carpeta,nombreArchivo)
    
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
        print(f"Carpeta {carpeta} creada exitosamente")
        
    if not os.path.exists(ruta):
        print(f"El archivo {ruta} no existe, creandolo...")
        df = pd.DataFrame(columns=columnas)
        df.to_csv(ruta, index = False)
        print(f"Archivo {ruta} creado exitosamente")
    else:
        print(f"El archivo {ruta} ya existe")
        
    return ruta