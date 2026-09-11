#!/usr/bin/env python3
"""Programa la tercera tanda de @hcarg.app: del 08/10 al 30/10, dia por medio.

Con esto las dos cuentas quedan cubiertas hasta fin de octubre.

Los textos siguen el molde nuevo: el gancho es el problema, no el producto.
La app aparece recien al final y en una linea. Si el primer renglon habla del
software, nadie lo guarda.
"""
import json
from pathlib import Path

RUTA = Path(__file__).resolve().parent.parent / "contenido" / "calendario.json"

HT = ("#Psicologos #PsicologiaArgentina #HistoriaClinica #ConsultorioPsicologico "
      "#PsicologosArgentina #SaludMental #GestionDeConsultorio #HCARG")

# Aviso fijo para las piezas que tocan temas legales. No se negocia: son
# psicologos leyendo sobre sus propias obligaciones y no somos su abogado.
LEGAL = ("Esto es orientación general, no asesoramiento legal. Ante un caso "
         "concreto, consultá con tu colegio profesional o con un abogado.")

P = [
 ("2026-10-08", "09:00", "hc26-que-no-escribir", "carrusel",
  [f"hc26_escribir_{i}.jpg" for i in range(1, 7)],
  "Cuatro cosas que conviene NO escribir en una historia clínica.\n\n"
  "No porque estén prohibidas, sino porque el día que alguien más la lee —un "
  "colega, un juez, el propio paciente— se vuelven en contra 👉 deslizá.\n\n"
  "La primera es la más común: «manipulador», «resistente», «poco "
  "colaborativo». Son conclusiones tuyas escritas como si fueran hechos. "
  "Describí la conducta que observaste y dejá que el criterio clínico se "
  "sostenga solo.\n\n"
  "Y la cuarta es la que más caro sale: no escribir nada durante tres "
  "semanas. Sin registro no podés fundamentar por qué hiciste lo que hiciste.\n\n"
  + LEGAL),

 ("2026-10-10", "20:00", "hc27-cuanto-guardar", "imagen", ["hc27_guardar.jpg"],
  "¿Cuánto tiempo hay que guardar una historia clínica?\n\n"
  "La ley 26.529 habla de diez años desde la última actuación.\n\n"
  "Diez años. Pensalo en papel: mudanzas, cajas, humedad, el altillo de la "
  "casa de tus viejos. Y la obligación sigue siendo tuya aunque el paciente "
  "no vuelva nunca más.\n\n"
  "En digital y cifrado ocupa lo que ocupa un archivo, se copia solo y se "
  "encuentra en dos segundos el día que alguien la pide.\n\n"
  + LEGAL),

 ("2026-10-12", "09:00", "hc28-oficio-judicial", "carrusel",
  [f"hc28_oficio_{i}.jpg" for i in range(1, 7)],
  "Te llega un oficio pidiendo la historia clínica de un paciente.\n\n"
  "Pasa más de lo que uno cree, casi siempre en un divorcio o una causa "
  "laboral, y casi siempre agarra desprevenido 👉 deslizá.\n\n"
  "Lo primero: en la enorme mayoría de los casos sos un tercero al que le "
  "piden documentación, no alguien investigado. El apuro y el susto son los "
  "que hacen que se cometan errores.\n\n"
  "Lo segundo, y es donde más se resbala: no es lo mismo que te pidan «la "
  "historia clínica completa» que «constancia de tratamiento» o «fechas de "
  "atención». Se entrega lo que se pidió. El secreto profesional sigue en "
  "pie sobre todo lo demás.\n\n"
  + LEGAL),

 ("2026-10-14", "20:00", "hc29-ausencias", "imagen", ["hc29_ausencias.jpg"],
  "«Perdón, hoy no voy a poder» — media hora antes.\n\n"
  "Ese turno no se recupera. Y la conversación sobre qué pasa cuando eso "
  "ocurre es de las que más se posterga, porque incomoda.\n\n"
  "Pero postergarla la vuelve peor: cuando la tenés que tener ya pasó algo, "
  "y entonces parece un reclamo personal en vez de un encuadre.\n\n"
  "Conviene que esté escrita y conversada en la primera sesión, junto con el "
  "resto del encuadre. No es una cuestión de plata: es parte del setting.\n\n"
  "¿Vos cómo lo manejás? Me interesa leerlo 👇"),

 ("2026-10-16", "09:00", "hc30-como-anotar", "carrusel",
  [f"hc30_anotar_{i}.jpg" for i in range(1, 7)],
  "Un formato para anotar la sesión en dos minutos.\n\n"
  "Si te quedás mirando la pantalla sin saber por dónde empezar, el problema "
  "no es tu memoria: es que no tenés un molde 👉 deslizá.\n\n"
  "Cuatro campos: qué trajo, qué observaste, qué hiciste, por dónde seguir.\n\n"
  "El tercero es el que casi nadie escribe y el único que después explica por "
  "qué el tratamiento fue por donde fue. Y el cuarto es un regalo para vos "
  "del futuro: te evita empezar preguntando «¿en qué habíamos quedado?».\n\n"
  "Guardátelo para tenerlo a mano esta semana 🌿"),

 ("2026-10-18", "20:00", "hc31-backup", "imagen", ["hc31_backup.jpg"],
  "Si mañana se te rompe la notebook, ¿qué perdés?\n\n"
  "No es una hipótesis rara. Un disco que muere, un café volcado, un robo en "
  "el consultorio. Le pasa a alguien todos los días.\n\n"
  "Si la respuesta es «todo» o «no sé», eso es lo primero que hay que "
  "resolver — antes que cambiar de sistema, antes que ordenar la agenda, "
  "antes que cualquier otra mejora.\n\n"
  "Y una segunda pregunta, más incómoda: si tenés copia de seguridad, "
  "¿alguna vez la restauraste? Una copia que nunca se probó es una copia que "
  "no sabés si sirve.\n\n"
  "En HC ARG las copias son automáticas y verificadas. hcarg.com.ar"),

 ("2026-10-20", "09:00", "hc32-consentimiento", "carrusel",
  [f"hc32_consent_{i}.jpg" for i in range(1, 7)],
  "Qué tendría que decir un consentimiento informado, más allá de la firma.\n\n"
  "Cuatro puntos 👉 deslizá.\n\n"
  "El segundo es el que más se omite y el más importante: los límites del "
  "secreto profesional. Decir de entrada en qué situaciones podrías tener "
  "que informar evita tener que explicarlo justo en el peor momento posible.\n\n"
  "Y el tercero cada vez lo preguntan más: dónde quedan sus datos y quién "
  "puede acceder. Tener la respuesta lista transmite seriedad antes de que "
  "empiece el tratamiento.\n\n"
  + LEGAL),

 ("2026-10-22", "20:00", "hc33-facturar", "imagen", ["hc33_facturar.jpg"],
  "El fin de mes, en una tarde menos.\n\n"
  "La app arma las Factura C, se conecta con ARCA y trae el CAE. Sin volver "
  "a cargar lo que ya anotaste sesión por sesión: si marcaste el cobro "
  "cuando pasó, la facturación ya está hecha.\n\n"
  "Lo que antes era un domingo entero con el navegador abierto en tres "
  "pestañas.\n\n"
  "Probalo gratis con dos pacientes — link en bio."),

 ("2026-10-24", "09:00", "hc34-teleconsulta", "carrusel",
  [f"hc34_tele_{i}.jpg" for i in range(1, 6)],
  "Atender por videollamada no es atender en el consultorio con otra "
  "pantalla.\n\n"
  "Tres cosas que cambian, y una que no 👉 deslizá.\n\n"
  "La primera: el encuadre que antes daba el espacio ahora hay que "
  "construirlo con palabras. Dónde está cada uno, qué pasa si se corta, "
  "quién más hay en la casa. Si no se acuerda, se improvisa — y se improvisa "
  "mal.\n\n"
  "Y la que no cambia: el registro. Una sesión por videollamada es una "
  "sesión, y va a la historia clínica con la misma responsabilidad.\n\n"
  + LEGAL),

 ("2026-10-26", "20:00", "hc35-primer-contacto", "imagen", ["hc35_contacto.jpg"],
  "Ese mensaje de WhatsApp que llega un domingo a la noche.\n\n"
  "Tres preguntas antes de agendar:\n\n"
  "· ¿Qué te trae?\n"
  "· ¿Estás en tratamiento con alguien más?\n"
  "· ¿Hay algo urgente?\n\n"
  "Dos minutos ahí te ahorran una primera sesión entera de reacomodar "
  "expectativas — o te evitan tomar un caso que no era para vos.\n\n"
  "La tercera además es de cuidado, no de filtro: si hay urgencia, esa "
  "persona necesita otra cosa antes que un turno para dentro de diez días 🌿"),

 ("2026-10-28", "09:00", "hc36-cerrar-anio", "carrusel",
  [f"hc36_cierre_{i}.jpg" for i in range(1, 8)],
  "Cinco cosas para revisar en tu consultorio ahora, no en diciembre.\n\n"
  "En diciembre ya no hay tiempo: hay cierres, fiestas y ganas de que "
  "termine 👉 deslizá.\n\n"
  "La segunda duele: agarrá lo que facturaste este año y dividilo por las "
  "horas que le dedicaste. Todas — sesión, administración, facturar el "
  "domingo. Ese número, y no tu tarifa, es lo que tendría que ordenar tus "
  "decisiones del año que viene.\n\n"
  "Y la quinta es la que más se posterga: el mejor momento para cambiar de "
  "sistema es enero, con la agenda vacía. En marzo ya estás corriendo y todo "
  "queda para el año que viene otra vez.\n\n"
  "Guardátelo y volvé en noviembre 🌿"),

 ("2026-10-30", "20:00", "hc37-pregunta-abierta", "imagen", ["hc37_pregunta.jpg"],
  "Una pregunta, y me interesa de verdad la respuesta:\n\n"
  "¿Qué es lo que más te cuesta de la parte administrativa del consultorio?\n\n"
  "Facturar a fin de mes. Escribir las sesiones. Coordinar turnos por "
  "WhatsApp. Perseguir cobros. Encontrar ese dato de hace dos años que "
  "sabés que anotaste en algún lado.\n\n"
  "Leo todas las respuestas. Varias de las funciones que tiene hoy HC ARG "
  "salieron de charlas así con colegas, y las próximas van a salir de "
  "acá 👇"),
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
    open(RUTA, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=2) + "\n")

    pend = [p for p in d["posts"] if p["estado"] == "pendiente"]
    largo = max(len(p["caption"]) for p in d["posts"])
    print(f"{nuevos} nuevas | {len(pend)} pendientes | caption mas larga: {largo} de 2200\n")
    for p in pend:
        n = len(p.get("archivos", [])) or 1
        print(f"  {p['fecha']} {p['hora']}  {p['tipo']:<9} {n:^3}  {p['id']}")


if __name__ == "__main__":
    main()
