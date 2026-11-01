#!/usr/bin/env python3
"""Sube las dos creatividades por separado, para poder promocionarlas.

Van separadas y no en un carrusel porque la idea es promocionar cada una y
dejar que Meta reparta el presupuesto entre las dos: el test se corre en la
campania paga, no en el organico. Con 37 seguidores el alcance organico de
cada una va a ser de 5 o 6 cuentas, que es ruido y no sirve para decidir.

Mismo horario en dias distintos, para no hacerlas competir entre si en la
misma pasada del feed.

Los dos posteos que habian quedado de la tanda vieja (hc37 y hc18) pasan a
borrador: con el cron apagado estaban vencidos, y si se disparara una corrida
manual el script publicaria el mas viejo primero en vez de la creatividad.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
RUTA = RAIZ / "contenido" / "calendario.json"

CIERRE = ("\n\nHC ARG es una historia clínica digital para psicólogos "
          "argentinos: cifrada en tu computadora —no en la nube—, con agenda, "
          "facturación ARCA y copias de seguridad verificadas.\n\n"
          "Dos pacientes gratis, sin tarjeta y sin vencimiento.\n\n"
          "👉 hcarg.com.ar\n\n"
          "#Psicologos #PsicologiaArgentina #HistoriaClinica "
          "#ConsultorioPsicologico #PsicologosArgentina #SaludMental "
          "#GestionDeConsultorio #HCARG")

P = [
 ("2026-11-01", "12:00", "ad-a-riesgo", "ad_a_riesgo.jpg",
  "Lo que no conviene escribir en una historia clínica.\n\n"
  "Juicios de valor sobre el paciente: «manipulador», «resistente». "
  "Datos de terceros con nombre y apellido. Un diagnóstico tirado al pasar "
  "en la segunda sesión. Tres semanas sin anotar nada.\n\n"
  "Ninguno de los cuatro se nota mientras la historia la leés solo vos. Se "
  "notan el día que la lee alguien más: un colega, un juez, el propio "
  "paciente." + CIERRE),

 ("2026-11-03", "12:00", "ad-b-producto", "ad_b_producto.jpg",
  "Tu historia clínica no tiene por qué vivir en un cuaderno ni en la nube "
  "de otro.\n\n"
  "HC ARG guarda todo cifrado en tu propia computadora. Vos tenés la llave y "
  "nadie más: ni nosotros." + CIERRE),
]

A_BORRADOR = ["hc37-pregunta-abierta", "hc18-exportar-pdf"]


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    existentes = {p["id"] for p in d["posts"]}

    for p in d["posts"]:
        if p["id"] in A_BORRADOR and p["estado"] == "pendiente":
            p["estado"] = "borrador"
            print(f"  ~ {p['id']} -> borrador")

    nuevos = 0
    for fecha, hora, pid, archivo, cap in P:
        if pid in existentes:
            continue
        if not (RAIZ / "contenido" / "publicar" / archivo).exists():
            print(f"  ! falta {archivo}")
            continue
        d["posts"].append(dict(id=pid, tipo="imagen", estado="pendiente",
                               fecha=fecha, hora=hora, archivo=archivo,
                               caption=cap))
        nuevos += 1
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    print(f"\n{nuevos} creatividades programadas")
    for p in d["posts"]:
        if p["estado"] == "pendiente":
            print(f"  {p['fecha']} {p['hora']}  {p['id']}")


if __name__ == "__main__":
    main()
