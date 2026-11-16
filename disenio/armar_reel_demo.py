"""Arma el reel vertical de HC ARG a partir del demo de 3 minutos.

Cuatro tramos elegidos sobre la transcripcion, no a ojo:
  - el cifrado local, que es el diferencial frente a cualquier nube
  - la sesion sellada, que es el argumento legal
  - la facturacion ARCA, que es el dolor concreto del fin de mes
  - el cierre con la prueba gratis

Por que NO se recorta hacia adentro de la app: el demo ya trae subtitulos
quemados que ocupan todo el ancho. Un recorte vertical los parte. Entonces el
video entra entero y se rellena arriba y abajo con una copia desenfocada de
si mismo, que es el formato que ya rindio con la charla del Diplomado.
"""
import subprocess
import textwrap
from pathlib import Path

FUENTE = Path(r"C:/Users/chris/OneDrive/Desktop/HC ARG - demo.mp4")
AQUI = Path(__file__).resolve().parent
W, H = 1080, 1920
GANCHO = "Tus datos no viven en la nube de una empresa"
TIPO_GANCHO = "C:/Windows/Fonts/segoeuib.ttf"
TIPO_PIE = "C:/Windows/Fonts/segoeui.ttf"

TRAMOS = [(0.0, 9.2), (85.4, 97.3), (143.0, 149.4), (166.3, 177.2)]


def esc_ruta(p):
    return p.replace("\\", "/").replace(":", "\\:")


def esc_texto(t):
    for a, b in (("\\", "\\\\"), (":", "\\:"), ("'", "\u2019"), ("%", "\\%"),
                 (",", "\\,")):
        t = t.replace(a, b)
    return t


def cortar():
    partes = []
    for i, (ini, fin) in enumerate(TRAMOS):
        salida = AQUI / f"parte{i}.mp4"
        subprocess.run([
            "ffmpeg", "-y", "-v", "error", "-ss", str(ini), "-t",
            str(round(fin - ini, 2)), "-i", str(FUENTE),
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
            "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-r", "30",
            str(salida)], check=True)
        partes.append(salida)
    lista = AQUI / "partes.txt"
    lista.write_text("".join(f"file '{p.as_posix()}'\n" for p in partes),
                     encoding="utf-8")
    pegado = AQUI / "pegado.mp4"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lista), "-c", "copy", str(pegado)], check=True)
    return pegado


def vertical(entrada, salida):
    alto_video = round(W * 9 / 16 / 2) * 2
    y_video = 700
    filtros = [
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
        f"crop={W}:{H},boxblur=30:2,eq=brightness=-0.20:saturation=0.6[fondo]",
        f"[0:v]scale={W}:{alto_video}[frente]",
        f"[fondo][frente]overlay=0:{y_video}[base]",
    ]
    capa = "base"
    for i, linea in enumerate(textwrap.wrap(GANCHO, width=22)):
        sig = f"g{i}"
        filtros.append(
            f"[{capa}]drawtext=fontfile='{esc_ruta(TIPO_GANCHO)}'"
            f":text='{esc_texto(linea)}':fontcolor=white:fontsize=74"
            f":x=(w-text_w)/2:y={210 + i * 92}"
            f":shadowcolor=black@0.55:shadowx=0:shadowy=4[{sig}]")
        capa = sig
    filtros.append(
        f"[{capa}]drawtext=fontfile='{esc_ruta(TIPO_PIE)}'"
        f":text='{esc_texto('@hcarg.app  ·  datos de demostración')}'"
        f":fontcolor=white@0.80:fontsize=36:x=(w-text_w)/2:y={H - 150}[v]")
    subprocess.run([
        "ffmpeg", "-y", "-v", "error", "-i", str(entrada),
        "-filter_complex", ";".join(filtros), "-map", "[v]", "-map", "0:a",
        "-c:v", "libx264", "-preset", "slow", "-crf", "20",
        "-pix_fmt", "yuv420p", "-profile:v", "high",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100", "-r", "30",
        "-movflags", "+faststart", str(salida)], check=True)
    mb = Path(salida).stat().st_size / 1_048_576
    print(f"  + {Path(salida).name}  {mb:.1f} MB")


if __name__ == "__main__":
    vertical(cortar(), AQUI / "reel_hcarg.mp4")
