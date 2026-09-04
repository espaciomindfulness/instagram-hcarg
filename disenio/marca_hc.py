#!/usr/bin/env python3
"""Sistema de diseno de HC ARG para Instagram (@hcarg.app).

Vive dentro del repo a proposito: la version anterior estaba en una carpeta
temporal y se perdio. Todo lo que haga falta para regenerar las placas tiene
que estar aca.

Paleta muestreada de las placas ya publicadas, para que lo nuevo sea
continuacion y no otra marca:
    teal   #36A8A0     rosa  #E78FA6     blanco menta  #EAF6F4
    teal oscuro #1D6A66  (botones y titulares fuertes)

Los tres fondos se alternan post a post: en la grilla del perfil Instagram
solo muestra la primera placa de cada publicacion, asi que alternar es lo
que evita el bloque monocromo.

El logo NO se dibuja por codigo: se usa el archivo real
(contenido/marca/isotipo_hcarg.png), que es el mismo de la foto de perfil.
Dibujarlo daba proporciones inventadas y se notaba.

Formato 1080x1350 (4:5), sin escalados intermedios.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
MARGEN = 96

TEAL = (54, 168, 160)          # #36A8A0
TEAL_OSCURO = (29, 106, 102)   # #1D6A66
TEAL_PALIDO = (168, 224, 219)
ROSA = (231, 143, 166)         # #E78FA6
ROSA_PALIDO = (250, 219, 227)
BLANCO = (234, 246, 244)       # #EAF6F4  blanco menta
BLANCO_PURO = (255, 255, 255)
TINTA = (28, 46, 45)           # titulares sobre fondo claro
GRIS = (92, 112, 111)          # cuerpo sobre fondo claro
GRIS_CLARO = (150, 170, 168)
LINEA_CLARA = (206, 228, 224)

F = "C:/Windows/Fonts/"
SANS, SANS_B = "calibri.ttf", "calibrib.ttf"
SERIF_B, SERIF_I = "georgiab.ttf", "georgiai.ttf"

RAIZ = Path(__file__).resolve().parent.parent
DESTINO = RAIZ / "contenido" / "originales"
CAPTURAS = RAIZ.parent / "capturas"
LOGO = Image.open(RAIZ / "contenido" / "marca" / "isotipo_hcarg.png").convert("RGBA")

# Cada fondo con sus colores de texto. `chapa` = disco blanco detras del logo,
# necesario sobre teal y rosa porque si no los petalos teal desaparecen.
TONOS = {
    "teal":   dict(fondo=TEAL,   titulo=BLANCO_PURO, sub=TEAL_PALIDO, cuerpo=(233, 246, 244),
                   linea=TEAL_PALIDO, acento=BLANCO_PURO, chapa=True,  pie=TEAL_PALIDO),
    "rosa":   dict(fondo=ROSA,   titulo=BLANCO_PURO, sub=ROSA_PALIDO, cuerpo=(253, 240, 244),
                   linea=ROSA_PALIDO, acento=BLANCO_PURO, chapa=True,  pie=ROSA_PALIDO),
    "blanco": dict(fondo=BLANCO, titulo=TINTA,       sub=TEAL,        cuerpo=GRIS,
                   linea=LINEA_CLARA, acento=TEAL,     chapa=False, pie=GRIS_CLARO),
}


def fuente(nombre, tam):
    return ImageFont.truetype(F + nombre, tam)


# --- texto ----------------------------------------------------------------

def ancho(d, texto, fnt):
    return d.textbbox((0, 0), texto, font=fnt)[2]


def envolver(d, texto, fnt, max_ancho):
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        prueba = f"{actual} {p}".strip()
        if ancho(d, prueba, fnt) <= max_ancho:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def alto_parrafo(d, texto, fnt, max_ancho, interlinea=1.42):
    return int(len(envolver(d, texto, fnt, max_ancho)) * fnt.size * interlinea)


def parrafo(d, texto, fnt, x, y, max_ancho, color, interlinea=1.42, centrado=False):
    lineas = envolver(d, texto, fnt, max_ancho)
    salto = int(fnt.size * interlinea)
    for i, linea in enumerate(lineas):
        px = x + (max_ancho - ancho(d, linea, fnt)) // 2 if centrado else x
        d.text((px, y + i * salto), linea, font=fnt, fill=color)
    return y + len(lineas) * salto


def espaciado(d, texto, fnt, x, y, color, sep=6, centrado_en=None):
    """Letter-spacing manual: Pillow no lo trae."""
    total = sum(ancho(d, c, fnt) + sep for c in texto) - sep
    px = x if centrado_en is None else (centrado_en - total) // 2
    for c in texto:
        d.text((px, y), c, font=fnt, fill=color)
        px += ancho(d, c, fnt) + sep
    return total


# --- elementos ------------------------------------------------------------

def isotipo(img, cx, cy, radio, chapa=False):
    """Pega el archivo real del logo. `chapa` agrega el disco blanco detras."""
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    if chapa:
        r_disco = radio * 1.52
        ImageDraw.Draw(capa).ellipse(
            [cx - r_disco, cy - r_disco, cx + r_disco, cy + r_disco],
            fill=(255, 255, 255, 255))
    img.alpha_composite(capa)
    lado = int(radio * 2)
    img.alpha_composite(LOGO.resize((lado, lado), Image.LANCZOS),
                        (cx - lado // 2, cy - lado // 2))


def circulos(img, color, especificaciones):
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for cx, cy, r, alfa in especificaciones:
        dc.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alfa,))
    img.alpha_composite(capa)


def caja_translucida(img, caja, color=BLANCO_PURO, alfa=30, radio=18):
    """ImageDraw sobre RGBA pisa el alfa en vez de mezclarlo: hay que componer."""
    capa = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(capa).rounded_rectangle(caja, radius=radio, fill=color + (alfa,))
    img.alpha_composite(capa)


def flecha(d, x, y, color, escala=1.0):
    s = 18 * escala
    d.polygon([(x, y - s / 2), (x + s * 0.85, y), (x, y + s / 2)], fill=color)


def pie(d, color=GRIS_CLARO):
    espaciado(d, "@hcarg.app", fuente(SANS, 30), 0, H - 78, color, sep=3, centrado_en=W)


def lienzo(fondo):
    return Image.new("RGBA", (W, H), fondo)


def captura(nombre, ancho_px, alto_px, foco_y=0.0, region=None):
    """Recorta una captura de la app. `region` (x0,y0,x1,y1 relativos) marca la
    zona util: son capturas de pantalla completa y sin eso entra fondo vacio."""
    im = Image.open(CAPTURAS / nombre).convert("RGB")
    if region:
        x0, y0, x1, y1 = region
        im = im.crop((int(x0 * im.width), int(y0 * im.height),
                      int(x1 * im.width), int(y1 * im.height)))
    escala = max(ancho_px / im.width, alto_px / im.height)
    im = im.resize((max(1, round(im.width * escala)), max(1, round(im.height * escala))),
                   Image.LANCZOS)
    x = int((im.width - ancho_px) * 0.5)
    y = int((im.height - alto_px) * foco_y)
    return im.crop((x, y, x + ancho_px, y + alto_px))


# --- piezas ---------------------------------------------------------------

def portada(titulo, subtitulo, bajada, tono="teal"):
    t = TONOS[tono]
    img = lienzo(t["fondo"])
    circulos(img, BLANCO_PURO if tono != "blanco" else TEAL,
             [(950, 190, 230, 16 if tono != "blanco" else 12), (110, 1180, 260, 12)])
    isotipo(img, W // 2, 190, 62, t["chapa"])
    d = ImageDraw.Draw(img)

    util = W - 2 * MARGEN
    f = fuente(SERIF_B, 88 if len(titulo) < 30 else 74)
    y = parrafo(d, titulo, f, MARGEN, 390, util, t["titulo"], interlinea=1.18, centrado=True)
    y = parrafo(d, subtitulo, fuente(SERIF_I, 76), MARGEN, y + 12, util, t["sub"],
                interlinea=1.18, centrado=True)
    d.line([(W // 2 - 90, y + 74), (W // 2 + 90, y + 74)], fill=t["linea"], width=3)
    parrafo(d, bajada, fuente(SANS, 42), MARGEN + 40, y + 140, util - 80, t["cuerpo"],
            interlinea=1.45, centrado=True)

    total = espaciado(d, "DESLIZÁ", fuente(SANS_B, 34), 0, H - 250, t["acento"], sep=6,
                      centrado_en=W - 46)
    flecha(d, (W + total) // 2 - 6, H - 235, t["acento"])
    pie(d, t["pie"])
    return img.convert("RGB")


def punto(etiqueta, titulo, cuerpo, numero=None):
    """Placa interior de carrusel. No lleva logo: el logo va en portada y cierre."""
    img = lienzo(BLANCO)
    circulos(img, TEAL, [(1000, 1230, 190, 12), (70, 140, 160, 9)])
    d = ImageDraw.Draw(img)

    if numero is not None:
        d.text((MARGEN - 12, 150), str(numero), font=fuente(SERIF_B, 250), fill=TEAL)
        arranque = 460
    else:
        espaciado(d, etiqueta, fuente(SANS_B, 32), MARGEN, 150, TEAL, sep=8)
        d.line([(MARGEN, 214), (MARGEN + 78, 214)], fill=ROSA, width=4)
        arranque = 290

    util = W - 2 * MARGEN - 16
    f_t, f_c = fuente(SERIF_B, 62), fuente(SANS, 45)
    alto = alto_parrafo(d, titulo, f_t, util, 1.24) + 56 + alto_parrafo(d, cuerpo, f_c, util, 1.48)
    y = arranque + max(0, (H - 210 - arranque - alto) // 2)
    y = parrafo(d, titulo, f_t, MARGEN, y, util, TINTA, interlinea=1.24)
    parrafo(d, cuerpo, f_c, MARGEN, y + 56, util, GRIS, interlinea=1.48)
    pie(d)
    return img.convert("RGB")


def placa_captura(etiqueta, titulo, cuerpo, archivo, region=None, foco_y=0.0):
    """Post de producto: captura real de la app arriba, texto abajo."""
    ALTO = 620
    img = lienzo(BLANCO)
    img.paste(captura(archivo, W, ALTO, foco_y, region).convert("RGBA"), (0, 0))
    caja_translucida(img, [0, 0, W, 132], color=TEAL, alfa=235, radio=0)
    isotipo(img, 92, 66, 40, chapa=True)
    d = ImageDraw.Draw(img)
    espaciado(d, etiqueta, fuente(SANS_B, 30), 178, 52, BLANCO_PURO, sep=7)

    leyenda = "CAPTURA REAL · DATOS DE DEMOSTRACIÓN"
    f_ley = fuente(SANS, 22)
    an = sum(ancho(d, c, f_ley) + 2 for c in leyenda) - 2
    caja_translucida(img, [MARGEN - 20, ALTO - 54, MARGEN + an + 20, ALTO - 12],
                     color=TINTA, alfa=205, radio=21)
    d = ImageDraw.Draw(img)
    espaciado(d, leyenda, f_ley, MARGEN, ALTO - 46, BLANCO_PURO, sep=2)

    util = W - 2 * MARGEN - 16
    y = parrafo(d, titulo, fuente(SERIF_B, 62), MARGEN, ALTO + 90, util, TINTA, interlinea=1.24)
    parrafo(d, cuerpo, fuente(SANS, 44), MARGEN, y + 46, util, GRIS, interlinea=1.48)
    pie(d)
    return img.convert("RGB")


def cta(titulo, cuerpo, boton, remate=None, tono="rosa"):
    t = TONOS[tono]
    img = lienzo(t["fondo"])
    circulos(img, BLANCO_PURO if tono != "blanco" else TEAL,
             [(140, 240, 250, 14), (960, 1150, 230, 16)])
    isotipo(img, W // 2, 186, 58, t["chapa"])
    d = ImageDraw.Draw(img)

    util = W - 2 * MARGEN
    y = parrafo(d, titulo, fuente(SERIF_B, 76), MARGEN, 390, util, t["titulo"],
                interlinea=1.22, centrado=True)
    d.line([(W // 2 - 70, y + 54), (W // 2 + 70, y + 54)], fill=t["linea"], width=3)
    y = parrafo(d, cuerpo, fuente(SANS, 44), MARGEN + 20, y + 124, util - 40, t["cuerpo"],
                interlinea=1.50, centrado=True)

    caja_y = y + 90
    d.rounded_rectangle([MARGEN + 60, caja_y, W - MARGEN - 60, caja_y + 126], radius=18,
                        fill=TEAL_OSCURO if tono != "blanco" else TEAL)
    espaciado(d, boton, fuente(SANS_B, 34 if len(boton) < 26 else 30), 0, caja_y + 44,
              BLANCO_PURO, sep=4, centrado_en=W)
    if remate:
        espaciado(d, remate, fuente(SANS, 27), 0, caja_y + 172, t["pie"], sep=3, centrado_en=W)
    pie(d, t["pie"])
    return img.convert("RGB")


def texto_suelto(etiqueta, titulo, cuerpo, remate=None, tono="blanco"):
    """Placa de un solo golpe: etiqueta, titular grande y bajada."""
    t = TONOS[tono]
    img = lienzo(t["fondo"])
    circulos(img, BLANCO_PURO if tono != "blanco" else TEAL,
             [(980, 240, 240, 14 if tono != "blanco" else 11), (90, 1180, 250, 12)])
    isotipo(img, W // 2, 180, 56, t["chapa"])
    d = ImageDraw.Draw(img)

    util = W - 2 * MARGEN - 16
    espaciado(d, etiqueta, fuente(SANS_B, 30), 0, 306,
              t["sub"] if tono == "blanco" else t["linea"], sep=7, centrado_en=W)
    f_t = fuente(SERIF_B, 76 if len(titulo) < 44 else 64)
    y = parrafo(d, titulo, f_t, MARGEN, 378, util, t["titulo"], interlinea=1.22, centrado=True)
    d.line([(W // 2 - 70, y + 54), (W // 2 + 70, y + 54)], fill=t["linea"], width=3)
    y = parrafo(d, cuerpo, fuente(SANS, 44), MARGEN + 10, y + 124, util - 20, t["cuerpo"],
                interlinea=1.50, centrado=True)
    if remate:
        espaciado(d, remate, fuente(SANS_B, 28), 0, y + 70,
                  t["sub"] if tono == "blanco" else t["linea"], sep=5, centrado_en=W)
    pie(d, t["pie"])
    return img.convert("RGB")


def guardar(placas, nombre_preview=None, cols=6):
    DESTINO.mkdir(parents=True, exist_ok=True)
    for nombre, img in placas:
        img.save(DESTINO / nombre)
        print("  +", nombre, img.size)
    if not nombre_preview:
        return
    tw, th = 260, 325
    filas = (len(placas) + cols - 1) // cols
    hoja = Image.new("RGB", (cols * tw, filas * th), "white")
    for i, (_, img) in enumerate(placas):
        mini = img.copy()
        mini.thumbnail((tw - 8, th - 8))
        hoja.paste(mini, ((i % cols) * tw + 4, (i // cols) * th + 4))
    hoja.save(nombre_preview, quality=90)
    print("preview:", nombre_preview)
