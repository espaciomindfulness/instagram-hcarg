#!/usr/bin/env python3
"""Dos creatividades para publicidad paga de @hcarg.app.

Por que estas dos y no otras: de las 20 publicaciones medidas, una sola
supero el 100% del alcance sobre la base — «Que NO conviene escribir en una
historia clinica», con 143%. Es la unica que Instagram mostro a gente que no
sigue la cuenta. Los posteos de producto (agenda, facturacion, prueba gratis)
quedaron todos entre 8% y 16%.

Asi que la apuesta A repite ese angulo —riesgo profesional, no
funcionalidades— y la B es el control directo de producto, para medir contra
algo. Testear dos y dejar correr a la que gane es mas barato que adivinar.

Formato 4:5: es el que mas pantalla ocupa en el feed.

Nota sobre el texto: estas placas tienen bastante. En anuncios, menos texto
suele rendir mejor. Si hay que recortar, se recorta el cuerpo, nunca el
titular ni el boton.
"""
from marca_hc import *


def a_riesgo():
    """El angulo que ya probo funcionar organicamente."""
    return cta(
        "Lo que no conviene escribir en una historia clínica",
        "Juicios de valor, datos de terceros, diagnósticos de apuro. Cuatro "
        "errores que el día que alguien más la lee se vuelven en contra.",
        "VER CÓMO REGISTRAR MEJOR", "HCARG.COM.AR", "teal")


def b_producto():
    """El control: oferta directa, sin rodeos."""
    return cta(
        "Historia clínica digital para psicólogos",
        "Cifrada en tu computadora, no en la nube. Agenda, facturación ARCA y "
        "reportes en un solo lugar. Dos pacientes gratis, sin tarjeta.",
        "PROBALO GRATIS", "HCARG.COM.AR", "rosa")


def main():
    guardar([("ad_a_riesgo.png", a_riesgo()),
             ("ad_b_producto.png", b_producto())],
            "preview_publicidad.jpg", cols=2)


if __name__ == "__main__":
    main()
