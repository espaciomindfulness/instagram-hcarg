#!/usr/bin/env python3
"""Tercera tanda de @hcarg.app: 12 publicaciones del 08/10 al 30/10.

Cambia el molde a proposito. Las dos tandas anteriores hablaban del software;
esta habla del PROBLEMA que el psicologo tiene esta semana, y el software
aparece al final como una forma de resolverlo, no como el tema.

El motivo es medido, no una corazonada: en @espaciomindfulness las unicas dos
publicaciones que se guardaron (12 y 10 veces) duplicaron el alcance de todas
las demas. Guardar es la senal que hace que Instagram te muestre a gente que
no te sigue. Y lo que se guarda es lo que uno quiere volver a leer: un
checklist, un plazo, un "que hago si me pasa esto". No un anuncio.

De ahi que la tanda sea mayoria carrusel (6 de 12) y que casi todos los temas
sean cosas que dan miedo o pereza: un oficio judicial, que anotar en la
sesion, cuanto hay que guardar, como cerrar el anio.

⚠️ PLAZOS LEGALES: los numeros de la ley 26.529 (10 anios de conservacion,
48 horas para entregar) van escritos como "la ley habla de", nunca como
asesoramiento. Cada pieza legal aclara que el responsable es el profesional.
Antes de publicar conviene que Christian los confirme.

Sin precios: la version de prueba es la unica oferta que se nombra.
"""
from marca_hc import *


