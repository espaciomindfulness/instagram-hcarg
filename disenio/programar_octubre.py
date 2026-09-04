#!/usr/bin/env python3
"""Programa la segunda tanda de @hcarg.app: del 18/09 al 16/10, dia por medio."""
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "contenido" / "calendario.json"

HT = ("#Psicologos #PsicologiaArgentina #HistoriaClinica #ConsultorioPsicologico "
      "#PsicologosArgentina #SaludMental #GestionDeConsultorio #HCARG")

P = [
 ("2026-09-18", "09:00", "hc16-trabajo-invisible", "imagen", ["hc16_trabajo_invisible.jpg"],
  "Nadie te paga por administrar tu consultorio.\n\n"
  "Y sin embargo son horas todos los meses: pasar registros, coordinar turnos, "
  "controlar quién pagó, armar facturas. Trabajo real que no entra en ninguna "
  "factura ni en el cálculo de cuánto vale tu hora.\n\n"
  "Pero sí entra en tu cansancio.\n\n"
  "HC ARG junta historia clínica, agenda y facturación en un solo lugar. "
  "Probalo gratis con dos pacientes — link en bio."),

 ("2026-09-20", "20:00", "hc17-derecho-de-acceso", "carrusel",
  [f"hc17_acceso_{i}.jpg" for i in range(1, 7)],
  "Un paciente te pide su historia clínica. ¿Qué hacés?\n\n"
  "Es un derecho suyo, no un favor tuyo: la historia clínica le pertenece. "
  "Vos sos el custodio.\n\n"
  "Cuatro cosas que conviene tener claras antes de que pase 👉 deslizá.\n\n"
  "La segunda es la que complica: los plazos son cortos. Si tus registros están "
  "en un cuaderno o repartidos en carpetas, juntar todo ordenado y legible en "
  "48 horas es un problema real.\n\n"
  "Probalo gratis con dos pacientes — link en bio."),

 ("2026-09-22", "09:00", "hc18-exportar-pdf", "imagen", ["hc18_exportar.jpg"],
  "La historia clínica completa, en un PDF.\n\n"
  "Ordenada, cronológica, con tus datos profesionales. Lista para entregarle al "
  "paciente que la pide o para presentar donde te la reclamen.\n\n"
  "Dos clics. Lo que con papel es una tarde entera de fotocopias y de rezar para "
  "que no falte ninguna hoja.\n\n"
  "hcarg.com.ar"),

 ("2026-09-24", "20:00", "hc19-precio-de-la-hora", "imagen", ["hc19_precio_hora.jpg"],
  "Hacé esta cuenta, aunque duela.\n\n"
  "Agarrá lo que facturaste el mes pasado y dividilo por las horas que le "
  "dedicaste. Todas: las de sesión, las de administración, las de buscar un "
  "dato viejo, las de facturar el domingo a la noche.\n\n"
  "El número que sale casi nunca coincide con lo que creés que cobrás por hora.\n\n"
  "La diferencia no está en tu tarifa: está en las horas que no cobrás.\n\n"
  "Probalo gratis — link en bio."),

 ("2026-09-26", "20:00", "hc20-confidencialidad-practica", "carrusel",
  [f"hc20_privacidad_{i}.jpg" for i in range(1, 8)],
  "La confidencialidad no se rompe por un hacker.\n\n"
  "Se rompe por la notebook en el café, el celular que se pierde, alguien que "
  "abre tu computadora en casa. Lo cotidiano.\n\n"
  "Cinco cosas concretas sobre proteger datos de pacientes, más allá del "
  "juramento 👉 deslizá.\n\n"
  "La segunda sorprende a mucha gente: la contraseña de Windows no protege tus "
  "archivos, solo la sesión. Si alguien saca el disco, lee todo.\n\n"
  "En HC ARG está resuelto por diseño: cifrado local, adjuntos dentro de la "
  "misma base y auditoría de accesos 🔒"),

 ("2026-09-28", "09:00", "hc21-agenda", "imagen", ["hc21_agenda.jpg"],
  "Los turnos, donde ya los mirás.\n\n"
  "La agenda se sincroniza con tu Google Calendar y ya trae los feriados "
  "argentinos cargados, así no agendás una sesión un 25 de mayo.\n\n"
  "Reprogramás en la app y se actualiza en el celular. Sin doble carga.\n\n"
  "Probalo gratis con dos pacientes en hcarg.com.ar"),

 ("2026-09-30", "20:00", "hc22-empezar-de-cero", "imagen", ["hc22_empezar.jpg"],
  "«Tengo diez años de historias en papel.»\n\n"
  "Es la objeción que más escucho, y tiene una respuesta simple: no hace falta "
  "cargar nada retroactivo.\n\n"
  "Empezás con los pacientes que atendés esta semana. El papel queda como "
  "archivo, ahí donde está. En dos meses la mayor parte de tu práctica activa "
  "ya está adentro, sin que hayas hecho ningún trabajo extra.\n\n"
  "No es todo o nada 🌿\n\n"
  "Probalo gratis — link en bio."),

 ("2026-10-02", "20:00", "hc23-dia-tipico", "carrusel",
  [f"hc23_dia_{i}.jpg" for i in range(1, 7)],
  "Cómo es un día con HC ARG, de principio a fin.\n\n"
  "No es «un programa más que abrir». Son cuatro momentos que ya existen en tu "
  "día, resueltos en dos minutos cada uno 👉 deslizá.\n\n"
  "El que más cambia las cosas es el segundo: escribir la sesión al terminar, "
  "con el paciente todavía fresco. No a la noche, cuando ya se te mezclaron "
  "cinco y escribís de memoria.\n\n"
  "Probalo gratis con dos pacientes en hcarg.com.ar"),

 ("2026-10-04", "09:00", "hc24-soporte-directo", "imagen", ["hc24_soporte.jpg"],
  "Si algo no funciona, me escribís a mí.\n\n"
  "No hay mesa de ayuda, ni ticket que se pierde, ni respuesta automática "
  "prometiendo 72 horas hábiles.\n\n"
  "Soy psicólogo y desarrollé HC ARG para mi propio consultorio. Cuando me "
  "contás un problema, entiendo de qué hablás antes de que termines de "
  "explicarlo — porque probablemente lo tuve yo primero.\n\n"
  "Es la ventaja de que esto lo haga un colega y no una empresa de software 🌿"),

 ("2026-10-06", "20:00", "hc25-cierre-prueba", "imagen", ["hc25_cierre.jpg"],
  "Dos pacientes, sin tarjeta, sin vencimiento.\n\n"
  "La versión de prueba tiene todas las funciones: historia clínica cifrada, "
  "agenda, facturación ARCA, reportes y copias de seguridad. No es una demo "
  "recortada.\n\n"
  "Cargá dos pacientes reales y usala un mes entero. Si te ordena la semana, "
  "seguís. Si no, la desinstalás y los datos quedan en tu computadora.\n\n"
  "hcarg.com.ar 🌿"),
]


def main():
    d = json.load(open(RUTA, encoding="utf-8"))
    existentes = {p["id"] for p in d["posts"]}
    nuevos = 0
    for fecha, hora, pid, tipo, arch, cap in P:
        if pid in existentes:
            continue
        post = dict(id=pid, tipo=tipo, estado="pendiente", fecha=fecha, hora=hora,
                    caption=cap + "\n\n" + HT)
        if tipo == "carrusel":
            post["archivos"] = arch
        else:
            post["archivo"] = arch[0]
        d["posts"].append(post)
        nuevos += 1
    d["posts"].sort(key=lambda p: (p["fecha"], p["hora"]))
    open(RUTA, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    pend = [p for p in d["posts"] if p["estado"] == "pendiente"]
    print(f"{nuevos} publicaciones nuevas | {len(pend)} pendientes en total\n")
    for p in pend:
        n = len(p.get("archivos", [])) or 1
        print(f"  {p['fecha']} {p['hora']}  {p['tipo']:<9} {n:^3}  {p['id']}")


if __name__ == "__main__":
    main()
