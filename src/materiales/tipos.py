"""Tipos de datos para el módulo materiales."""

from typing import TypeAlias
import numpy as np
import numpy.typing as npt


ArregloImagen: TypeAlias = (
    npt.NDArray[np.integer] | npt.NDArray[np.floating] | npt.NDArray[np.bool_]
)
