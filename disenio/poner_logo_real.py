#!/usr/bin/env python3
"""Reemplaza el isotipo dibujado por el archivo real del logo de HC ARG.

Yo venia dibujando la flor por codigo con proporciones inventadas: los petalos
quedaban pegados entre si y al centro. El logo real los tiene separados, con
aire. Se nota.

Este script tapa el isotipo viejo con el color de fondo de la placa y pega
encima el archivo real (contenido/marca/isotipo_hcarg.png). Sobre los fondos
teal y rosa el logo va sobre un disco blanco, porque si no sus petalos teal
desaparecen contra el fondo.
"""
from collections import Counter
from pathlib import Path
from PIL import Image, ImageDraw

RAIZ = Path(r"C:/Users/chris/OneDrive/Desktop/PROYECTO HC ARG/HC ARG - Marketing/instagram")
ORIGINALES = RAIZ / "contenido" / "originales"
LOGO = Image.open(RAIZ / "contenido" / "marca" / "isotipo_hcarg.png").convert("RGBA")

# Donde cada tipo de placa dibujaba el isotipo: centro y radio del dibujo viejo.
POSICIONES = [(540, 190, 62), (540, 186, 58), (540, 180, 56), (92, 66, 40)]


def hay_isotipo(im, cx, cy, r):
    """Detecta el isotipo viejo: centro teal oscuro (dibujado) o blanco (chapa)."""
    if not (r < cx < im.width - r and r < cy < im.height - r):
        return False
    # El isotipo siempre tiene el centro en teal oscuro (#1D6A66). Buscar
    # "algo blanco" daba falsos positivos: el fondo crema tambien es casi blanco
    # y terminaba pintando logos en placas interiores que no llevan.
    c = im.getpixel((cx, cy))[:3]
    return abs(c[0] - 29) < 34 and abs(c[1] - 106) < 34 and abs(c[2] - 102) < 34


def color_de_fondo(im, cx, cy, r):
    """El color que rodea al isotipo, para poder taparlo sin dejar cerco."""
    import math
    muestras = []
    for i in range(12):
        ang = math.radians(i * 30)
        x = int(cx + r * 1.85 * math.cos(ang))
        y = int(cy + r * 1.85 * math.sin(ang))
        if 0 <= x < im.width and 0 <= y < im.height:
            muestras.append(im.getpixel((x, y))[:3])
    return Counter(muestras).most_common(1)[0][0] if muestras else (255, 255, 255)


def es_fondo_oscuro(color):
    return sum(color) / 3 < 215


def poner(im, cx, cy, r):
    fondo = color_de_fondo(im, cx, cy, r)
    capa = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)

    # 1. tapamos el isotipo viejo con el color del fondo
    r_tapa = r * 1.55
    d.ellipse([cx - r_tapa, cy - r_tapa, cx + r_tapa, cy + r_tapa], fill=fondo + (255,))

    # 2. sobre fondo de color, disco blanco para que el logo se lea
    radio_logo = r * 0.86
    if es_fondo_oscuro(fondo):
        r_disco = r * 1.30
        d.ellipse([cx - r_disco, cy - r_disco, cx + r_disco, cy + r_disco],
                  fill=(255, 255, 255, 255))
    else:
        radio_logo = r * 1.05     # sobre fondo claro va suelto y puede ser mas grande

    im.alpha_composite(capa)

    # 3. el logo real, en sus colores
    lado = int(radio_logo * 2)
    logo = LOGO.resize((lado, lado), Image.LANCZOS)
    im.alpha_composite(logo, (cx - lado // 2, cy - lado // 2))


def main():
    tocadas = 0
    for ruta in sorted(ORIGINALES.glob("hc*.png")):
        im = Image.open(ruta).convert("RGBA")
        cambio = False
        for cx, cy, r in POSICIONES:
            if hay_isotipo(im, cx, cy, r):
                poner(im, cx, cy, r)
                cambio = True
        if cambio:
            im.convert("RGB").save(ruta)
            tocadas += 1
            print("  ", ruta.name)
    print(f"\n{tocadas} placas ahora usan el archivo real del logo")


if __name__ == "__main__":
    main()
