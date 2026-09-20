#!/usr/bin/env python3
"""Placa del testimonio de Denise M. (publicado tambien en hcarg.com.ar).

La cita de la placa es un recorte del testimonio completo: en Instagram una
cita de 9 renglones no se lee. El texto entero va en el caption, sin cortes.
Los puntos suspensivos marcan donde se recorto; no se cambio ninguna palabra.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from marca_hc import testimonio, guardar, ROSA

CITA = ("Podés facturar directamente desde la plataforma, con un solo botón "
        "y en segundos… Sin dudas, es de lo que más tiempo me ahorra.")

placas = [("hc38_testimonio_denise.png",
           testimonio(CITA, "D", "Lic. Denise M.", color_avatar=ROSA))]

guardar(placas, nombre_preview="preview_testimonio_denise.jpg", cols=1)
