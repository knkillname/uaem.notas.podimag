"""Materiales del curso de Procesamiento Digital de Imágenes.

Estas clases y funciones no son parte esencial del curso, pero pueden
ser útiles para realizar tareas comunes que forman parte de la
didáctica del curso.

Funciones
---------
descargar_sipi
    Descarga un volumen de la base de datos miscelánea de la USC-SIPI.
describir_imagen
    Produce una descripción textual de una imagen.

Tipos
-----
ArregloImagen
    Tipo de datos para arreglos de imágenes.
"""

from .tipos import ArregloImagen
from .sipi import descargar_sipi
from .descriptores import describir_imagen

__all__ = ["ArregloImagen", "descargar_sipi", "describir_imagen"]
