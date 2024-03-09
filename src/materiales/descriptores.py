"""Módulo para describir imágenes y arreglos de Numpy."""

import dataclasses
import textwrap
from collections.abc import Collection
from typing import Sequence

import numpy as np

from .tipos import ArregloImagen

PRECISION = "3.3g"


@dataclasses.dataclass
class DescriptorDeMuestra:
    """Descripción de una muestra de datos.

    Atributos
    ---------
    media : float
        Media de la muestra.
    desviacion : float
        Desviación estándar de la muestra.
    minimo : float | int
        Valor mínimo de la muestra.
    maximo : float | int
        Valor máximo de la muestra.
    """

    media: float
    desviacion: float
    minimo: float | int
    maximo: float | int

    def __str__(self) -> str:
        """Devuelve un texto con la descripción de la muestra."""
        # pylint: disable=consider-using-f-string
        msg = "{{:{0}}} ± {{:{0}}} en el intervalo ".format(PRECISION)
        if isinstance(self.minimo, int) and isinstance(self.maximo, int):
            msg += "[{{}}, {{}}]"
        else:
            msg += "[{{:{0}}}, {{:{0}}}]".format(PRECISION)

        msg = msg.format(self.media, self.desviacion, self.minimo, self.maximo)
        return msg


@dataclasses.dataclass
class DescriptorImagen:
    """Descripción de una imagen.

    Atributos
    ---------
    nombre : str
        Nombre de la imagen.
    ancho : int
        Ancho de la imagen.
    alto : int
        Alto de la imagen.
    canales : Sequence[str]
        Nombres de los canales de la imagen.
    tipo : type[np.integer] | type[np.floating] | type[np.bool_]
        Tipo de datos de la imagen.
    distribuciones : Sequence[DescriptorDeMuestra]
        Descripción de la distribución de los valores en los canales.
    """

    nombre: str
    ancho: int
    alto: int
    canales: Sequence[str]
    tipo: type[np.integer] | type[np.floating] | type[np.bool_]
    distribuciones: Sequence[DescriptorDeMuestra]

    def __str__(self) -> str:
        """Devuelve un texto con la descripción de la imagen."""
        n_canales = len(self.canales)
        tipo = self.tipo.__name__
        lineas = textwrap.wrap(
            f"{self.nombre} tiene tamaño {self.ancho}×{self.alto} "
            f"y {n_canales} canales de tipo {tipo}.",
            width=80,
        )
        canales = (
            map(str, range(self.canales))
            if isinstance(self.canales, int)
            else self.canales
        )
        for canal, distribucion in zip(canales, self.distribuciones):
            lineas.append(f"  - {canal}: {distribucion}")
        return "\n".join(lineas)

    def _markdown(self) -> str:
        """Devuelve un texto con la descripción de la imagen en formato Markdown."""
        return str(self)


def nombrar_canales(n_canales: int, tipo: type, inferir: bool = True) -> Sequence[str]:
    """Devuelve los nombres de los canales de una imagen.

    Si `inferir` es `True`, el nombre de los canales se infiere del tipo
    de la imagen.

    Parámetros
    ----------
    n_canales : int
        Número de canales de la imagen.
    tipo : type[np.integer] | type[np.floating] | type[np.bool_]
        Tipo de datos de la imagen.
    inferir : bool, opcional
        Si es `True`, el nombre de los canales se infiere del tipo de la imagen.

    Devuelve
    --------
    Sequence[str]
        Nombres de los canales de la imagen.
    """
    if inferir:
        if n_canales == 1:
            return ("Máscara",) if issubclass(tipo, np.bool_) else ("Gris",)
        elif n_canales == 3:
            return ("Rojo", "Verde", "Azul")
        elif n_canales == 4:
            return ("Rojo", "Verde", "Azul", "Alfa")
    return tuple(f"Canal {i}" for i in range(n_canales))


def construir_descripcion(
    nombre: str, imagen: ArregloImagen, canales: Collection[str] | bool = True
) -> DescriptorImagen:
    """Describe los atributos de una imagen.

    Parámetros
    ----------
    nombre : str
        Nombre de la imagen.
    imagen : ArregloImagen
        Imagen a describir.
    canales : Collection[str] | bool, opcional
        Nombres de los canales de la imagen. Si es `True`, se infieren
        del tipo de la imagen.

    Devuelve
    --------
    DescriptorImagen
        Descripción de la imagen.
    """
    if not isinstance(imagen, np.ndarray):
        raise ValueError("La imagen debe ser un arreglo de Numpy.")
    if imagen.ndim not in (2, 3):
        raise ValueError("El arreglo debe ser 2D o 3D.")
    if imagen.ndim == 2:
        imagen = imagen[..., np.newaxis]

    ancho, alto = imagen.shape[:2]
    n_canales = imagen.shape[2]
    tipo = imagen.dtype.type
    distribuciones = [
        DescriptorDeMuestra(
            media=imagen[..., i].mean(),
            desviacion=imagen[..., i].std(),
            minimo=imagen[..., i].min(),
            maximo=imagen[..., i].max(),
        )
        for i in range(n_canales)
    ]
    if isinstance(canales, bool):
        nom_canales = nombrar_canales(n_canales, tipo, inferir=canales)
    else:
        nom_canales = tuple(canales)

    return DescriptorImagen(
        nombre=nombre,
        ancho=ancho,
        alto=alto,
        canales=nom_canales,
        tipo=tipo,
        distribuciones=distribuciones,
    )


def describir_imagen(
    imagen: ArregloImagen,
    nombre: str = "Imagen",
    canales: Collection[str] | bool = True,
    imprimir: bool = True,
) -> str | None:
    """Produce una descripción textual de una imagen.

    Parámetros
    ----------
    imagen : ArregloImagen
        Imagen a describir.
    nombre : str, opcional
        Nombre de la imagen.
    canales : Collection[str] | bool, opcional
        Nombres de los canales de la imagen. Si es `True`, se infieren
        del tipo de la imagen.
    imprimir : bool, opcional
        Si es `True`, imprime la descripción en consola.

    Devuelve
    --------
    str | None
        Descripción de la imagen en texto plano. Si `imprimir` es `True`,
        la descripción se imprime en consola y se devuelve `None`.
    """
    desc = construir_descripcion(nombre, imagen, canales)
    if imprimir:
        print(desc)
        return None
    return str(desc)