# ── 08/10 · lo que no va en la historia clinica ───────────────────────────
def p26_que_no_escribir():
    return [
        ("hc26_escribir_1.png", portada(
            "Qué NO conviene", "escribir en una historia clínica",
            "Cuatro cosas que después se vuelven en contra.", "teal")),
        ("hc26_escribir_2.png", punto(
            None, "Juicios de valor sobre el paciente.",
            "«Manipulador», «poco colaborativo», «resistente». Describí la "
            "conducta que observaste, no la etiqueta que te generó. La "
            "diferencia importa el día que alguien más lo lee.", 1)),
        ("hc26_escribir_3.png", punto(
            None, "Datos de terceros con nombre y apellido.",
            "Lo que el paciente cuenta de su pareja, su jefe o su madre es "
            "material clínico, pero esas personas no consintieron nada. "
            "Alcanza con el vínculo: «la pareja», «un familiar».", 2)),
        ("hc26_escribir_4.png", punto(
            None, "Diagnósticos tirados al pasar.",
            "Un rótulo escrito de apuro en la segunda sesión queda ahí para "
            "siempre. Si todavía es una hipótesis, escribila como hipótesis.", 3)),
        ("hc26_escribir_5.png", punto(
            None, "Nada, durante tres semanas.",
            "El registro tardío es el problema más común y el más caro: sin "
            "notas no podés fundamentar tus decisiones clínicas si alguna vez "
            "te las preguntan.", 4)),
        ("hc26_escribir_6.png", cta(
            "Escribir en el momento",
            "Cuando la historia clínica está a un clic, anotar al terminar la "
            "sesión deja de ser una tarea pendiente para el domingo.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "teal")),
    ]


# ── 10/10 · cuanto hay que guardarla ──────────────────────────────────────
def p27_cuanto_guardar():
    return texto_suelto(
        "UNA PREGUNTA QUE APARECE TARDE",
        "¿Cuánto tiempo hay que guardar una historia clínica?",
        "La ley 26.529 habla de diez años desde la última actuación. Diez "
        "años de papel, de mudanzas, de cajas que se mojan. O un archivo "
        "cifrado con copia automática.",
        "CONSULTÁ SIEMPRE CON TU COLEGIO", "rosa")


# ── 12/10 · el oficio judicial ────────────────────────────────────────────
def p28_oficio():
    return [
        ("hc28_oficio_1.png", portada(
            "Te llega un oficio", "pidiendo una historia clínica",
            "Qué se entrega, qué no, y en cuánto tiempo.", "blanco")),
        ("hc28_oficio_2.png", punto(
            None, "Respirá: no es una acusación.",
            "En la enorme mayoría de los casos sos un tercero al que le piden "
            "documentación, no alguien investigado. El apuro es lo que hace "
            "que se cometan errores.", 1)),
        ("hc28_oficio_3.png", punto(
            None, "Leé qué te están pidiendo exactamente.",
            "No es lo mismo «la historia clínica completa» que «constancia de "
            "tratamiento» o «fechas de atención». Se entrega lo pedido, no "
            "todo lo que tenés.", 2)),
        ("hc28_oficio_4.png", punto(
            None, "El secreto profesional no desaparece.",
            "Sigue en pie sobre lo que no fue requerido. Si algo del pedido "
            "te genera dudas, se puede plantear la reserva por escrito en vez "
            "de resolverlo solo.", 3)),
        ("hc28_oficio_5.png", punto(
            None, "Y quedate con constancia de todo.",
            "Qué entregaste, cuándo y a quién. Esa constancia te protege a "
            "vos, y es lo primero que falta cuando el registro está en papel.", 4)),
        ("hc28_oficio_6.png", cta(
            "Ordenada y en dos clics",
            "Exportás la historia completa en PDF, cronológica y con tus "
            "datos profesionales. Ante un plazo corto, eso es todo.",
            "PROBALO GRATIS · LINK EN BIO", None, "blanco")),
    ]


# ── 14/10 · el paciente que falta ─────────────────────────────────────────
def p29_ausencias():
    return texto_suelto(
        "LA CONVERSACIÓN INCÓMODA",
        "El paciente que falta y avisa media hora antes.",
        "Ese turno no se recupera. La política de cancelación no es una "
        "cuestión de plata: es un encuadre, y conviene que esté escrita y "
        "conversada en la primera sesión, no improvisada cuando ya pasó.",
        None, "teal")


# ── 16/10 · como anotar la sesion ─────────────────────────────────────────
def p30_como_anotar():
    return [
        ("hc30_anotar_1.png", portada(
            "Anotar la sesión", "en dos minutos",
            "Un formato para no quedarte mirando la pantalla.", "rosa")),
        ("hc30_anotar_2.png", punto(
            "QUÉ TRAJO", "Con qué llegó, en sus palabras.",
            "Una o dos líneas. Sirve más una frase textual del paciente que "
            "un resumen tuyo: cuando la releas te devuelve el clima de la "
            "sesión entera.")),
        ("hc30_anotar_3.png", punto(
            "QUÉ OBSERVASTE", "Lo que viste, no lo que interpretaste.",
            "Llegó tarde, lloró, evitó un tema, cambió el tono. Los datos "
            "observables son los que después sostienen tu criterio clínico.")),
        ("hc30_anotar_4.png", punto(
            "QUÉ HICISTE", "La intervención, dicha simple.",
            "Qué trabajaste y con qué. Es la parte que casi nadie anota y la "
            "única que explica por qué el tratamiento fue por donde fue.")),
        ("hc30_anotar_5.png", punto(
            "POR DÓNDE SEGUIR", "Una línea para vos, del futuro.",
            "Qué retomar la próxima. Es lo que te evita empezar la sesión "
            "siguiente preguntando «¿en qué habíamos quedado?».")),
        ("hc30_anotar_6.png", cta(
            "Cuatro campos, dos minutos",
            "Con el paciente todavía fresco, al terminar. No a la noche, "
            "cuando ya se te mezclaron cinco y escribís de memoria.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "rosa")),
    ]


# ── 18/10 · se rompe la notebook ──────────────────────────────────────────
def p31_backup():
    return texto_suelto(
        "LA PREGUNTA DE LAS TRES DE LA MAÑANA",
        "Si mañana se te rompe la notebook, ¿qué perdés?",
        "No es una hipótesis rara: pasa. Si la respuesta es «todo» o «no sé», "
        "eso es lo primero que hay que resolver, antes que cualquier otra "
        "mejora en tu consultorio.",
        "COPIAS AUTOMÁTICAS Y VERIFICADAS", "blanco")


# ── 20/10 · consentimiento informado ──────────────────────────────────────
def p32_consentimiento():
    return [
        ("hc32_consent_1.png", portada(
            "Consentimiento", "informado",
            "Qué tendría que decir, más allá de la firma.", "teal")),
        ("hc32_consent_2.png", punto(
            None, "En qué consiste el tratamiento.",
            "Enfoque, frecuencia y duración estimada. No hace falta un "
            "tratado: hace falta que la persona entienda a qué está "
            "diciendo que sí.", 1)),
        ("hc32_consent_3.png", punto(
            None, "Los límites del secreto profesional.",
            "Es la parte que más se omite y la más importante. Decir de "
            "entrada en qué situaciones podrías tener que informar evita el "
            "peor momento posible para explicarlo.", 2)),
        ("hc32_consent_4.png", punto(
            None, "Cómo se manejan sus datos.",
            "Dónde queda registrada la información, quién puede acceder y "
            "cómo se protege. Cada vez más pacientes lo preguntan, y tener "
            "la respuesta lista transmite seriedad.", 3)),
        ("hc32_consent_5.png", punto(
            None, "Que puede revocarlo cuando quiera.",
            "Consentir no es firmar una permanencia. Decirlo explícitamente "
            "cambia la relación: el paciente se queda porque elige, no "
            "porque firmó.", 4)),
        ("hc32_consent_6.png", cta(
            "Y que quede guardado",
            "Adjuntalo a la historia clínica del paciente, dentro de la "
            "misma base cifrada. Firmado, fechado y siempre a mano.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "teal")),
    ]


# ── 22/10 · facturacion ───────────────────────────────────────────────────
def p33_facturar():
    return placa_captura(
        "FACTURACIÓN",
        "El fin de mes, en una tarde menos.",
        "La app arma las Factura C, se conecta con ARCA y trae el CAE. Sin "
        "cargar dos veces lo que ya anotaste sesión por sesión.",
        "FACTURAR.png", (0.00, 0.10, 0.52, 0.62))


# ── 24/10 · teleconsulta ──────────────────────────────────────────────────
def p34_teleconsulta():
    return [
        ("hc34_tele_1.png", portada(
            "Atender por videollamada", "no es lo mismo",
            "Tres cosas que cambian, y una que no.", "rosa")),
        ("hc34_tele_2.png", punto(
            None, "El encuadre hay que construirlo.",
            "El consultorio lo daba solo: un espacio, una puerta, un horario. "
            "En pantalla eso se acuerda: dónde está cada uno, qué pasa si se "
            "corta, quién más hay en la casa.", 1)),
        ("hc34_tele_3.png", punto(
            None, "La privacidad ya no depende solo de vos.",
            "Podés cuidar tu lado, pero no el del paciente. Conviene "
            "conversarlo de entrada, no asumirlo.", 2)),
        ("hc34_tele_4.png", punto(
            None, "El registro es igual de obligatorio.",
            "Una sesión por videollamada es una sesión. Va a la historia "
            "clínica con la misma responsabilidad que la presencial.", 3)),
        ("hc34_tele_5.png", cta(
            "Lo que no cambia",
            "Tu obligación de registrar, guardar y poder entregar. Da igual "
            "el canal: la historia clínica es una sola.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "rosa")),
    ]


# ── 26/10 · el primer contacto ────────────────────────────────────────────
def p35_primer_contacto():
    return texto_suelto(
        "ANTES DE DAR EL TURNO",
        "Ese mensaje de WhatsApp que llega un domingo.",
        "Tres preguntas antes de agendar: qué la trae, si está en tratamiento "
        "con alguien más, y si hay algo urgente. Dos minutos ahí te ahorran "
        "una primera sesión entera de reacomodar expectativas.",
        None, "blanco")


# ── 28/10 · cerrar el anio ────────────────────────────────────────────────
def p36_cerrar_anio():
    return [
        ("hc36_cierre_1.png", portada(
            "Cerrar el año", "en tu consultorio",
            "Cinco cosas para revisar ahora, no en diciembre.", "teal")),
        ("hc36_cierre_2.png", punto(
            None, "Las historias que quedaron a medio escribir.",
            "Las sesiones sin registrar de marzo no se van a escribir solas. "
            "Ponete dos horas y cerralas mientras todavía te acordás.", 1)),
        ("hc36_cierre_3.png", punto(
            None, "Cuánto cobraste de verdad.",
            "Lo facturado dividido las horas trabajadas, todas. El número "
            "casi nunca coincide con lo que uno cree, y es el que tendría "
            "que ordenar tus decisiones del año que viene.", 2)),
        ("hc36_cierre_4.png", punto(
            None, "Los pacientes que dejaron de venir.",
            "Sin seguimiento formal, las altas y los abandonos se mezclan. "
            "Distinguirlos te dice más de tu práctica que cualquier balance.", 3)),
        ("hc36_cierre_5.png", punto(
            None, "Si tu copia de seguridad existe.",
            "No «si está activada»: si la probaste. Una copia que nunca se "
            "restauró es una copia que no sabés si sirve.", 4)),
        ("hc36_cierre_6.png", punto(
            None, "Cómo vas a arrancar en marzo.",
            "El mejor momento para cambiar de sistema es enero, con la agenda "
            "vacía. En marzo ya estás corriendo y todo queda para el año que "
            "viene otra vez.", 5)),
        ("hc36_cierre_7.png", cta(
            "Probalo con la agenda tranquila",
            "Dos pacientes reales, sin tarjeta y sin vencimiento. Si te "
            "ordena el verano, en marzo ya lo tenés andando.",
            "PROBALO GRATIS · LINK EN BIO", "HCARG.COM.AR", "teal")),
    ]


# ── 30/10 · pregunta abierta ──────────────────────────────────────────────
# Iba a ser otro "hecho por un colega", pero ese angulo ya sale el 14/09
# (hc14) y el 04/10 (hc24). Tres veces en seis semanas es repetirse. Una
# pregunta abierta, en cambio, junta comentarios — que tambien empujan el
# alcance — y de paso devuelve ideas para las proximas tandas.
def p37_pregunta():
    return texto_suelto(
        "CONTAME",
        "¿Qué es lo que más te cuesta de la parte administrativa?",
        "Facturar, registrar, coordinar turnos, cobrar, encontrar un dato "
        "viejo. Leo todas las respuestas: de ahí salen las próximas "
        "funciones de la app.",
        "RESPONDÉ EN LOS COMENTARIOS", "rosa")


def main():
    placas = []
    placas += p26_que_no_escribir()
    placas.append(("hc27_guardar.png", p27_cuanto_guardar()))
    placas += p28_oficio()
    placas.append(("hc29_ausencias.png", p29_ausencias()))
    placas += p30_como_anotar()
    placas.append(("hc31_backup.png", p31_backup()))
    placas += p32_consentimiento()
    placas.append(("hc33_facturar.png", p33_facturar()))
    placas += p34_teleconsulta()
    placas.append(("hc35_contacto.png", p35_primer_contacto()))
    placas += p36_cerrar_anio()
    placas.append(("hc37_pregunta.png", p37_pregunta()))
    guardar(placas, "preview_octubre2_hc.jpg", cols=7)


if __name__ == "__main__":
    main()
