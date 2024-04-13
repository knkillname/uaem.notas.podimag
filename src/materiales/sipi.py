"""Funciones para trabajar con la base de datos de la USC-SIPI.

La base de datos de la Universidad del Sur de California (USC) contiene
imágenes digitales de texturas, imágenes aéreas, imágenes misceláneas y
secuencias de video. Los archivos están en formato .zip.

Funciones
---------
descargar_sipi(volumen: str, destino: Path = Path("sipi")) -> None
    Descarga un volumen de la base de datos miscelánea de la USC-SIPI.
"""

import enum
from pathlib import Path
from random import Random
import tempfile
import urllib.request
import zipfile


class Volumen(enum.StrEnum):
    """Volumen de la base de datos de la USC-SIPI."""

    TEXTURAS = "textures"
    AEREAS = "aerials"
    MISCELANEA = "misc"
    SECUENCIAS = "sequences"


def descargar_sipi(volumen: str | Volumen, destino: Path = Path("sipi")) -> None:
    """Descarga un volumen de la base de datos miscelánea de la USC-SIPI."""
    url = f"https://sipi.usc.edu/database/{volumen}.zip"
    volumen = Volumen(volumen)

    if (destino / volumen).exists():
        print(f"El volumen {volumen} ya existe en el directorio sipi.")
        return

    with tempfile.TemporaryFile() as temp:
        # Usamos un archivo temporal para la descarga
        print(f"Descargando {url}...")
        with urllib.request.urlopen(url) as response:
            temp.write(response.read())

        temp.seek(0)  # Reiniciar el puntero del archivo para leerlo

        with zipfile.ZipFile(temp) as z:
            print(f"Descomprimiendo {volumen}.zip...")
            z.extractall(destino)

    print(f"Volumen {volumen} descargado y descomprimido en {destino}.")


def ejemplo_sipi(rng=Random()) -> Path:
    """Selecciona un archivo arbitrario de la base de datos miscelánea de la USC-SIPI."""
    sipi = Path("sipi")
    if not sipi.exists():
        raise FileNotFoundError("No se encontró la base de datos de la USC-SIPI.")

    archivos = [
        archivo
        for archivo in sipi.rglob("*")
        if archivo.is_file() and archivo.suffix != ".zip"
    ]

    if not archivos:
        raise FileNotFoundError(
            "No se encontraron archivos en la base de datos de la USC-SIPI."
        )

    return rng.choice(archivos)
